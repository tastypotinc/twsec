#! /usr/bin/python2
# -*- coding: utf-8 -*-
"""
"""
__author__ = "xero"
__email__ = "volleyp7689@gmail.com"

from settings.config import DECODE, ENCODE


def to_utf8(response):
    """
    Translate cp950 source response to utf
    """
    response_cp9 = response.decode(DECODE)
    response_utf8 = response_cp9.encode(ENCODE)
    return response_utf8