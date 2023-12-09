import sys
sys.path.append("../..")

import numpy as np
import itertools
from lib.utils import dl_lines, dl_blockoflines_str, dl_blockoflines
import re



dl_method = dl_lines


data = dl_method("input.txt")
# data = dl_method("sample.txt")
# data = dl_method("sample_2.txt")
# data = dl_method("sample_3.txt")

data = [[ int(_d) for _d in d.split(" ")] for d in data]
print(data)

sum_last_item = 0
last_item = []
previous_item = []
for ls, serie in enumerate(data):
    pyr = [serie]
    n=0
    while False in [p == 0 for p in pyr[-1]]: #nd n < 10:
        s = pyr[-1]
        pyr.append([ s[i+1] - s[i] for i in range(len(s[:-1]))])
        n+=1
    pyr.reverse() #reversed(pyr)
    for p in pyr: 
        print(p)
    pyr2 = pyr # quitae straightforward
    for ip in range(len(pyr) - 1):
        pyr[ip+1].append(pyr[ip][-1] + pyr[ip+1][-1])
        pyr2[ip+1].insert(0, pyr2[ip+1][0] - pyr2[ip][0])
    sum_last_item += pyr[-1][-1]
    last_item.append(pyr[-1][-1])
    previous_item.append(pyr2[-1][0])
    for p in pyr2:
        print(p)
    print()
print(last_item)
print("part1:", sum(last_item))

print(previous_item)
print("part2:", sum(previous_item))

# solved in ~45'
