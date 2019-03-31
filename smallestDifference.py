#usr/bin/env python
# -*- coding:utf-8 -*-
import sys
#'''
#    二分法求解，但是时间会超。
#'''
# def smallestDifference(A, B):
#     sys.setrecursionlimit(1000000)
#     tem = sys.maxsize
#     listA = sorted(A)
#     listB = sorted(B)
#     i = len(listA)
#     j = len(listB)
#     if i < 2 and j < 2:
#         return abs(listB[0] - listA[0])
#     if i < j:
#         for s in range(i):
#             # 二分查找listB中a的元素
#             tem = min(tem, binsearch(listA[s], listB))
#     else:
#         for s in range(j):
#             tem = min(tem, binsearch(listB[s], listA))
#     return tem
#
# def binsearch(a, list):
#     l = len(list)
#     if l == 1:
#         return abs(a - list[0])
#     if l == 2:
#         return min(abs(a - list[0]), abs(list[1] - a))
#     x = int(l / 2)
#     ss = sys.maxsize
#     if a == list[x]:
#         ss = 0
#     elif a > list[x]:
#         ss = binsearch(a, list[x:l])
#     else:
#         ss = binsearch(a, list[0:x])
#     return ss

def smallestDifference(A, B):
    '''
    @Author : possibleit
    @Date : 12:21 2019/3/31
    @Description :
        描述
            给定两个整数数组（第一个是数组 A，第二个是数组 B），在数组 A 中取 A[i]，数组 B 中取
            B[j]，A[i] 和 B[j]两者的差越小越好(|A[i] - B[j]|), 返回最小差。
            挑战时间复杂度 O(n log n)
    @Example :
        样例 1:
            输入: A = [3, 6, 7, 4], B = [2, 8, 9, 3]
            输出: 0
            解释: A[0] - B[3] = 0
        样例 2:
            输入: A = [1, 2, 3, 4], B = [7, 6, 5]
            输出: 1
            解释: B[2] - A[3] = 1
            挑战
            时间复杂度 O(n log n)
    @Solution :
        最开始我想到的解决方法是上边的方法，但是有两个问题，一是递归深度超标(sys.setrecursionlimit(1000000)),
        二是运行到后边如果输入的数据量过大会超时。之后我在一个用户(@dxqwouTgUxyn)的笔记(two pointers in two arrays. ida and idb, these two pointers starting from beginning of A and B. then move from left to right, in the meantime, we will update minDif. then we will judge A[ida] ? B[idb]. in order to get minum difference, if A[ida] > B[idb], we need to enlarge B[idb], therefore idb++; samewise as A.)中找到了思路,具体方法就是用两个指针，分别指向A和B
        比较指针所指向的数据，若其中一个数小于另一个数，则将指针右移，继续比较，在这个过程中记录最小的值。
        比较的结束条件是遍历完一个数组。
    '''
    listA = sorted(A)
    listB = sorted(B)
    i = len(listA)
    j = len(listB)
    minx = sys.maxsize
    s = 0
    m = 0
    while 1:
        if s >= i or m >= j:
            break;
        if listA[s] > listB[m]:
            minx = min(minx, abs(listA[s] - listB[m]))
            m = m + 1
        else:
            minx = min(minx, abs(listA[s] - listB[m]))
            s = s + 1
    return minx