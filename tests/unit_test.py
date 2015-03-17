#! /usr/bin/python2
# -*- coding: utf-8 -*-
"""For module unit testing.
"""
__author__ = "xero"
__email__ = "volleyp7689@gmail.com"

from crawl import crawl_stock_day_average
from twseDate import get_date_queue

dq = get_date_queue()

date = [("104", "03"), ("104", "02"), ("104", "01")]

stock_no = ['1101', '1102', '1103']  # Generate list from aft data?

"""
for stock in stock_no:
    month_queue = gen_month()
    while not month_queue.isEmpty():
        date = month_queue.get()
        data = crawl_stock_day_average()
        output(data)
"""