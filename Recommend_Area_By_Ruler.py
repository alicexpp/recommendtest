# coding=utf-8
# 利用规则引擎，为钢卷推荐小区域

import sys
from pyke import knowledge_engine
from pyke import krb_compiler
from pyke import krb_traceback
from pyke import goal
import ibm_db
import ibm_db_dbi


# 连接数据库
conn = ibm_db.connect("DRIVER = {IBM DB2 ODBC DRIVER}; DATABASE=UACSDB0; HOSTNAME=10.25.101.8;PORT=50000;"
                      "PROTOCOL = TCPIP; UID=UACSAPP;PWD=UACSAPP;","","")
conn_ibm_dbi=ibm_db_dbi.connect("DRIVER={IBM DB2 ODBC DRIVER};DATABASE=UACSDB0;HOSTNAME=10.25.101.8;"
                                "PORT=50000;PROTOCOL=TCPIP;UID=UACSAPP;PWD=UACSAPP;","","")
if conn:
    print "connect db2 successed!"

#

engine = knowledge_engine.engine(__file__)
# 激活事实库
engine.activate('fc_area_recommend')


# 读取数据库中，每个小区的长度、宽度以及当前库容率
def select_data(table_name, area_name):
    sql="SELECT * FROM %s WHERE STOCK_NAME='%s'"% (table_name, area_name)
    stmt = ibm_db.exec_immediate(conn, sql)
    row = ibm_db.fetch_assoc(stmt)
    return row['MAX_LENGTH'], row['MAX_WIDTH'], row['CURRENT_RATIO']


# 判断库满的函数
def fc_test(coil_kind, external_diameter, width, status1=1):
    fc_goal = goal.compile('coil_area.move_area($coil_kind,$area,$status)')
    try:
        with fc_goal.prove(engine, coil_kind=coil_kind, status=status1) as gen:
            for vars, plan in gen:
                # 读取数据库中库区的信息
                # 当前库区的最大长度
                Max_Length = select_data('UACS_STOCK_INFO', vars['area'])[0]
                # 当前库区的最大宽度
                Max_Width = select_data('UACS_STOCK_INFO', vars['area'])[1]
                # 当前库区的库容率
                Current_Ratio = select_data('UACS_STOCK_INFO', vars['area'])[2]
                #  计算该钢卷放入之后的库容率
                Cal_Capacity= Current_Ratio + (external_diameter * width)/ (Max_Length * Max_Width)
                # print "若该钢卷放入%s区域，库容率为%f"%(vars['area'],Cal_Capacity)
                if Cal_Capacity < 1 :
                    print"%s should be played in %s" % (coil_kind, vars['area'])
                    return vars['area'],status1
                else:
                    print "the %s area is full!" % (vars['area'])
                    status_1 = status1 + 1
                    return fc_test(coil_kind, external_diameter, width, status1=status_1)
        return "null"
    except:
        print "something err"
        krb_traceback.print_exc()
        sys.exit()