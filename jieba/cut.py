#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# @Time : 19-12-16 下午7:03 
# @Author : shixi 
# @Site : shixi.zhang@cloudminds.com 
# @File : cut.py
import jieba

if __name__ == '__main__':
    stopwords = ["好的"]
    s = "你 好hello world好的"
    words = " ".join(list(jieba.cut(s)))
    print(words)
