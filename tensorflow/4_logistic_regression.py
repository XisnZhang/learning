#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os


def logisitic_regression():
    tf.flags.DEFINE_string("log_dir", os.path.dirname(os.path.abspath(__file__)) + "/logs",
                           "log dir")
    FLAGS = tf.flags.FLAGS
    log_dir = os.path.expanduser(FLAGS.log_dir)
    if not os.path.isabs(log_dir):
        raise ValueError("please input right log dir.")
    if os.path.exists(log_dir):
        for file in os.listdir(log_dir):
            os.remove(os.path.join(log_dir, file))
    # #构建训练数据
    data_X = np.random.randn(50, 2).astype(np.float32)
    data_Y = np.where((data_X[:, 1] - data_X[:, 0]) > 0, 1, 0).reshape(50, 1)
    # pos = np.where(data_Y == 1)
    # neg = np.where(data_Y == 0)
    # plt.plot(data_X[pos, 0], data_X[pos, 1], "k+")
    # plt.plot(data_X[neg, 0], data_X[neg, 1], "ko")
    # plt.plot([-2, 2], [-2, 2])

    # #占位符
    X = tf.placeholder(tf.float32, [None, 2], name="X")  # 二维空间上的点，即两维特征
    Y = tf.placeholder(tf.float32, [None, 1], name="Y")

    # #变量及模型
    W = tf.Variable([[1], [1]], name="W", dtype=tf.float32)
    b = tf.Variable([0.0], name="b", dtype=tf.float32)
    Y_predicted = tf.sigmoid(tf.matmul(X, W) + b)

    # #loss和参数更新
    train_loss = tf.reduce_mean(-Y * tf.log(Y_predicted) - (1 - Y) * tf.log(1 - Y_predicted))  # 一个batch的loss求均值
    train_acc = tf.reduce_mean(tf.cast(tf.equal(Y, tf.cast((Y_predicted > 0.5), tf.float32)), tf.float32))

    # # tensorboard画图内容
    tf.summary.scalar("train_loss", train_loss)
    tf.summary.scalar("train_acc", train_acc)
    train_op = tf.train.GradientDescentOptimizer(0.01).minimize(train_loss)
    train_summary = tf.summary.merge_all()

    # #全部变量初始化
    init_op = tf.global_variables_initializer()
    with tf.Session() as sess:
        writer = tf.summary.FileWriter(log_dir, sess.graph)
        sess.run(init_op)
        for i in range(1000):
            # #一个iter更新所有所有数据
            predict, train_w, train_b, merge_summary, loss, acc, _ = sess.run(
                [Y_predicted, W, b, train_summary, train_loss, train_acc, train_op],
                feed_dict={X: data_X, Y: data_Y})
            print("epoch: {:d}, loss: {:f}, acc: {:f}".format(i, loss, acc))
            # print(train_w, train_b)
            # print(predict)

            writer.add_summary(merge_summary, i)
    # plt.show()


if __name__ == '__main__':
    logisitic_regression()
