# coding=utf-8
# 给C++调用的接口程序

import ibm_db
import ibm_db_dbi
from Recommend_Area_By_Ruler import fc_test, select_data
from BaseClass import RECT, POINT
from Area_Coordinate_Trans import absolute_to_relative
from Recommend_Saddle_By_Algorithm import find_suit_pos,output_coordinate_x,output_coordinate_y


# 连接数据库
conn = ibm_db.connect("DRIVER = {IBM DB2 ODBC DRIVER}; DATABASE=UACSDB0; HOSTNAME=10.25.101.8;PORT=50000;PROTOCOL=TCPIP;UID=UACSAPP;PWD=UACSAPP;","","")
conn_ibm_dbi=ibm_db_dbi.connect("DRIVER={IBM DB2 ODBC DRIVER};DATABASE=UACSDB0;HOSTNAME=10.25.101.8;PORT=50000;PROTOCOL=TCPIP;UID=UACSAPP;PWD=UACSAPP;","","")
if conn:
    print "connect db2 successed"


# 读取库图数据库中的钢卷占用库区状态,UACS_STOCK_STATUS_TEST,读取出
def read_stock_status(table_name, area_name):
    sql="SELECT * FROM %s WHERE STOCK_NAME = '%s'" % (table_name, area_name)
    c = conn_ibm_dbi.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows


# 放置钢卷后，更新库区的库容率,UACS_STOCK_INFO
def update_area_ratio(table_name, area_name, new_ratio):
    update_ratio = "UPDATE %s SET CURRENT_RATIO = '%f' WHERE STOCK_NAME = '%s' " %(table_name, new_ratio, area_name)
    ibm_db.exec_immediate(conn, update_ratio)
    ibm_db.commit(conn)
    return area_name


# 根据鞍座坐标返回鞍座号
def select_saddle_no(table_name, center_x, center_y):
    sql = "SELECT SADDLE_NO FROM %s WHERE X_CENTER= %d AND Y_CENTER = %d " % (table_name, center_x, center_y)
    c = conn_ibm_dbi.cursor()
    c.execute(sql)
    rows = c.fetchall()
    return rows[0][0]


# 先判断推荐库位，再根据库位推荐相应的库区的函数
def recommend_stock_position(coil_information, external_diameter, width, status1=1):
    area_result = fc_test(coil_information, float(external_diameter), float(width), status1)
    area_name = area_result[0]
    status_n = area_result[1]
    Max_Length = select_data('UACS_STOCK_INFO', area_name)[0]
    Max_Width = select_data('UACS_STOCK_INFO', area_name)[1]
    Current_Capacity = select_data('UACS_STOCK_INFO', area_name)[2]
    print "current storage_capacity is:", Current_Capacity
    # 此处center_x,center_y定义是依据第一个小区的的第一个鞍座坐标定义的
    center_x = 1100
    center_y = 1050
    while float(width) / 2 > center_x:
        center_x = center_x + 2200
    while float(external_diameter) / 2 > center_y:
        center_y = center_y + 600
    print "start center_x:", center_x
    print "start center_y:", center_y
    # steel_information表示小区的rect,所以其坐标也是小区的
    steel_information = RECT(llp=POINT(center_x - float(width) / 2, center_y - float(external_diameter) / 2),
                             length=float(external_diameter), width=float(width))
    # 获取当前区域的steel_list，每个区域的steel_list不同
    # 在该处应该先读取数据库中鞍座的占有情况，将其append到new_steel_list中去
    # 读取的是整个库区中的鞍座坐标占用
    exist_steel_lists = read_stock_status('UACS_STOCK_STATUS_TEST', area_name)
    new_steel_list = []
    for item in exist_steel_lists:
        CENTER_X = item[1]
        CENTER_Y = item[2]
        # 将X_CENTER(大区坐标)转换成小区坐标
        center_x_exist = absolute_to_relative(area_name, CENTER_X, CENTER_Y)[0]
        # 将Y_CENTER(大区坐标)转换成小区坐标
        center_y_exist = absolute_to_relative(area_name, CENTER_X, CENTER_Y)[1]
        external_diameter_exist = item[4]
        width_exist = item[5]
        steel_exist = RECT(llp=POINT(center_x_exist-width_exist/2., center_y_exist-external_diameter/2.),
                           length=float(external_diameter_exist), width=float(width_exist))
        new_steel_list.append(steel_exist)
    recommend_result = find_suit_pos(steel_information, new_steel_list, Max_Length, Max_Width, area_name,
                                     Current_Capacity)
    if recommend_result != False:
        new_storage_capacity = recommend_result[0]
        recommend_saddle_rect = recommend_result[1]
        update_area_ratio('UACS_STOCK_INFO', area_name, new_storage_capacity)
        print "after place coil the storage_capacity is:", new_storage_capacity
        # 推荐的鞍座坐标
        saddle_center_x = output_coordinate_x(recommend_saddle_rect)
        saddle_center_y = output_coordinate_y(recommend_saddle_rect)
        # 更新库区状态数据库
        update_stock_status="INSERT INTO UACS_STOCK_STATUS_TEST(STOCK_NAME,X_CENTER,Y_CENTER,COIL_KIND_NAME," \
                            "COIL_OUT_LENGTH,COIL_WIDTH) VALUES('%s','%.2f',%.2f,'%s',%d,%d)"%\
                            (area_name,saddle_center_x,saddle_center_y,coil_information,external_diameter,width)
        ibm_db.exec_immediate(conn, update_stock_status)
        saddle_no = select_saddle_no('UACS_SADDLE_TEST', saddle_center_x, saddle_center_y)
        print "Finally select saddle_no is :", saddle_no
        return saddle_no
    else:
        # 加入Flag标志位，是为了表示当库容率小于1，但是却没有鞍座可以放置的情况，因此fc_test中也需要加入Flag作为判断
        print "the saddle of  %s area is full" % (area_name)
        status_n = status_n + 1
        return recommend_stock_position(coil_information, external_diameter, width, status_n)


