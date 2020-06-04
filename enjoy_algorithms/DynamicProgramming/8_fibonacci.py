#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time


class fibonacci:
    def solution1(self, n):
        """
        递归计算，子问题会被重复计算，如f(5) = f(4)+f(3), 又需要计算一遍f(4)和f(3)
        重复计算，速度比较慢
        """
        if n < 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return self.solution1(n - 1) + self.solution1(n - 2)

    def solution2(self, n):
        """
        备忘录，记录下之前已经计算过的结果
        自顶向下
        """
        if n < 0:
            return n
        memo = [-1] * (n + 1)

        def _fib(n):
            if memo[n] != -1:
                return memo[n]
            elif n <= 2:
                memo[n] = 1
            else:
                memo[n] = _fib(n - 1) + _fib(n - 2)
            return memo[n]

        r = _fib(n)
        print(memo)
        return r

    def solution3(self, n):
        if n <= 0:
            return 0
        elif n <= 2:
            return 1
        memo = [-1] * (n + 1)
        memo[1], memo[2] = 1, 1
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]

    def solution4(self, n):
        """
        对方案3进行空间优化, 实际上只用到了f(n-1)和f(n-2),所以只需保留这两个位置的数即可
        """
        if n <= 0:
            return 0
        elif n <= 2:
            return 1
        f_1, f_2, f = 1, 1, 2
        for i in range(3, n + 1):
            f = f_1 + f_2
            f_2 = f_1
            f_1 = f
        return f


if __name__ == '__main__':
    fib = fibonacci()
    start = time.time()
    """
    solution1: 递归fib(20), time: 5.98ms
    solution2: 备忘录，以空间换时间，time: 1ms以内
    """
    print(fib.solution2(20))
    print((time.time() - start) * 1000.)
