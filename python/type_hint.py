#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# @Time : 20-1-15 上午10:12 
# @Author : shixi 
# @Site : shixi.zhang@cloudminds.com 
# @File : type_hint.py 

"""
type hint
var:type, 对该变量类型的注释说明，python3.5新增
"""
import jieba


def add(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    a: int = 5
    print(a)
    print(add(2, 3))

    # with open("./test.txt", "w") as f:
    #     f.write("{}\n".format("ddd"))
    #     f.write("{}\n".format("fff"))

    print(list(jieba.cut("你知道呦")))
