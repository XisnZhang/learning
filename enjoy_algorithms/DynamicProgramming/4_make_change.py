#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题定义：给定一组货币面额， 和一个零钱总数，给出合适的零钱组合，货币数目应尽可能地少
"""
import sys


class solution:
    def __init__(self, changes):
        self.changes = changes

    def make_change(self, total_num):
        """贪心算法：每个子问题选择最优解
        """
        changes = sorted(self.changes, reverse=True)
        result = []
        diff = total_num
        for c in changes:
            while c <= diff and diff > 0:
                result.append(c)
                diff = total_num - sum(result)
        return result


class solution2:
    """动态规划，返回最少的钞票数目和组合方案"""
    def __init__(self, changes):
        self.changes = sorted(changes)

    def make_change(self, total_change):
        d = [sys.maxsize] * (total_change + 1)
        d[0] = 0
        rs = [[] for _ in range(total_change+1)]
        for i in range(1, total_change + 1):
            for c in self.changes:
                if c <= i:
                    if d[i - c] + 1 < d[i]:
                        d[i] = d[i - c] + 1
                        rs[i] = [c]+rs[i-c]
        return rs[total_change]


if __name__ == '__main__':
    slu = solution2([1, 5, 11])
    print(slu.make_change(15))
