# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 20:34:12 2018

@author: haoqi
"""
from __future__ import print_function
import tensorflow as tf
import keras
from keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()