#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re
def reverseWords(s):
    '''
    @Author : possibleit
    @Date : 13:47 2019/6/4
    @Description : 给定一个字符串句子，反转句子中每一个单词的所有字母，同时保持空格和最初的单词顺序。
        字符串中，每一个单词都是由空格隔开，字符串中不会有多余的空格。
    @Example :
        输入: "Let's take LeetCode contest"
        输出: "s'teL ekat edoCteeL tsetnoc"
    @Solution :
        使用正则表达式匹配字符串中的空格，将结果得到的list中的每个单词翻转之后拼接为新的句子
    '''
    # Write your code here
    # \s匹配[<空格>\t\r\n\f\v]
    if s == ' ' or s == '':
        return s
    l = re.split('\s', s)
    ll = [i[::-1] for i in l]
    result = ''
    for i in ll:
        result += i + ' '
    return result[:-1]

s = "Let's take LeetCode contest"
print(reverseWords(s))