#coding:utf-8

"""
    一个背包里可放入总量为weight的物品，现有n件物品的集合S，其中物品的
    重量分别为w1,w2,..., 能否从中选出若干件物品，其重量之等于weight
"""

def bag(total_weight, weight_list, n):
    if total_weight == 0:
        return True

    if total_weight < 0 or total_weight > 0 and n < 1:
        return False

    if bag(total_weight - weight_list[n - 1], weight_list, n - 1):
        print n, weight_list[n - 1]
        return True

    if bag(total_weight, weight_list, n - 1):
        return True

    else:
        return False


print bag(10, [1, 2, 3, 4], 4)