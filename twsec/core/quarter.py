# -*- coding: utf-8 -*-
"""This module will add MatLab header into after trading data of first day of every quarterly.

"""
__author__ = 'xero'
__email__ = "volleyp7689@gmail.com"

import os

# Path of After Trading Data
afd_path = os.path.join(os.path.curdir, "After_Trading_Data")

# month of every Quarterly
quarterly_month = ["01", "04", "07", "10"]


def get_quarter():
    """
    This Function will yield a quarter file from each year.
    """
    year_dirs = os.listdir(afd_path)
    year_dirs.sort(key=int)
    for year_dir in year_dirs:
        year_path = os.path.join(afd_path, year_dir)
        for month_dir in os.listdir(year_path):
            month_path = os.path.join(year_path, month_dir)
            if month_dir in quarterly_month:
                fn = os.listdir(month_path)[0]
                fp = os.path.join(month_path, fn)
                yield fp


def add_quarterly():
    """
    """
    # Find year and month of each quarterly.
    for year_dir in os.listdir(afd_path):
        year_path = os.path.join(afd_path, year_dir)
        for month_dir in os.listdir(year_path):
            month_path = os.path.join(year_path, month_dir)
            if month_dir in quarterly_month:
                fn = os.listdir(month_path)[0]
                fp = os.path.join(month_path, fn)
                year, month, day = fn.split(".")[0].split("_")
                year = int(year)
                year += 1911
                q = int(month_dir) / 3 + 1
                with open(fp, "r") as original_file:
                    data = original_file.read()
                with open(fp, "w+") as modified_file:
                    modified_file.write("{}Q{}".format(year, q) + data)
                print fp + "Done !"

    """Rewrite add quarter to first line
    gq = get_quarter()
    while True:
        fn, fp = gq.next()
        y, m, d = fn.split(".")[0].split("_")
        y = int(y)
        y += 1911
        q = int()
    """


def main():
    q = get_quarter()
    p = os.listdir(afd_path)
    p.sort(key=int)
    print p

    while True:
        raw_input("Press Enter to continue.")
        print("{}".format(q.next()))

if __name__ == "__main__":
    main()