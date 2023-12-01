import sys
sys.path.append("../..")

import numpy as np
import itertools


from lib.utils import dl_lines


dl_method = dl_lines
# dl_method = dl_blockoflines_str
# dl_method = dl_blockoflines_list


# data = dl_method("sample.txt")
# data = dl_method("sample_2.txt")
data = dl_method("input.txt")

# pathetic-but-working data parsing
conv = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1", # <- I added this when I panicked
    "2": "2", # ...
    "3": "3", # ...
    "4": "4", # ...
    "5": "5", # ...
    "6": "6", # ...
    "7": "7", # ...
    "8": "8", # ...
    "9": "9", # please don't judge me
}

def conv_s(s):
    so = s
    ls = []
    for k, v in conv.items():
        p = 0
        so = s
        while p != -1:
            p = so.find(k) # find the number "one" "two" etc. in the str 
            if p > -1:
                so = so[:p] +"".join(["_" for c in range(len(k))])+ so[p+len(k):] # <- this line is tragic but it helps
                ls.append((v, p))

    ls = sorted(ls, key=lambda x: x[1])
    print(s, ls)
    return ls
            

data = [[c[0] for c in conv_s(d)] for d in data]


ss = [int(d[0] + d[-1]) for d in data]

# print(ss)

print(sum(ss))


# YEAH part1 and part 2 in ~30'
