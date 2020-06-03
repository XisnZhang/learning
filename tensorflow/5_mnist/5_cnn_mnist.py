#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import random
# #通过导入ssl模块把证书验证改成不用验证就行了,避免证书验证不通过而无法下载
import ssl
from load_data import fetch_data, batch
import os

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    logdir = "/home/cloud/logs/tensorflow-logs/" + os.path.basename(__file__).split(".")[0]
    if os.path.exists(logdir):
        for file in os.listdir(logdir):
            os.remove(os.path.join(logdir, file))
            
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.8)
    mnist = input_data.read_data_sets("/home/cloud/datas/datasets/cv/MNIST_data ", reshape=False, one_hot=False)
    data = fetch_data(mnist, reshape=False, one_hot=True)

    train_images = data.train.images
    train_labels = data.train.labels
    index = list(range(train_images.shape[0]))
    random.shuffle(index)
    train_images = train_images[index]
    train_labels = train_labels[index]

    print(data.train.images.shape, data.train.labels.shape)
    print(data.dev.images.shape, data.dev.labels.shape)
    print(data.test.images.shape, data.test.labels.shape)

    # # placeholder
    X = tf.placeholder(tf.float32, [None, 28, 28, 1], name="X")
    Y = tf.placeholder(tf.float32, [None, 10], name='Y')

    """model 卷积1+max pooling1 +卷积2+max pooling2+softmax"""
    # #第一层卷积
    # #conv2d的filters:4维矩阵， [filter_height, filter_width, in_channels, out_channels]
    # #初始化时如果stddev设置为默认值1，则会出现参数为nan的情况
    filter1 = tf.Variable(tf.truncated_normal([5, 5, 1, 32], stddev=0.1), name="filter1")
    bias1 = tf.Variable(tf.cast(tf.fill([32], 0.1), tf.float32), name="bias1")
    conv1 = tf.nn.conv2d(X, filter1, strides=[1, 1, 1, 1], padding="SAME", name="conv1")
    h_conv1 = tf.nn.relu(conv1 + bias1)
    max_pool_1 = tf.nn.max_pool(h_conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # #第二层卷积
    filter2 = tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1), name="filter2")
    bias2 = tf.Variable(tf.cast(tf.fill([64], 0.1), tf.float32), name="bias2")
    conv2 = tf.nn.conv2d(max_pool_1, filter2, strides=[1, 1, 1, 1], padding="SAME", name="conv2")
    h_conv2 = tf.nn.relu(conv2 + bias2)
    max_pool_2 = tf.nn.max_pool(h_conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # # feedforward
    ffn_w = tf.Variable(tf.truncated_normal([7 * 7 * 64, 1024], stddev=0.1), name="ffn1_w")
    ffn_b = tf.Variable(tf.cast(tf.fill([1024], 0.1), tf.float32), name="ffn1_b")
    max_pool_2_flat = tf.reshape(max_pool_2, [-1, 7 * 7 * 64])
    fnn_h = tf.nn.relu(tf.matmul(max_pool_2_flat, ffn_w) + ffn_b)

    # # softmax
    ffn2_w = tf.Variable(tf.truncated_normal([1024, 10], stddev=0.1), name="ffn2_w")
    ffn2_b = tf.Variable(tf.cast(tf.fill([10], 0.1), tf.float32), name="ffn2_b")
    y_ = tf.nn.softmax(tf.matmul(fnn_h, ffn2_w) + ffn2_b)

    loss = -tf.reduce_sum(Y * tf.log(y_))
    acc = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(Y, 1), tf.argmax(y_, 1)), tf.float32))
    train_op = tf.train.AdamOptimizer(1e-4).minimize(loss)

    with tf.Session(config=tf.ConfigProto(gpu_options=gpu_options)) as sess:
        writer = tf.summary.FileWriter(logdir, sess.graph)
        sess.run(tf.global_variables_initializer())
        for i in range(2000):
            for batch_images, batch_labels in batch(train_images, train_labels, batchsize=100):
                filter1_, bias1_, loss_, acc_, _ = sess.run(
                    [filter1, bias1, loss, acc, train_op], feed_dict={X: batch_images, Y: batch_labels})
            print("epoch: {:d}, loss: {:f}, acc: {:f}".format(i, loss_, acc_, train_op))
        test_acc = sess.run([acc], feed_dict={X: data.test.images, Y: data.test.labels})
        print(test_acc)
    writer.close()


if __name__ == '__main__':
    main()
