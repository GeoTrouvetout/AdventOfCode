import sys
sys.path.append("../..")

import numpy as np
import itertools
from lib.utils import dl_lines, dl_blockoflines_str, dl_blockoflines
import re



dl_method = dl_blockoflines


data = dl_method("input.txt")
# data = dl_method("sample.txt")
# data = dl_method("sample_2.txt")
# data = dl_method("sample_3.txt")

inst = data[0]

map = data[1].split("\n")
map = [m for m in map if len(m) > 0]
map = { m.split(" = ")[0] : m.split(" = ")[1] for m in map}
map = { k:v.replace("(", "").replace(")", "").split(", ") for k, v in map.items()}
print(inst)
print(map)

pos = "AAA"
posi = 0
n = 0
while pos != "ZZZ" : #and n <=10:
    # print("start" , pos, posi, posi%len(inst), inst[posi%len(inst)])
    _inst = inst[posi%len(inst)]
    i = 0 if _inst == "L" else 1
    pos = map[pos][i]
    
    # print(posi, _inst, pos)
    n +=1
    posi += 1
    # if n%10 == 0:
        # print(posi, _inst, pos)
        
print("part1:", n)

data = dl_method("input.txt")
# data = dl_method("sample_3.txt")

inst = data[0]

map = data[1].split("\n")
map = [m for m in map if len(m) > 0]
map = { m.split(" = ")[0] : m.split(" = ")[1] for m in map}
map = { k:v.replace("(", "").replace(")", "").split(", ") for k, v in map.items()}
# print(inst)
# print(map)

# map2 = {}
# for k, v in map.items():
#     nk = str(n_k[k[2]])
#     new_k = "".join([nk, nk, k[2]])
#     new_v = [
#         "".join([
#                 str(n_k[v[0][2]]),
#                 str(n_k[v[0][2]]),
#                 v[0][2]
#                 ]),
#         "".join([
#                 str(n_k[v[1][2]]),
#                 str(n_k[v[1][2]]),
#                 v[1][2]]),
#         ]
#     map2[new_k] = new_v
#     n_k[k[2]] += 1
#     print(nk, k[2], n_k[k[2]], map2)
# print(map2)

n = 0
posi = 0

paths = [
    k
    for k, v in map.items()
    if k[2] == "A"
]

print(paths)

len_path = []

for indpath, path in enumerate(paths): # Here I decided to compute the path lenght individually 
    _n = 0
    _posi = 0
    _path = path
    while _path[2] !="Z":
        _inst = inst[_posi%len(inst)]
        i_inst = 0 if _inst == "L" else 1
        new_pos = map[_path][i_inst]
        _path = new_pos
        _n += 1
        _posi +=1
        
    print(path, "->", _path, _n)
    len_path.append(_n)


# Here I wanted to reinvent the wheel
# But I choose to read everything in every random kid math websites from the internet and finally discover about LCM
lcm = 1
for x in len_path:
    lcm = np.lcm(x, lcm)
    print(x, lcm)

print("part2" : lcm)
