#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
问题定义：
在一个夜黑风高的晚上，有n（n <= 50）个小朋友在桥的这边，现在他们需要过桥，但是由于桥很窄，每次只允许不大于两人通
过，他们只有一个手电筒，所以每次过桥的两个人需要把手电筒带回来，i号小朋友过桥的时间为T[i]，两个人过桥的总时间为
二者中时间长者。问所有小朋友过桥的总时间最短是多少。
"""
import sys


class ChildrenRiver:
    def __init__(self, times):
        self.times = sorted(times)

    def solution1(self):
        """贪婪算法，不一定能得到最优解"""
        times = sorted(self.times)
        return times[0] * (len(times) - 2) + sum(times[1:])

    def solution2(self):
        """
        前i个人过河分两种情况：
        1）河这边余一个人i,手电筒在对岸，则只需要对岸最快的人将手电送过来a[0]，再和i一起过河即可
        2）河这边余两个人i和另外一个人，手电筒在对岸，则只需要对岸最快的人将手电送过来，再让i和另一个人一起过河，
           再让对边最快的人a[1]将手电送过来即可
        :return:
        """
        n = len(self.times)
        # #注意边界问题
        if n <= 0:
            return 0
        elif n <= 2:
            return self.times[-1]

        d = [sys.maxsize] * n
        d[0] = self.times[0]
        d[1] = self.times[1]
        for i in range(2, n):
            d[i] = min(d[i - 1] + self.times[0] + self.times[i],
                       d[i - 2] + self.times[0] + self.times[i] + 2 * self.times[1])
        print(d)
        return d[n - 1]


if __name__ == '__main__':
    # times = [1, 2, 5, 10]
    times = [1]
    slu = ChildrenRiver(times)
    print(slu.solution2())
