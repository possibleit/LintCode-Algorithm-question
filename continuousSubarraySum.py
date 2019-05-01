#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def continuousSubarraySum(A):
    '''
    @Author : Qian
    @Date : 10:23 2019/5/1
    @Description :
        描述:
            给定一个整数数组，请找出一个连续子数组，使得该子数组的和最大。输出答案时，
            请分别返回第一个数字和最后一个数字的下标。（如果存在多个答案，请返回字典序最小的）
    @Example :
    Example1:
        输入: [-3, 1, 3, -3, 4]
        输出: [1, 4]
    Example2:
        输入: [0, 1, 0, 1]
        输出: [0, 3]
        解释: 字典序最小.
    @Solution :
        维护一个int变量start_index作为解的前半部分，当前求和值为cur_sum,全局最优解为max_sum，
        从零开始遍历数组，第一个if判断保证获取的是最优解，第二个if保证cur_sum始终大于0，这就保证了
        start_index右移的正确性。
        另一种方案是双指针遍历
    '''
    if not A:
        return [0,0]
    cur_sum = 0
    start_index = 0
    ans = []
    max_sum = float('-inf')

    for i,n in enumerate(A):
        cur_sum += n
        if max_sum < cur_sum:
            ans = [start_index,i]
            max_sum = cur_sum
        if cur_sum < 0:
            cur_sum = 0
            start_index = i + 1
    return ans
A = [-3,1,3,-3,4]
print(continuousSubarraySum(A))#output[1,4]