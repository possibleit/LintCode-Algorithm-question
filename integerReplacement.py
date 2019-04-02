#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def integerReplacement(n):
    '''
    @Author : possibleit
    @Date : 13:39 2019/4/2
    @Description : 给定一个正整数n，你可以做如下的操作：
        1:如果n为偶数，将n替换为n/2。
        2:如果n为奇数，你可以将n替换为n + 1或n - 1。
        将n转换为1的最少的替换次数为多少？
    @Example :
        输入：8
        输出：3
        说明：8 -> 4 -> 2 -> 1
    @Solution :
        看到这道题，第一想法是动态规划，因为这道题的最优解有如下结构，
        if n % 2 == 0
            s(n) = s(n/2) + 1
        else
            s(n) = min(s(n + 1),s(n - 1)) + 1
        按照这个解法就可以解出题目
        但是运行时间过长，第一次提交运行时间2717ms

        于是在这道题的笔记中，我看到了一位网友(snipers)答案，构造广度优先搜索。
    '''
    if n == 1:
        return 0;
    if (n % 2) == 0:
        return integerReplacement(n / 2) + 1
    else:
        return min(integerReplacement(n - 1) + 1, integerReplacement(n + 1) + 1)

print(integerReplacement(7))
