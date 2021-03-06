#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
利用tensorflow搭建linear regression model
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os


def linear_regression():
    tf.flags.DEFINE_string("log_dir", "/home/cloud/logs/tensorflow-logs/" + os.path.basename(__file__).split(".")[0],
                           "log dir")
    tf.flags.DEFINE_integer("epoch", 100,
                            "# of train epoch")
    tf.flags.DEFINE_float("lr", 0.001,
                          "learning rate")
    FLAGS = tf.flags.FLAGS
    log_dir = os.path.expanduser(FLAGS.log_dir)
    if not os.path.isabs(log_dir):
        raise ValueError("please input right log dir.")

    # #构造训练数据
    train_X = np.linspace(-1, 1, 100)
    # print(train_X.shape)  # # (100,)
    # print(*train_X.shape)  # # 100
    train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.5 + 10

    # #输入输出
    X = tf.placeholder(tf.float32, name="X")
    Y = tf.placeholder(tf.float32, name="Y")

    # #参数
    w = tf.Variable(initial_value=0.5, name="w")
    b = tf.Variable(initial_value=0.0, name="b")

    # #build graph,loss
    Y_predicted = X * w + b
    train_loss = tf.squared_difference(Y, Y_predicted)
    tf.summary.scalar('train_loss', train_loss)
    tf.summary.scalar('train_loss_2', train_loss)  # test
    merge_summary = tf.summary.merge_all()
    # #更新参数，更新方向是最小化train_loss
    train_op = tf.train.GradientDescentOptimizer(FLAGS.lr).minimize(train_loss)  # #随机梯度优化器
    # train_op = tf.train.AdamOptimizer(FLAGS.lr).minimize(train_loss)  # #Adam优化器
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        writer = tf.summary.FileWriter(log_dir, sess.graph)
        sess.run(init)
        for epoch in range(FLAGS.epoch):
            for x, y in zip(train_X, train_Y):
                # #逐个example计算loss,更新参数
                train_summary, loss, _ = sess.run([merge_summary, train_loss, train_op], feed_dict={X: x, Y: y})

                # #一个epoch全部训练完后的w, b, loss
            wcoeff, bias = sess.run([w, b])
            print("epoch: {:d}, loss: {:f}, w: {:f}, b: {:f}".format(epoch, loss, wcoeff, bias))
            writer.add_summary(train_summary, epoch)
    plt.plot(train_X, train_Y, "*")
    plt.plot(train_X, wcoeff * train_X + bias)
    plt.show()
    writer.close()


def linear_regression_2():
    # 使用 NumPy 生成假数据(phony data), 总共 100 个点.
    x_data = np.float32(np.random.rand(2, 100))  # 随机输入,2*100维的0-1间的随机数
    y_data = np.dot([0.100, 0.200], x_data) + 0.300

    # # 构造一个线性模型
    # #
    b = tf.Variable(tf.zeros([1]))
    W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))  # 维度1*2, 值介于-1.0到1.0，是均匀分布的
    y = tf.matmul(W, x_data) + b
    #
    # 最小化方差
    loss = tf.reduce_mean(tf.square(y - y_data))  # mse
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(loss)
    #
    # 初始化变量
    init = tf.initialize_all_variables()
    #
    # 启动图 (graph)
    sess = tf.Session()
    sess.run(init)
    #
    # 拟合平面
    for step in range(0, 201):
        sess.run(train)
        if step % 20 == 0:
            _loss, _w, _b = sess.run([loss, W, b])
            print(step, _loss, _w, _b)

    # 得到最佳拟合结果 W: [[0.100  0.200]], b: [0.300]
    sess.close()


if __name__ == '__main__':
    linear_regression_2()
