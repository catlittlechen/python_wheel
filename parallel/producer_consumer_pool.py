#!/usr/bin/env python
# encoding: utf-8

import time
import threading
import Queue
import urllib2


class Consumer(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            msg = self._queue.get()
            if isinstance(msg, str) and msg == 'quit':
                break
            urllib2.urlopen(msg)
            print "I'm a thread, and I received %s" % msg
        print "Bye byes!"


class ConsumerPool():

    def __init__(self, queue, size):
        self.workers = []
        self.queue = queue
        for _ in xrange(size):
            worker = Consumer(queue)
            worker.start()
            self.workers.append(worker)

    def close(self):
        for worker in self.workers:
            self.queue.put('quit')

        for worker in self.workers:
            worker.join()


def Produce():

    urls = [
        'http://www.python.org', 'http://www.qq.com',
        'http://www.baidu.com', 'http://www.taobao.com'
    ]

    queue = Queue.Queue()
    worker_pool = ConsumerPool(queue, 4)

    for url in urls:
        queue.put(url)
        time.sleep(1)

    worker_pool.close()

if __name__ == "__main__":
    Produce()
