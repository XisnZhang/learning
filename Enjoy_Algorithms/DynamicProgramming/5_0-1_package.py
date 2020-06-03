#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题定义：
有一个背包，最多能承受重量为c的物品，现有n个物品，给定每件物品的重量w_i和价值v_i,要求从n个物品中选择合适的物品，使得质量不超过c,价值最大
"""

import sys


class solution:
    """贪心算法"""

    def __init__(self, values, weights):
        assert len(values) == len(
            weights), "values and weights are not map. # of values: {:d}, # of weights: {:d}".format(len(values),
                                                                                                     len(weights))
        self.packs = []
        for v, w in zip(values, weights):
            self.packs.append(dict(weight=w, value=v, status=0))

    def find_pack_with_values(self, total_weight):
        """每次拿value最大的pack"""
        idx = -1
        max_p = 0
        for i, p in enumerate(self.packs):
            if p["weight"] < total_weight and p["status"] == 0:
                if p["value"] > max_p:
                    idx = i
                    max_p = p["value"]
        if idx != -1:
            self.packs[idx]["status"] = 1
        return idx

    def find_pack_with_weights(self, total_weight):
        """每次拿重量最轻的pack"""
        idx = -1
        min_weight = sys.maxsize
        for i, p in enumerate(self.packs):
            if p["weight"] <= total_weight and p["status"] == 0:
                if p["weight"] < min_weight:
                    idx = i
                    min_weight = p["weight"]
        if idx != -1:
            self.packs[idx]["status"] = 1
        return idx

    def find_pack_with_ratio(self, total_weight):
        """按最大价值密度选择"""
        idx = -1
        max_ratio = 0.0
        for i, p in enumerate(self.packs):
            if p["weight"] <= total_weight and p["status"] == 0:
                ratio = float(p["value"]) / p["weight"]
                if ratio > max_ratio:
                    idx = i
                    max_ratio = ratio
        if idx != -1:
            self.packs[idx]["status"] = 1
        return idx

    def package(self, total_wight, policy="value"):
        """
        贪心算法：每次选择价值最高的物品
        """
        results = []
        if policy == "weight":
            choice_func = self.find_pack_with_weights
        elif policy == "ratio":
            choice_func = self.find_pack_with_ratio
        else:
            choice_func = self.find_pack_with_values

        idx = choice_func(total_wight)
        while idx != -1 and total_wight >= 0:
            results.append(idx)
            total_wight = total_wight - self.packs[idx]["weight"]
            # print(idx, total_wight)
            idx = choice_func(total_wight)
        all_weights = sum([self.packs[idx]["weight"] for idx in results])
        all_values = sum([self.packs[idx]["value"] for idx in results])
        print("policy: {}, packages: {}, all weights: {:d}, all values: {:d}".format(policy, results, all_weights,
                                                                                     all_values))


class solution2:
    """
    动态规划
    """

    def __init__(self, weights, values):
        assert len(weights) == len(values)
        self.packs = []
        for v, w in zip(values, weights):
            self.packs.append(dict(weight=w, value=v, status=0))

    def package(self, total_weight):
        s = [[0] * (total_weight + 1) for _ in range(len(self.packs))]
        for i, p in enumerate(self.packs):
            for j in range(1, total_weight + 1):
                if j < p["weight"]:
                    s[i][j] = s[i - 1][j]
                else:
                    s[i][j] = max(s[i - 1][j], s[i - 1][j - p["weight"]] + p["value"])
        print(s)

    def package2(self, total_weight):
        """空间优化"""
        s = [0 for _ in range(total_weight + 1)]
        for i, p in enumerate(self.packs):
            """
            s[i][w] = max(s[i-1][w],  s[i-1][w-w_i]+v_i)
            在计算s[i][w]的时候，需要比较的是s[i-1][w] 和 s[i-1][w-w_i]+v_i,
            如果只用一个数组s[w]来表示的话，则需要保证在计算s[i][w]的时候，s[w-w_i]里保存的是i-1时刻的s[w-w_i],
            因此weight需要逆序计算，否则在计算i的时候，w-w_i会先计算，则s[w-w_i]里保存的就是i时刻的s[w-w_i]了
            """
            for j in range(total_weight, 0, -1):
                if j >= p["weight"] and s[j] < s[j - p["weight"]] + p["value"]:
                    s[j] = s[j - p["weight"]] + p["value"]

        print(s)
        # print(r)


if __name__ == '__main__':
    """ [5, 1, 6, 3, 0], all weights: 150, all values: 170 """
    weights = [35, 30, 60, 50, 40, 10, 25]
    values = [10, 40, 30, 50, 35, 40, 30]
    # slu = solution(
    #     weights=weights,
    #     values=values
    # )
    # slu.package(total_wight=150, policy="ratio")
    slu = solution2(
        weights=weights,
        values=values
    )
    slu.package2(total_weight=150)
