#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
引入装饰器，增加缓存器的通用性
"""
import functools
import time

CACHE = {}


def cache_it(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        key = repr(*args, **kwargs)
        try:
            result = CACHE[key]
        except KeyError:
            result = func(*args, *kwargs)
            CACHE[key] = result
        return result

    return inner


@cache_it
def query(sql):
    time.sleep(1)
    result = 'execute %s' % sql
    return result


if __name__ == '__main__':
    start = time.time()
    result = query('SELECT * FROM blog_post')
    print('execute sql time: %.2fs' % (time.time() - start))
    print('sql result 1:', result)

    start = time.time()
    query('SELECT * FROM blog_post')
    print('-' * 100)
    print('execute sql time: %.2fs' % (time.time() - start))
    print('sql result 2:', result)
