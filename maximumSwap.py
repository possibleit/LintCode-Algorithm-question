#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
@Author : possibleit
@Date : 17:10 2019/3/29
@Description : 给定一个非负整数，你可以交换两个数位至多一次来获得最大的合法的数。
    返回最大的合法的你能够获得的数。
    1.给定的数字在 [0, 10^8] 内。
@Example :
    样例1:
    输入: 2736
    输出: 7236
    解释: 交换数字2和数字7.
    样例2:
    输入: 9973
    输出: 9973
    解释: 不用交换.
@Solution :
    思路是将所给的'num'(10^8)转化成一个list，例如2736，转化成[6,3,7,2]
    之后从list中取出最后一个数字，即所给'num'的第一个数字，并用余下的list与
    此数字比较，若存在比它大的，则交换位置，并将交换过程中较大的数字加到list末尾；
    若不存在，则将取出最后一个数字的list当作新的list，递归进行上述操作后，将取出
    的数字加到list末尾；最终将list转化位数字返回即可。
'''
def maximumSwap(num):
    if num <= 10:
        return num
    list = []
    pre = num
    i = 10
    while pre >= 1:
        bot = pre % i;
        pre = pre / i;
        bot = int(bot)
        list.append(bot)
    list = set(list)
    x = len(list) - 1
    s = list[x]
    while x > 0:
        s = s * 10 + list[x - 1]
        x = x - 1
    return s

def set(list):
    #list[6,3,7,2]
    if len(list) < 1:
        return list
    x = len(list) - 1
    xs = list[x]
    xx = xs
    del list[x]#list[6,3,7]
    for i in list:
        if i > xs:
            xs = i
    if xs == xx:
        set(list)
    else:
        index = list.index(xs)
        list[index] = xx#list[6,3,2]
    list.append(xs)#list[6,3,2,7]
    return list

print (maximumSwap(2736))