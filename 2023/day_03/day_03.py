import sys
sys.path.append("../..")

import numpy as np
import itertools
from lib.utils import dl_lines

dl_method = dl_lines
# dl_method = dl_blockoflines_str
# dl_method = dl_blockoflines_list

import re

# data = dl_method("sample.txt")
# data = dl_method("sample_2.txt")
data = dl_method("input.txt")
map = data
for m in map:
    print(m)
compiled = re.compile(r'[A-Za-z]+|\d+|\W')# <- this one cost me 1h : I need to get better at regex
        

list_number = set()
map_gear = [ 
    [
        [] 
        for _ in range(len(map[0]))
    ] 
    for _ in range(len(map)) 
]

newmap = map.copy()
for i, l in enumerate(map):
    numbers= []
    res = compiled.finditer(l)
    for r in res:
        if r.group(0).isdigit(): # this part could've been worst
            start = r.start()
            end = r.end()
            numbers.append(
                (r.group(0), start, end)
            )
    for n, s, e in numbers:
        bok = (False, 0, 0, 0, 0) # <- I started to panick and wanted to store every piece of information that I had in mind => Mostly useless
        gearok = (0, 0, n) # totally useless  
        bnok = True # I don't remember writing this -_-'
        if n.isdigit():
            for dx in [-1, 0, 1]:
                x = i + dx
                if 0 <= x < len(data):
                    nl = data[x]
                    for y in range(s-1, e+1):
                        if 0<= y < len(l):
                            value = data[x][y]
                            if value != "." and not value.isdigit():
                                bok = (True, n, i, s, e)
                            if value == "*":
                                map_gear[x][y].append(n)
                                
            if bok[0]:
                n, i, s, e = bok[1], bok[2], bok[3], bok[4]
                list_number.add((n, i, s, e))
                for x in range(s, e):
                    newmap[i] = newmap[i][:x] + "A" + newmap[i][x + 1:]

                
print("part1", sum([int(n[0]) for n in list_number]))


sum_ratio_gear = 0
for lmp in map_gear:
    for pg in lmp:
        if len(pg) == 2:
            rg = int(pg[0]) * int(pg[1])
            sum_ratio_gear += rg
print("part2" , sum_ratio_gear)

# 1 day to finish... but I spend most of the time in Christmas shopping and "marché de Noël"
