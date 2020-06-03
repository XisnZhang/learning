#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# @Time : 20-6-1 下午5:40 
# @Author : shixi 
# @Site : shixi.zhang@cloudminds.com 
# @File : sklearn_decesion_tree_test.py 
from sklearn import tree
from sklearn.datasets import load_iris
import pydotplus
import sys
import os

# python找不到Graphviz
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
if __name__ == '__main__':
    iris = load_iris()
    clf = tree.DecisionTreeClassifier()  # cart决策树
    clf = clf.fit(iris.data, iris.target)
    dot_data = tree.export_graphviz(clf, out_file=None)
    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.write_pdf("iris.pdf")
