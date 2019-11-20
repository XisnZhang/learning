#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import tensorflow as tf
import os

"""
1. tf.操作返回值都是tensor
2. name="specific_name"使得在tensorboard中更易查看
3. tf.summary.FileWriter 将sumaries写入event files，tensorboard从event files中加载内容并可视化
   tf.summary.FileWriter要记得close()
4. sess.run()用来指定需要运行的tensor,否则其对应的操作不会执行，递归执行，只要运行了最后的tensor,
   其涉及的所有tensor都会被计算,没涉及到的则不会被计算
"""
if __name__ == '__main__':
    tf.flags.DEFINE_string("log_dir", os.path.dirname(os.path.abspath(__file__)) + "/logs",
                           "log dir ")
    FLAGS = tf.flags.FLAGS
    log_dir = os.path.expanduser(FLAGS.log_dir)
    if not os.path.isabs(log_dir):
        raise ValueError("please input right log_dir")

    a = tf.constant(1., name="a")
    b = tf.constant(2., name="b")
    c = tf.add(a, b, name="add")
    d = tf.add(c, tf.div(a, b, name="div"), name="d")

    e = tf.constant(3., name="e")
    # e,f 不会被计算，会作为辅助graph出现在tensorboard中，作为一个独立的graph
    f = tf.add(a, e, name="f")
    with tf.Session() as sess:
        writer = tf.summary.FileWriter(log_dir, sess.graph)
        print("output:", sess.run([a, b, d]))
        writer.close()
