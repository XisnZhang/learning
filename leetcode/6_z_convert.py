#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# @Time : 19-11-20 下午12:20 
# @Author : shixi 
# @Site : shixi.zhang@cloudminds.com 
# @File : 6_z_convert.py 
"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
"""


class Solution:
    def convert(self, s, numRows):
        if len(s) < numRows or numRows == 1:
            return s
        l = len(s)
        m = []
        for a in s[:numRows]:
            m.append(a)
        row = numRows - 2

        i = numRows
        while i < l:
            while row > 0 and i < l:
                m[row] += s[i]
                row = row - 1
                i += 1
            while row < numRows - 1 and i < l:
                m[row] += s[i]
                row += 1
                i += 1

        return "".join(m)


if __name__ == '__main__':
    s = "LEETCODEISHIRING"
    numRows = 3
    print(Solution().convert(s, numRows))
