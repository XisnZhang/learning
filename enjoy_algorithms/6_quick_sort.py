#!/usr/bin/env python
# -*- coding: utf-8 -*-

class solution:

    def pivot(self, a, left, right):
        """找序列中的标兵数的位置
           标兵数的选择：1）最左边的数
                       2）最右边的数
                       3）中间的数
                       4）随机选择的数
           标兵数的位置：左边的数均小于标兵数，右边的数均大于标兵数，标兵数的位置是后续划分的依据
        """
        p = a[right]
        i, j = left, right
        while i < j:
            while a[i] <= p and i < j:
                i += 1
            while a[j] >= p and i < j:
                j -= 1
            a[i], a[j] = a[j], a[i]
        a[j], a[right] = a[right], a[j]
        return j, a

    def _quick_sort(self, a, left, right):
        """子问题划分结束标志，左右处在一个位置，即子序列是一个数字"""
        if left < right:
            pivot, a = self.pivot(a, left, right)
            """标兵数的位置已经确定，无须在参与排序"""
            a = self._quick_sort(a, left, pivot - 1)
            a = self._quick_sort(a, pivot + 1, right)
        return a

    def sort(self, a):
        return self._quick_sort(a, 0, len(a) - 1)


if __name__ == '__main__':
    a = [9, 8, 4, 6, 7, 9]
    print(solution().sort(a))
