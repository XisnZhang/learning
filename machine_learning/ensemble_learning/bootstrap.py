#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def bootstrap(samples):
    """
    有放回地随机选择
    """
    length = len(samples)
    result = []
    for _ in range(length):
        result.append(random.choice(samples))
    return result


if __name__ == '__main__':
    samples = [1, 2, 3, 4, 5]
    print(bootstrap(samples))  # [5, 2, 5, 2, 2]
    print(bootstrap(samples))  # [3, 1, 3, 5, 3]
