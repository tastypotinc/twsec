#! /usr/bin/python2
# -*- coding: utf-8 -*-
"""
"""
__author__ = "xero"
__email__ = "volleyp7689@gmail.com"

import os


def check_dir(data_dir, fnl):
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