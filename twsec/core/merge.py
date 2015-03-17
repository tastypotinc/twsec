""" Merge After Trading Data based on each quarter

"""
from quarter import get_quarter

atd = open("atd.txt", "a")
gq = get_quarter()

while True:
    f = gq.next()
    with open(f, "r") as tmp_q:
        for line in tmp_q:
            atd.write(line)