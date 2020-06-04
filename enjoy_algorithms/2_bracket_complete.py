#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
问题定义：判断一个表达式中的括号是否匹配
"""


class solution:
    def bracket_complete(self, s):
        a = []
        for char in s:
            if char == "(":
                a.append(char)
            elif char == ")":
                if not a:
                    return False
                a.pop()

        return len(a) == 0

    def bracket_complete_2(self, s):
        """空间优化"""
        left_count = 0
        for char in s:
            if char == "(":
                left_count += 1
            elif char == ")":
                if left_count < 1:
                    return False
                left_count -= 1
        return left_count == 0


if __name__ == '__main__':
    ss = ["hh)jjj",
          "(ddj(j())",
          "ddPPP(()d)",
          "ddd((dd))d)"]
    slu = solution()
    for s in ss:
        print(s, slu.bracket_complete_2(s))
