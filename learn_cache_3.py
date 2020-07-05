#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
引入装饰器，增强版缓存装饰器
"""
import functools
import time

from my_lrucache import LRUCacheDict


def cache_it(max_size=1024, expiration=60):
    CACHE = LRUCacheDict(max_size=max_size, expiration=expiration)

    def wrapper(func):
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
    return wrapper


@cache_it(max_size=10, expiration=3)
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
    print('execute sql time 2: %.2fs' % (time.time() - start))
    print('sql result 2:', result)

    time.sleep(4)

    start = time.time()
    query('SELECT * FROM blog_post')
    print('-' * 100)
    print('execute sql time 3: %.2fs' % (time.time() - start))
    print('sql result 3:', result)

    start = time.time()
    query('SELECT * FROM blog_post')
    print('-' * 100)
    print('execute sql time 4: %.2fs' % (time.time() - start))
    print('sql result 4:', result)