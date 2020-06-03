#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import log2


def count_entroy(dataset):
    """
    d[-1] 为label
    """
    label_counts = {}
    for d in dataset:
        l = d[-1]
        if l not in label_counts:
            label_counts[l] = 0
        label_counts[l] += 1
    total_count = len(dataset)
    entroy = 0
    for k, v in label_counts.items():
        p = v / total_count
        entroy += -p * log2(p)
    return entroy


def split_dataset_by_feature(dataset, feature):
    pass


if __name__ == '__main__':
    data = [[0, 0], [1, 1]]
    print(count_entroy(data))
