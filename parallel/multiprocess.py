#!/usr/bin/env python
# encoding: utf-8

import urllib2
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.python.org', 'http://www.qq.com',
    'http://www.baidu.com', 'http://www.taobao.com'
]

pool = ThreadPool(4)

results = pool.map(urllib2.urlopen, urls)
pool.close()
pool.join()

print len(results)
