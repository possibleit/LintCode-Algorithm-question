#!/usr/bin/env python 
# -*- coding:utf-8 -*-
    
def MinimumString(s, k):
    '''
    @Author : possibleit
    @Date : 22:44 2019/4/10
    @Description : 描述
        给定一个长度为n的只含小写字母的字符串s，从里面去掉k个字符，得到一个长度为n-k的新字符串。设计算法，输出字典序最小的新字符串。
        此题中字典序的定义：首先比较两个字符串的长度，长度小的字典序更小，如果长度相同，则从字符串左边开始逐位比较，找到第一位不同的字符，对应字符小的字符串的字典序更小。
        如："abbz"和"abza"，首先两个字符串的长度相同，则从左边开始逐位比较：
        第一位都是"a"，则继续比较下一位
        第二位都是"b"，则继续比较下一位
        第三位第一个字符串是"b"，而第二个字符串是"z"，因为"b" < "z"，故第一个字符串的字典序更小。
        0≤k<n≤100000
    @Example :
        Input: s = "abccc", k = 2
        Output: "abc"`
        Explanation：
        Delete the `c` of the 4th and 5th positions
    @Solution :
        参考答案：贪心策略，删除前k个(前一个数大于后一个)的情况，如果不够k个，则删除末尾的若干个
    '''
    n = len(s)
    cnt = 0
    news = [0 for i in range(n)]
    lim = n - k
    for i in range(n):
        while cnt > 0 and k > 0 and news[cnt - 1] > s[i]:
            cnt -= 1
            k -= 1
        news[cnt] = s[i]
        cnt += 1
    return ''.join(news[:lim])
print(MinimumString("acbcc",2))