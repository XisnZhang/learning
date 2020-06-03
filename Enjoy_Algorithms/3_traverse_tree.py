#!/usr/bin/env python
# -*- coding: utf-8 -*-

def visit_node(v):
    pass


visited = True
queue = []


def DFS(graph, v):
    """
    图的深度优先遍历
    """
    visit_node(v)  # 访问v点，并标记为已经访问的点
    for vi in v:  # 遍历v的所有邻接点
        if vi is not visited:  # 如果未被访问， 则访问
            DFS(graph, vi)


def BFS(graph, v):
    """
    图的广度优先遍历
    """
    for vi in v:
        if vi is not visited:
            visit_node(vi)  # 访问vi
            queue.append(vi)  # vi入队列
    while queue:
        v = queue.pop(0)  # 队列头部元素出队列
        BFS(graph, v)
