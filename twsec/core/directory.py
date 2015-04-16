#! /usr/bin/python2
# -*- coding: utf-8 -*-
"""
"""
__author__ = "xero"
__email__ = "volleyp7689@gmail.com"

import os

PROJECT_DIR = os.path.abspath("..")
DATA_DIR = os.path.join(PROJECT_DIR, "data")

STOCK_DAY_AVG_DIR = os.path.join(DATA_DIR, "stock_day_avg")
BWIBBU_DIR = os.path.join(DATA_DIR, "bwibbu")


def check_stock_day_avg_dir(stkno, data_dir=STOCK_DAY_AVG_DIR):
    """
    :param data_dir: path to data directory
    :param stkno: stock id
    :return: path of directory of stock id
    """
    stkno_dir = os.path.join(data_dir, str(stkno))
    if not os.path.isdir(stkno_dir):
        os.makedirs(stkno_dir)
    return stkno_dir


def check_bwibbu_dir(fnl, data_dir=BWIBBU_DIR):
    """
        Year: fnl[0]
        Month: fnl[1]
        Day: fnl[2]
        """
    year_dir = os.path.join(data_dir, fnl[0])
    month_dir = os.path.join(year_dir, fnl[1])

    if not os.path.isdir(year_dir):
        os.mkdir(year_dir)

    if not os.path.isdir(month_dir):
        os.mkdir(month_dir)
    return month_dir

if __name__ == "__main__":
    check_stock_day_avg_dir(1101)