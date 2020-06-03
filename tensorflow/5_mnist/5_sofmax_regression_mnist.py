#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
from load_data import fetch_data
# #通过导入ssl模块把证书验证改成不用验证就行了,避免证书验证不通过而无法下载
import ssl
import os
import random
import numpy as np
from load_data import fetch_data, batch

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    logdir = "/home/cloud/logs/tensorflow-logs/" + os.path.basename(__file__).split(".")[0]
    mnist = input_data.read_data_sets("/home/cloud/datas/datasets/cv/MNIST_data ", reshape=False, one_hot=False)
    data = fetch_data(mnist, reshape=True, one_hot=True)
    if os.path.exists(logdir):
        for file in os.listdir(logdir):
            os.remove(os.path.join(logdir, file))
    train_images = data.train.images
    train_labels = data.train.labels
    # index = list(range(train_images.shape[0]))
    # random.shuffle(index)
    # train_images = train_images[index]
    # train_labels = train_labels[index]

    print(data.train.images.shape, data.train.labels.shape)
    print(data.dev.images.shape, data.dev.labels.shape)
    print(data.test.images.shape, data.test.labels.shape)

    # # placeholder
    X = tf.placeholder(tf.float32, [None, 784], name="X")
    Y = tf.placeholder(tf.float32, [None, 10], name="Y")

    # #model
    W = tf.Variable(tf.zeros([784, 10]), name="W")
    b = tf.Variable(tf.zeros([10]), name="b")
    y_ = tf.nn.softmax(tf.matmul(X, W) + b)

    # #交叉熵， -sum(y_real*log(y_predict))
    loss = -tf.reduce_sum(Y * tf.log(y_))
    optimizer = tf.train.GradientDescentOptimizer(0.001)
    train_op = optimizer.minimize(loss)

    # #tensorboard记录的一些值
    acc = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(Y, 1), tf.argmax(y_, 1)), tf.float32))
    tf.summary.scalar("acc", acc, collections=["train", "test"])
    init = tf.global_variables_initializer()

    summary_train = tf.summary.merge_all("train")
    summary_test = tf.summary.merge_all("test")
    with tf.Session() as sess:
        writer = tf.summary.FileWriter(logdir, sess.graph)
        sess.run(init)
        for i in range(1000):
            for batch_images, batch_labels in batch(train_images, train_labels, batchsize=100):
                summary_train_, summary_test_, loss_, acc_, _ = sess.run(
                    [summary_train, summary_test, loss, acc, train_op],
                    feed_dict={X: batch_images, Y: batch_labels})
            print("epoch: {:d}, loss: {:f}, acc: {:f}".format(i, loss_, acc_, train_op))
            writer.add_summary(summary_train_, i)
            writer.add_summary(summary_test_, i)
        test_acc = sess.run([acc], feed_dict={X: data.test.images, Y: data.test.labels})
        print(test_acc)
        writer.close()


if __name__ == '__main__':
    main()
