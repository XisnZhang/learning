#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


def my_dropout(x, drop_prob):
    if drop_prob > 1.0 or drop_prob < 0.:
        raise ValueError("wrong dropout prob, must in [0,1]")

    # #以概率p随机生成1个0,1构成的向量，1出现的概率为p
    retain_prob = 1 - drop_prob
    sample = np.random.binomial(n=1, p=retain_prob, size=x.shape)

    # #以概率drop_prob使得某些神经元值输入变为0，即删除这些神经元
    x *= sample

    """
    训练阶段通过随机丢弃某些神经元训练不同的网络模型，那么在测试阶段，原则上，也需要随机丢弃某些神经元，
    但这样会导致模型不稳定，对于同一个测试数据,可能输出a也可能输出b; 因此，在实际应用中，会采用一种补偿
    方案， 即：给每个神经元的输入都乘以概率retain_prob， 使得在“总体上”，训练阶段和测试阶段是保持一致的；
    比如，对于输入x,在训练阶段，以概率1-retain_prob丢弃某些神经元，则最终期望是:
    retain_prob*x+ (1-retain_prob)*0=retain_prob*x, 测试阶段，直接乘以概率retain_prob， 即retain_prob*x，
    由此一来，就需要在测试阶段，加一次乘法操作，为减少推理耗时，在训练阶段完成此步骤，即如下rescale:
    """
    # #rescale操作
    x /= retain_prob
    return x


if __name__ == '__main__':
    in_x = np.array([1, 2, 3, 4, 5, 6])
    print(in_x)
    droped_x = my_dropout(in_x, 0.3)
    print(droped_x)
