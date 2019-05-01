#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import collections
class TrieNode(object):
    def __init__(self,value=0):
        self.value = value
        self.isword = False
        #OrderDict是Dict的子类，可以记录元素添加的顺序，具体见https://docs.python.org/3.6/library/collections.html?highlight=collections#collections.OrderedDict
        self.children = collections.OrderDict()

    @classmethod
    def insert(cls,root, word):
        p = root
        for c in word:
            child = p.children.get(c)
            if not child:
                child = TrieNode(c)
                p.children[c] = child
            p = child
        p.isword = True


class Solution:
    # @param {char[][]} board a list of lists of char
    # @param {str[]} words a list of string
    # @return {int} an integer
    
    '''
    @Author : @LintCode参考答案
    @Date : 16:28 2019/4/18
    @Description : 描述
        给定一个2D矩阵包括 a-z 和字典 dict，找到矩阵上最大的单词集合，这些单词不能在相同的位置重叠。返回最大集合的大小
        字典中的单词不重复
        可以重复使用字典中的单词
    @Example :
        Input:
        ["abc","def","ghi"]
        {"abc","defi","gh"}
        Output:
            3
        Explanation:
            we can get the largest collection`["abc", "defi", "gh"]`
    @Solution :
        使用深度优先和回溯的方法，在矩阵上搜索，同时使用前缀树来优化搜索
    '''
    def boggleGame(self, board, words):
        # Write your code here
        self.board = board
        self.words = words
        self.m = len(board)
        self.n = len(board[0])
        self.results = []
        self.temp = []
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]

        self.root = TrieNode()
        for word in words:
            TrieNode.insert(self.root, word)

        self.dfs(0, 0, self.root)

        return len(self.results)

    def dfs(self, x, y, root):
        for i in range(x, self.m):
            for j in range(y, self.n):
                paths = []
                temp = []
                self.getAllPaths(i, j, paths, temp, root)
                for path in paths:
                    word = ''
                    for px, py in path:
                        word += self.board[px][py]
                        self.visited[px][py] = True
                    self.temp.append(word)

                    if len(self.temp) > len(self.results):
                        self.results = self.temp[:]

                    self.dfs(i, j, root)
                    self.temp.pop()
                    for px, py in path:
                        self.visited[px][py] = False
            y = 0

    def getAllPaths(self, i, j, paths, temp, root):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or \
                self.board[i][j] not in root.children or \
                self.visited[i][j] == True:
            return

        root = root.children[self.board[i][j]]
        if root.isWord:
            temp.append((i, j))
            paths.append(temp[:])
            temp.pop()
            return

        self.visited[i][j] = True
        deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in deltas:
            newx = i + dx
            newy = j + dy
            temp.append((i, j))
            self.getAllPaths(newx, newy, paths, temp, root)
            temp.pop()
        self.visited[i][j] = False