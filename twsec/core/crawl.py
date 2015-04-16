#! /usr/bin/python2
# -*- coding: utf-8 -*-
"""

"""
__author__ = "xero"
__email__ = "volleyp7689@gmail.com"

import os
import re
import abc

import sys
sys.path.append(os.path.abspath('..'))

import connect
import code


class TWSEParser(object):
    """
    """
    def __init__(self):
        try:
            self.response = code.to_utf8(self.get_http_response())
        except StopIteration as si:
            print si.message

    @abc.abstractmethod
    def get_http_response(self):
        """Method to get http response,"""

    @abc.abstractmethod
    def parse_http_tag(self):
        """Method to parse data inside http tags."""


def stock_day_average(stk_no, myear, mmon):
    """
    Generator of stock_day_average data
    個股日收盤價
    """
    info_flag = 'STOCK_DAY_AVG'
    try:
        """ URL """
        refer_url = "http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAY.php"
        par = {'STK_NO': stk_no, 'myear': myear, 'mmon': mmon}
        gen_url = connect.twse_gen_url(refer_url, par)
        response = connect.get_request(gen_url, info_flag)

        response = code.to_utf8(response)

        pattern_tr = "<tr bgcolor='#FFFFFF' class='basic2'>(.*?)</tr>"
        pattern_data = '<.*?><.*?>(.*?)<.*?><.*?>'
        tr = re.findall(pattern_tr, response, re.DOTALL)

        if not tr:
            return

        result = []
        for item in tr:
            data = re.findall(pattern_data, item, re.DOTALL)
            result.append([data[0], data[1]])

        return result[:-1]  # We don't need month average data.

    except StopIteration as se:
        print(se.message)


def bwibbu(date):
    """Crawl Data from bwibbu in one date.
    :param date:
    :return:
    """
    try:
        # Connect to http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU_d.php
        url = 'http://www.twse.com.tw/ch/trading/exchange/BWIBBU/BWIBBU_d.php'
        par = {'input_date': date}
        response = connect.post_request(url, par)

        response = code.to_utf8(response)

        # Locate target html tag
        pattern_tb1 = '<tr bgcolor=#FFFFFF>(.*?)</tr>'
        pattern_data = '<.*?>(.*?)<.*?>'
        tb1 = re.findall(pattern_tb1, response, re.DOTALL)

        if not tb1:
            return

        result = []
        for security in tb1:
            data = re.findall(pattern_data, security, re.DOTALL)
            result.append(data)

        return result

    except StopIteration as se:
        print(se.message)


if __name__ == "__main__":
    print stock_day_average("1101", "2014", "04")
    print bwibbu("97/07/02")
