#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# path1 = os.path.abspath(__file__)
# path2 = os.path.dirname(path1)
# path3 = os.path.dirname(path2)
#
# print(path1)
# print(path2)
# print(path3)
# coding:utf-8


class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):
        return cls.averag(cls.X, cls.Y)


class Son(Foo):
    X = 3
    Y = 5

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / 3

p = Son()
print(p.static_method())
print(p.class_method())
# 1.5
# 2.6666666666666665