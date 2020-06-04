#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
问题定义：
固定长度缓冲区读写：有一个日志缓冲区，最多只能存储100条日志，当超过100条时，新增的日志将覆盖旧的日志
"""


class solution:
    """
        空间限制，不能用append，开辟新的空间？？
        采用环形队列
    """

    def __init__(self, cache_size=100):
        self.cache_size = cache_size
        self.cache = [-1] * cache_size
        self.last_index = -1

    def write_log(self, log):
        if self.last_index < self.cache_size - 1:
            self.last_index += 1
        else:  # 直接替换第一个位置处的log,依次往后写
            self.last_index = 0
        self.cache[self.last_index] = log
        print(self.cache)

    def write_log_2(self, log):
        """
        采用取模的一致性处理，不需要每次判断是否已经到了队尾
        :param log:
        :return:
        """
        idx = (self.last_index + 1) % self.cache_size
        self.cache[idx] = log
        self.last_index += 1
        print(self.cache)


if __name__ == '__main__':
    logs = range(120)
    slu = solution(cache_size=100)
    for i in logs:
        slu.write_log_2(i)
