# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import logging
import time
import os

from multiprocessing import Process


def run(function, data, max_tasks):
    logging.debug('Runner started with pid=%s' % os.getpid())

    start_time = time.time()
    logging.info('start time = %s' % start_time)
    if max_tasks > 0:
        for item in data:
            tasks = []

            for ind in range(0, max_tasks):
                logging.debug('Process put to execution query')
                process = Process(target=function, args=(item))
                tasks.append(process)

            for task in tasks:
                task.start()

            for task in tasks:
                task.join()

    logging.info('end time = %s' % time.time())
    logging.info('execution time = %s' % str((time.time() - start_time) / 60))
