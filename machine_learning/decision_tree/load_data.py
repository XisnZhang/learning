#!/usr/bin/env python
# -*- coding: utf-8 -*-
def load_data(filename):
    with open(filename, "r") as f:
        data = f.readlines()[1:]
        data = [d.strip("\n").split(",") for d in data]
        return data


if __name__ == '__main__':
    train_file = "./train.txt"
    test_file = "./test.txt"
    train_data = load_data(train_file)
    print(train_data)
    test_data = load_data(test_file)
    print(test_data)
