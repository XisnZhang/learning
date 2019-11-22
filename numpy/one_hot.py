#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy  as np


def one_hot(a, num_classes):
    index = np.arange(a.shape[0]) * num_classes
    one_hot = np.zeros([a.shape[0], num_classes])
    one_hot.flat[index + a.ravel() - 1] = 1
    return one_hot


if __name__ == '__main__':
    a = np.array([1, 2, 1, 3, 4])
    num_classes = 4
    print(one_hot(a, num_classes))
