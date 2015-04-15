# -*- coding: utf-8 -*-
"""Roc Date Generator

"""
__author__ = 'xero'
__email__ = "volleyp7689@gmail.com"

import datetime
import threading
import Queue

'''
class TwseDateGenerator(object):
    """Generator for date in TWSE Format.
    """
    def __init__(self, roc_year=None, month=None, day=None):
        self.roc_year = roc_year
        self.month = month
        self.day = day

    def year(self):
        """
        :return: Transform Roc year to B.C year.
        """
        return str(1911 + self.roc_year)

    def gen_month(self):
        """
        :return:
        """

    def gen_day(self):
        pass
'''


def gen_year(roc_year):
    """
    :return: Transform Roc year to B.C year.
    """
    return str(1911 + roc_year)


def gen_month(month):
    """
    :return:
    """
    if month < 10:
        return "0" + str(month)
    else:
        return str(month)


def gen_day(day):
    """
    :return:
    """
    if day < 10:
        return "0" + str(day)
    else:
        return str(day)


def get_date_queue(end):
    """ Using date generator to fill the date queue """
    dg = gen_date_from_now_to(end)
    dq = Queue.Queue()
    while True:
        date = dg.next()
        if date is not None:
            dq.put(date)
        else:
            return dq


def gen_date_from_now_to(end):
    """ This function will generate date in the format of roc.Y/M/D from now to ROC year 94.
    """
    c_date = datetime.datetime.today()
    lock = threading.Lock()
    while True:
        lock.acquire()
        try:
            year = c_date.year-1911
            month = gen_month(c_date.month)
            day = gen_day(c_date.day)
            o_date = "{}/{}/{}".format(year, month, day)  # 1911 = change AD to ROC year.

            yield o_date

            # The oldest data of Taiwan Exchanger is 94/07/01,
            if o_date == end:
                yield None
                break
            c_date = c_date - datetime.timedelta(days=1)
        finally:
            lock.release()


if __name__ == "__main__":
    q = get_date_queue("94/07/01")
    print q.get()