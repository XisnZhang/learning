#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import tensorflow as tf
import os

if __name__ == '__main__':
    tf.flags.DEFINE_string("log_dir", os.path.dirname(os.path.abspath(__file__)) + "/logs",
                           "dir of the tensorboard log")
    FLAGS = tf.flags.FLAGS
    log_dir = os.path.expanduser(FLAGS.log_dir)
    if not os.path.isabs(log_dir):
        raise ValueError("Please input right log_dir.")
    welcome = tf.constant("Hello, Tensorflow.", name="welcome")
    with tf.Session() as sess:
        writer = tf.summary.FileWriter(log_dir, sess.graph)
        print("output:", sess.run(welcome))
    writer.close()
