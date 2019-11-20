#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# @Time : 19-11-19 下午6:27 
# @Author : shixi 
# @Site : shixi.zhang@cloudminds.com 
# @File : 5_longest_palindrome.py 
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        核心思想：遍历所有的中心点，寻找每个中心点对应的最长回文子串，即计算每个中心点的回文半径
        时间复杂度为o(n*n)
        :param s:
        :return:
        """
        if not s:
            return ""
        # #使得奇偶回文串处理方式一样
        s = "#" + "#".join(s) + "#"
        result = ""
        for i, a in enumerate(s):
            if i == 0:
                continue
            j = i - 1
            k = i + 1
            while j > 0 and k < len(s):
                if s[j] == s[k] == "#":
                    j -= 1
                    k += 1
                elif s[j] == s[k] != "#":
                    j -= 2
                    k += 2
                else:
                    break
            rs = s[j + 1:k]
            if len(rs) > len(result):
                result = rs

        return result.replace("#", "")


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        """马拉车算法
           核心思想：遍历所有的中心点，寻找每个中心点对应的最长回文子串，计算每个中心点的回文半径
           在计算回文半径的时候，一直更新两个变量，已经计算的回文串的最右点mx以及该最右点对应的中心点mid，
           在计算后续中心点的回文半径时，充分利用mx和mid
           时间复杂度为o(n)
        """

        if len(s) <= 1:
            return s
        # # 在字符串中插入"\1"可以使得奇偶串均变为奇数串，便于处理
        # # 在末尾加入两个不同的字符，可直接中断循环，而不用每次验证是否越界
        s_new = '\0' + '\1' + '\1'.join(s) + '\1' + '\2'
        l = len(s_new)

        mx = 0  # 已遍历的最大右边界
        mid = 0  # 对应的中心点
        p = [0] * l  # 扩散半径数组，不包括中心点自己
        for i in range(1, l - 1):
            if i < mx:
                # #充分利用最右边界
                j = 2 * mid - i  # # i 关于mid的对称点
                # #mx-i是mx可能不能涵盖住i+p[j]这个部分，只能涵盖住mx-i, 超过的部分需要一个个判断
                p[i] = min(mx - i, p[j])

            while s_new[i - p[i] - 1] == s_new[i + p[i] + 1]:
                p[i] += 1

            # 记录一下mx和mid(mx必须是最右边点，所以i+p[i]>mx时才更新)
            if i + p[i] > mx:
                mx = i + p[i]
                mid = i
        maxr = max(p)
        maxr_id = p.index(maxr)
        return s_new[maxr_id - maxr:maxr_id + maxr + 1].replace('\1', '')


if __name__ == '__main__':
    s = "babad"
    # s = "cbbd"
    print(Solution2().longestPalindrome(s))
    # print(longestPalindrome5(s))
