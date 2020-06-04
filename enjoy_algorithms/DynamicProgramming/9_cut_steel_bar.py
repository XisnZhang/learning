#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题定义：
给定一段长度为n的钢条，和一份价格表p_i(i=1,2,...,n),求一个切割方案，使得收益最大

动态规划：实质上还是遍历所有解空间，只是会记录已经计算过的结果，以空间换时间
         两种记录方法：1）自顶向下，从大问题开始递归向下，算得一个子问题结果便记录入备忘录，
                        避免该子问题在后面被重复计算
                    2）自底向上，从最小的子问题开始计算并记录
"""
import time


class StealBarCuting:
    def __init__(self, prices):
        self.prices = prices
        self.func_num = 0

    def solution1(self, n):
        """纯递归求解，遍历所有解空间
            n为8时，该函数执行了256次，递归代价比较大
            空间复杂度为o(1)
        """
        self.func_num += 1
        if n == 0:
            return 0
        q = 0
        for i in range(1, n + 1):
            q = max(q, self.prices[i - 1] + self.solution1(n - i))

        return q

    def solution2(self, n):
        """
        _cut执行37
         自顶向下动态规划， 备忘录，递归
         空间复杂度o(n),以空间换时间
        """
        self.func_num = 0

        if n <= 0:
            return 0
        memo = [-1] * (n + 1)

        def _cut(l):
            self.func_num += 1
            q = 0  # #important, 每一个长度的切分，初始值为0
            if l == 0:
                return 0
            if memo[l] != -1:
                return memo[l]
            for i in range(1, l + 1):
                q = max(q, prices[i - 1] + _cut(l - i))
            memo[l] = q
            return memo[l]

        _cut(n)
        print(memo)
        print(self.func_num)
        return memo[n]

    def solution3(self, n):
        """
        自底向上动态规划，无递归，采用循环方式
        从最小的子问题开始记录结果，空间复杂度o(n),以空间换时间
        """
        if n <= 0:
            return 0
        memo = [0] * (n + 1)
        for i in range(1, n + 1):
            p = 0
            for j in range(1, i + 1):
                p = max(p, self.prices[j - 1] + memo[i - j])
            memo[i] = p
        print(memo)
        return memo[n]


if __name__ == '__main__':
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    sbc = StealBarCuting(prices)
    start = time.time()
    print(sbc.solution2(8))
    print(time.time() - start)
