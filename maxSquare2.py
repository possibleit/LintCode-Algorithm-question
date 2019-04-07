#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def maxSquare2(matrix):
    '''
    @Author : @lintCode参考答案
    @Date : 12:23 2019/4/7
    @Description :给出一个只有 0 和 1 组成的二维矩阵，找出最大的一个子矩阵，
        使得这个矩阵对角线上全是 1 ，其他位置全是 0 .只考虑主对角线。
    @Example :
        输入:
        [[1,0,1,0,0],
         [1,0,0,1,0],
         [1,1,0,0,1],
         [1,0,0,1,0]]
        输出:9
        解释:
            [0,2]->[2,4]
    @Solution :

    '''
    if not matrix or not matrix[0]:
        return 0

    n, m = len(matrix), len(matrix[0])
    f = [[0] * m for _ in range(n)]
    up = [[0] * m for _ in range(n)]

    for i in range(m):
        f[0][i] = matrix[0][i]
        up[0][i] = 1 - matrix[0][i]

    edge = max(matrix[0])
    for i in range(1, n):
        f[i][0] = matrix[i][0]
        up[i][0] = 0 if matrix[i][0] else up[i - 1][0] + 1
        left = 1 - matrix[i][0]
        for j in range(1, m):
            if matrix[i][j]:
                f[i][j] = min(f[i - 1][j - 1], left, up[i - 1][j]) + 1
                up[i][j] = 0
                left = 0
            else:
                f[i][j] = 0
                up[i][j] = up[i - 1][j] + 1
                left += 1

        edge = max(edge, max(f[i]))

    return edge * edge



S = [[1,0,1,0,0],
    [1,0,0,1,0],
    [1,1,0,0,1],
    [1,0,0,1,0]]
print(maxSquare2(S))