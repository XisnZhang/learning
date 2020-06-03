#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy.sparse import csc_matrix


def pageRank(G, s=.85, maxerr=.0001):
    """
     Computes the pagerank for each of the n states Parameters
     ----------
    G: 矩阵表示的关系图， G_ij表示node_i与node_j是否连通，1表示连通，0表示不连通
    s: probability of following a transition. 1-s probability of teleporting
       to another state.
    maxerr: if the sum of pageranks between iterations is bellow this we will
       have converged.
    """
    n = G.shape[0]  # node 个数
    # 将 G into 马尔科夫 A
    A = csc_matrix(G, dtype=np.float)  # #稀疏矩阵的表示
    rsums = np.array(A.sum(1))[:, 0]  # #计算每个节点的出度
    ri, ci = A.nonzero()
    print(A.data)  # #A中的非零数值

    A.data /= rsums[ri]
    sink = rsums == 0
    # 计算PR值，直到满足收敛条件
    ro, r = np.zeros(n), np.ones(n)
    while np.sum(np.abs(r - ro)) > maxerr:  # 当前迭代轮与上次迭代的差值
        ro = r.copy()
        for i in range(0, n):
            Ai = np.array(A[:, i].todense())[:, 0]
            Di = sink / float(n)
            Ei = np.ones(n) / float(n)
            r[i] = ro.dot(Ai * s + Di * s + Ei * (1 - s))
    # 归一化
    return r / float(sum(r))


if __name__ == '__main__':
    # 上面的例子
    G = np.array([[0, 0, 1],
                  [1, 0, 0],
                  [1, 1, 0]])
    print(pageRank(G, s=0.85))
