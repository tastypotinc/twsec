# -*- coding: utf-8 -*-
"""Roc Date Generator

"""
__author__ = 'xero'
__email__ = "volleyp7689@gmail.com"

import datetime
import threading
import Queue


def get_date_queue():
    """ Using date generator to fill the date queue """
    dg = gen_date()
    dq = Queue.Queue()
    while True:
        date = dg.next()
        if date is not None:
            dq.put(date)
        else:
            return dq


def gen_date():
    """ This function will generate date in the format of roc.Y/M/D from now to ROC year 94.
    """
    c_date = datetime.datetime.today()
    lock = threading.Lock()
    while True:
        lock.acquire()
        try:
            year = c_date.year-1911

            if c_date.month < 10:
                month = "0" + str(c_date.month)
            else:
                month = c_date.month

            if c_date.day < 10:
                day = "0" + str(c_date.day)
            else:
                day = c_date.day

            o_date = "{}/{}/{}".format(year, month, day)  # 1911 = change AD to ROC year.

            yield o_date

            # The oldest data of Taiwan Exchanger is 94/07/01,
            if o_date == "94/07/01":
                yield None
                break

            c_date = c_date - datetime.timedelta(days=1)
        finally:
            lock.release()


def gen_year():
    pass


def gen_month():
    pass

if __name__ == "__main__":
    g = gen_date()
    while True:
        raw_input()
        print g.next()