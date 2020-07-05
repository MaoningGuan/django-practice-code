#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

CACHE = {}


def query(sql):
    result = CACHE.get(sql)
    if not result:
        time.sleep(1)
        result = 'execute %s' % sql
        CACHE[sql] = result
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
