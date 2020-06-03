#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# @Time : 20-1-19 下午6:28 
# @Author : shixi 
# @Site : shixi.zhang@cloudminds.com 
# @File : concat.py 
import tensorflow as tf

tf.compat.v1.disable_eager_execution()
if __name__ == '__main__':
    a = tf.constant([[1, 2, 3], [4, 5, 6]])
    b = tf.constant([[5, 6, 7], [7, 8, 9]])
    c = tf.concat([a, b], 0)
    d = tf.split(a, 2, 0)
    with tf.compat.v1.Session() as sess:
        print(sess.run([c, d]))
