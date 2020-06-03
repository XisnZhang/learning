#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

示例 1:

输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

输出:
"apple"
示例 2:

输入:
s = "abpcplea", d = ["a","b","c"]

输出:
"a"
"""


class Solution:
    def findLongestWord(self, s, d):
        result = ""
        d = sorted(d, key=lambda x: (-len(x), x))
        for w in d:
            if list(set(w) - set(s)):
                continue
            i, j, m, n = 0, len(w) - 1, 0, len(s) - 1
            while i < j and m < n:
                while w[i] != s[m] and m < n:
                    m += 1

                while w[j] != s[n] and m < n:
                    n -= 1
                if w[j] == s[n] and i < j and m < n:
                    j -= 1
                    n -= 1
                if w[i] == s[m] and i < j and m < n:
                    i += 1
                    m += 1

            if i >= j and m <= n:
                return w
        return result


import re


class Solution2:
    """超时"""

    def findLongestWord(self, s, d):
        result = ""
        d = sorted(d, key=lambda x: (-len(x), x))
        for w in d:
            r = "[a-zA-Z]*".join(w)
            if re.search(r, s):
                return w

        return result


if __name__ == '__main__':
    # s = "abpcplea"
    # d = ["ale", "apple", "monkey", "plea"]
    s = "abpcplea"
    d = ["a", "b", "c"]
    print(Solution2().findLongestWord(s, d))
