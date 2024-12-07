import sys
sys.path.append("../..")

import numpy as np
import itertools

from lib.utils import dl_lines

dl_method = dl_lines
data = dl_method("input.txt")

cc = [ 
    l.split("   ")
    for l in data
]
print(cc[:10])
l1 = [int(c[0]) for c in cc]
l2 = [int(c[1]) for c in cc]

l1 = sorted(l1)

l2 = sorted(l2)


sum = 0
for (x, y) in zip(l1, l2):
    d = abs(x-y)
    sum += d

print(sum)


sum_2 = 0
for x1 in l1:
    x2 = l2.count(x1)
    sum_2 += x1*x2

print(sum_2)


# 14 minutes. Pretty straight forward but lazy code
