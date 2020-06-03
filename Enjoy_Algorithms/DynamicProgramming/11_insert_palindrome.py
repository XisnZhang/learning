#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题定义：
给定一个长度为n（n <= 1000）的字符串A，求插入最少多少个字符使得它变成一个回文串。
"""
import sys


class InsertPalindrome:
    def __init__(self, s):
        self.s = s

    def solution1(self):
        def _insert(i, j):
            if i >= j:
                return 0
            if self.s[i] == self.s[j]:
                return _insert(i + 1, j - 1)
            else:
                return min(_insert(i + 1, j), _insert(i, j - 1)) + 1

        return _insert(0, len(self.s) - 1)

    def solution2(self):
        s = self.s
        n = len(self.s)
        memo = [[-1] * n for _ in range(n)]

        def _insert(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            if i >= j:
                memo[i][j] = 0
            elif s[i] == s[j]:
                memo[i][j] = _insert(i + 1, j - 1)
            else:
                memo[i][j] = min(
                    _insert(i + 1, j),
                    _insert(i, j - 1)
                ) + 1
            return memo[i][j]

        return _insert(0, n - 1)

    def solution3(self):
        """
        求s[i][j]的最小值，则有两种情况：
        1) s[i] == s[j]: s[i][j] = s[i+1][j-1]
        2) s[i]!= s[j]:
               (1) 在s[j]右侧插入字母s[i], s[i][j] = s[i][j-1]+1
               (2) 在s[i]左侧插入字母s[j], s[i][j] = s[i+1][j]+1
           在(1)(2)中选择较小值

        时间复杂度： o(n^2)
        空间复杂度： o(n^2)
        """
        # # 边界情况处理：
        s = self.s
        n = len(self.s)
        d = [[0] * n for _ in range(n)]
        mid = n // 2  # #c从中间位置向两边递推
        for i in range(mid, -1, -1):
            for j in range(i, n):
                if i == j:
                    d[i][j] = 0
                elif s[i] == s[j]:
                    d[i][j] = d[i + 1][j - 1]
                else:
                    d[i][j] = min(d[i + 1][j], d[i][j - 1]) + 1
        print(d)
        return d[0][-1]

    def solution4(self):
        """
        对solution1进行空间优化？
        空间复杂度可优化至o(n)？
        怎么进行空间优化？？
        """
        s = self.s
        n = len(s)
        mid = n // 2  # #c从中间位置向两边递推
        d = [0] * n  # 保存d[i]?
        for i in range(mid, -1, -1):
            p = 0  # d[i+1][j-1]
            for j in range(i, n):
                if s[i] == s[j]:
                    p = d[i + 1]
                else:
                    p = min(p, d[i+1]+1)
            d[i] = p
        print(d)
        return d[0]


if __name__ == '__main__':
    s = "abdb"
    slu = InsertPalindrome(s)
    print(slu.solution4())
