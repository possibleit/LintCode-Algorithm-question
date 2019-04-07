#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def longestConsecutive(num):
    '''
    @Author : possibleit
    @Date : 22:55 2019/4/7
    @Description : 给定一个未排序的整数数组，找出最长连续序列的长度。说明:要求你的算法复杂度为O(n)
    @Example :
        样例
        给出数组[100, 4, 200, 1, 3, 2]，这个最长的连续序列是 [1, 2, 3, 4]，返回所求长度 4
    @Solution :
        对给定的每个数字进行以下操作：
            删除n
            判断n-1是否存在，存在则删除，n--
            判断n+1是否存在，存在则删除，n++
    '''
    if len(num) == 1:
        return 1
    mdict = {}
    for m in num:
        mdict[m] = 1
    ans = 0

    for m in num:
        if m in mdict:
            mlen = 1
            del mdict[m]
            left = m - 1
            right = m + 1

            while left in mdict:
                mlen = mlen + 1
                del mdict[left]
                left = left - 1
            while right in mdict:
                mlen = mlen + 1
                del mdict[right]
                right = right + 1

            if ans < mlen:
                ans = mlen
    return ans

num = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(num))