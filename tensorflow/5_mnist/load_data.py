#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import numpy as np
import collections


class MNIST_OBJECT(object):
    def __init__(self,
                 images,
                 labels,
                 ont_hot=False,
                 reshape=True):
        """
        :param images:[nums, width, height,channels]--> [nums,28,28,1]
        :param labels: [nums]
        :param ont_hot: 是否将label进行one-hot, 0-->[1,0,0,0,0,0,0,0,0,0]
        :param reshape: 是否转换为[nums,width*height]--> [nums,784]
        """
        num_class = 10
        assert images.shape[0] == labels.shape[0], (
                'images.shape: %s labels.shape: %s' % (images.shape, labels.shape))
        self._sample_exapmles = images.shape[0]

        if reshape:
            images = images.reshape(images.shape[0],
                                    images.shape[1] * images.shape[2])
        self._images = images
        self._labels = labels
        if ont_hot:
            index = np.arange(self._sample_exapmles) * num_class
            onehot_labels = np.zeros([self._sample_exapmles, num_class])
            onehot_labels.flat[index + labels.ravel()] = 1

            self._labels = onehot_labels

    @property
    def images(self):
        return self._images

    @property
    def labels(self):
        return self._labels

    @property
    def num_samples(self):
        return self._sample_exapmles


def fetch_data(mnist, reshape=True, one_hot=True):
    train_images = mnist.train.images
    train_labels = mnist.train.labels
    dev_images = mnist.validation.images
    dev_labels = mnist.validation.labels
    test_images = mnist.test.images
    test_labels = mnist.test.labels

    train = MNIST_OBJECT(train_images, train_labels, one_hot, reshape)
    dev = MNIST_OBJECT(dev_images, dev_labels, one_hot, reshape)
    test = MNIST_OBJECT(test_images, test_labels, one_hot, reshape)

    dataset = collections.namedtuple("DATASET", ["train", "dev", "test"])
    mnist_dataset = dataset(train=train, dev=dev, test=test)
    return mnist_dataset


def batch(images, labels, batchsize=100):
    assert images.shape[0] == labels.shape[0]
    sample_num = images.shape[0] // batchsize
    for ndx in range(0, sample_num, batchsize):
        yield images[ndx:min(ndx + batchsize, sample_num)], labels[ndx:min(ndx + batchsize, sample_num)]
