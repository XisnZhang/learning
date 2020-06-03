#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution1:
    """超出时间限制"""

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        d = [0 for _ in range(len(s))]

        for i, a in enumerate(s):
            if i == 0:
                continue
            start = d[i - 1]
            if a not in s[start:i]:
                d[i] = start
            else:
                print(i, s[i], s[:i], d)
                d[i] = max([d[k] for k in range(i)])
                d[i] = max(d[i], d[i] + s[d[i]:i].find(a))
                if s[i] == s[d[i]]:
                    d[i] = d[i] + 1
        d = [i - d[i] + 1 for i, _ in enumerate(d)]

        return max(d)


class Solution:
    """滑动窗口，时间复杂度为o(n)"""

    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0
        result = 1
        start = 0
        for i, a in enumerate(s):
            index = start + s[start:i].find(a)
            start = index + 1
            length = i - start + 1
            if length > result:
                result = length

        return result


if __name__ == '__main__':
    ss = [
        "aabcabcbb", "bbbb", "ddvvsdf"

    ]
    for s in ss:
        print(s, Solution().lengthOfLongestSubstring(s))
