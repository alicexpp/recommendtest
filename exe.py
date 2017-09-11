# coding=utf-8
#  执行测试程序
import random
from Interface import recommend_stock_position
if __name__=="__main__":
    while True:
        # external_diameter =raw_input("请输入钢卷外径：")
        external_diameter = random.randint(1000, 1200)
        print "请输入钢卷外径:", external_diameter
        # width = raw_input("请输入钢卷宽度：")
        width = random.randint(1300, 2000)
        print "请输入钢卷宽度：", width
        steel_kind_list = ["back_closed_coil", "hot_closed_coil", "finished_product", "back_coil", "hot_coil",
                           "2030", "back_retreat_coil", "hot_retreat_coil", "back_return_coil"]
        steel_name = random.sample(steel_kind_list, 1)[0]
        print "钢卷种类：", steel_name
        print recommend_stock_position(steel_name, float(external_diameter), float(width))
        # print recommend_stock_position('UACS_STOCK_INFO', 'hot_coil', float(external_diameter), float(width))
