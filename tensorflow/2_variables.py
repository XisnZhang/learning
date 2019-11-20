#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
主要内容：变量， tf.Variable()
1. variables: hold on parameters, 对train,save,restore非常重要
2. 所有的变量必须初始化，然后才可以运行对应的operation
3. 变量的初始化方法： global, custom, inherited, restore
    * global: tf.global_variables_initializer(),一次初始化所有变量
    * customer: tf.variables_initializer(var_list=all_variables_list), 手动指定需要初始化哪些变量
              （虽然可以手动指定部分变量初始化，但最终所有参与计算的变量必须全部初始化）
    * inherited: tf.Variable(other_variable.initialized_value()),将其他变量(other_variable)的初始化值作为新变量的初始化值
      restore: 从ckpt中restore
4. 同一个变量，如果执行了多次初始化操作，在tensorboard中会显示多个init操作
"""
import tensorflow as tf
from tensorflow.python.framework import ops
import os

if __name__ == '__main__':
    tf.flags.DEFINE_string("log_dir", os.path.dirname(os.path.abspath(__file__)) + "/logs",
                           "log dir")
    FLAGS = tf.flags.FLAGS
    log_dir = os.path.expanduser(FLAGS.log_dir)
    if not os.path.isabs(log_dir):
        raise ValueError("please input right log_dir")

    weights = tf.Variable(tf.random_normal([2, 3], stddev=0.01), name="weights")
    # bias = tf.Variable(tf.zeros([3]), name="bias")
    # customer_variable = tf.Variable(tf.zeros([2]), name="customer")

    # 获取所有变量，并存储在一个列表中,只获取截至目前的所有变量，不包括后面的new_weights
    all_variable_list = ops.get_collection(ops.GraphKeys.GLOBAL_VARIABLES)
    # custom_init_variables_list = [weights, customer_variable]

    # #gloabl: 初始化所有变量
    # #方法1： global初始化,放在new_weigths定义前，不会初始化new_weights
    init_all_op = tf.global_variables_initializer()

    # #方法2： 手动初始化所有变量, 不会初始化new_weights
    # init_all_op = tf.variables_initializer(all_variable_list)

    # #custom: 手动初始化指定变量
    # customer_init_op = tf.variables_initializer(var_list=custom_init_variables_list)  # 手动初始化

    # #inheried: 用已有变量的初始化值初始化某个变量
    new_weights = tf.Variable(weights.initialized_value(), name="new_weights")
    init_new_weights_op = tf.variables_initializer([new_weights])

    with tf.Session() as sess:
        writer = tf.summary.FileWriter(log_dir, sess.graph)
        # sess.run(customer_init_op)
        # sess.run(init_new_weights_op)
        sess.run(init_all_op)
        sess.run(new_weights)
        print(all_variable_list)
