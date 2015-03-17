# -*- coding: utf-8 -*-
"""This is a TWSE After-Hour Trading data Crawler

"""
__author__ = 'xero'
__email__ = "volleyp7689@gmail.com"

# Standard Library
import os
import threading
import logging

# Custom Library
from core.gendate import get_date_queue
from core.crawl import crawl_bwibbu
from twsec.settings.config import DATA_DIR, NUM_OF_THREAD

date_queue = None
logger = logging.getLogger("__file__")


def main():
    # Initialize data directory
    if not os.path.isdir(DATA_DIR):
        os.mkdir(DATA_DIR)

    # Initialize date queue
    dq = get_date_queue()

    threads = []
    num_of_thread = NUM_OF_THREAD
    for i in range(num_of_thread):
        ct = threading.Thread(target=crawl_bwibbu(),
                              args=(dq,))
        threads.append(ct)
        ct.start()

if __name__ == "__main__":
    main()
