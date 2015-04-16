# -*- coding: utf-8 -*-
"""This is a TWSE After-Hour Trading data Crawler

"""
__author__ = 'xero'
__email__ = "volleyp7689@gmail.com"

# Standard Library
import os
import threading
import logging
import sys
sys.path.append(os.path.abspath('..'))  # import package path

# Custom Library
from core.gendate import get_date_queue, gen_year, gen_month
from core.crawl import bwibbu, stock_day_average
from core.directory import check_stock_day_avg_dir
from twsec.settings.config import NUM_OF_THREAD


date_queue = None
logger = logging.getLogger("__file__")


def crawl_after_trading_data():
    # Initialize data directory
    #if not os.path.isdir(DATA_DIR):
    #   os.mkdir(DATA_DIR)

    # Initialize date queue
    dq = get_date_queue()

    threads = []
    num_of_thread = NUM_OF_THREAD
    for i in range(num_of_thread):
        ct = threading.Thread(target=bwibbu(),
                              args=(dq,))
        threads.append(ct)
        ct.start()


def crawl_stock_day_avg(stock_no):

    """Move this time function to independent file!!"""
    import datetime
    now = datetime.datetime.now()
    yl = [str(y) for y in range(1999, now.year+1)]
    ml = []
    for m in range(1, 13):
        if m < 10:
            ml.append("0" + str(m))
        else:
            ml.append(str(m))

    sl = []
    for y in yl:
        for m in ml:
            sl.append(stock_day_average(stock_no, y, m))


def crawl_stock_day():
    stk_no_list = [no for no in range(1101, 1111)]  # Cement Stock
    for stkno in stk_no_list:
        stkno_dir = check_stock_day_avg_dir(stkno)
        for y in range(88, 105):
            data_list = []
            year = gen_year(y)
            for m in range(1, 13):
                output_single_month = ""
                if y == 105 and m > 4:
                    continue
                month = gen_month(m)
                sda = stock_day_average(stkno, year, month)
                print sda
                for data in sda:
                    date = data[0]
                    price = data[1]
                    output_single_month = output_single_month + "{}\t{}\n".format(date, price)
                fn = (os.path.join(stkno_dir, year + "_" + month + ".txt"))
                with open(fn, "w+") as f:
                    f.write(output_single_month)
                data_list.append(data)


if __name__ == "__main__":
    crawl_stock_day()