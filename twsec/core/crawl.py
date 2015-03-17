#! /usr/bin/python2
# -*- coding: utf-8 -*-
"""
"""
__author__ = "xero"
__email__ = "volleyp7689@gmail.com"

import os
import re
import time
import random
import threading

from twsec.settings.config import ENCODE, DECODE, DATA_DIR, FILE_EXTENSION
from twsec.settings.config import ENCODE
import directory
import connect
import code


def crawl_stock_day_average(stk_no, myear, mmon):
    """
    Generator of stock_day_average data
    """
    info_flag = 'STOCK_DAY_AVG'
    try:
        """ URL """
        referer_url = "http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAY.php"
        par = {'STK_NO': stk_no, 'myear': myear, 'mmon': mmon}
        gen_url = connect.twse_gen_url(referer_url, par)
        response = connect.get_request(gen_url, info_flag)

        """ """
        response = code.to_utf8(response)

        with open("sda.html", "w") as f:
            for line in response:
                f.write(line)

        pattern_tr = "<tr bgcolor='#FFFFFF' class='basic2'>(.*?)</tr>"
        pattern_data = '<.*?><.*?>(.*?)<.*?><.*?>'
        tr = re.findall(pattern_tr, response, re.DOTALL)

        if not tr:
            return

        sda = {}
        for item in tr:
            data = re.findall(pattern_data, item, re.DOTALL)
            sda[data[0]] = data[1]

        print sda
        return sda

    except StopIteration as se:
        print(se.message)


def crawl_bwibbu(date_queue):
    """ Crawling Thread
    """
    while not date_queue.empty():
        try:
            # Get item from date queue
            date = date_queue.get()

            # Check dir and Open file
            fnl = date.split("/")
            f_dir = directory.check_dir(DATA_DIR, fnl)  # Path of Dir
            n = "_".join(fnl) + FILE_EXTENSION  # File name
            fn = os.path.join(f_dir, n)
            if os.path.isfile(fn):
                print "File exists"
                continue
            # logging.info(fn)

            # Connect to http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU_d.php
            url = 'http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU_d.php'
            par = {'input_date': date}
            the_page = connect.post_request(url, par)

            # Convert source page to utf-8
            src_cp9 = the_page.decode(DECODE)
            src_utf8 = src_cp9.encode(ENCODE)

            # Locate target html tag
            pattern_tb1 = '<tr bgcolor=#FFFFFF>(.*?)</tr>'
            pattern_data = '<.*?>(.*?)<.*?>'
            tb1 = re.findall(pattern_tb1, src_utf8, re.DOTALL)
            if not tb1:
                continue

            # Open file
            while True:
                try:
                    f = open(fn, "w+")
                    break
                except IOError as err:
                    print err.message
                    time.sleep(random.random()*10)
                    continue

            # Write to file
            for security in tb1:
                data = re.findall(pattern_data, security, re.DOTALL)
                for item in data:
                    f.write('%s\t' % item)
                f.write("\n")
            f.close()
            print threading.currentThread().getName() + ": " + fn + " is Done!"
        except StopIteration as se:
            print(se.message)
            continue
    print threading.currentThread() + " is done!"


def unit_test():
    c = crawl_stock_day_average("1101", "2014", "03")

if __name__ == "__main__":
    unit_test()