import sys
sys.path.append("../..")

import numpy as np
import itertools
from lib.utils import dl_lines, dl_blockoflines_str, dl_blockoflines

# dl_method = dl_lines
# dl_method = dl_blockoflines_str
# dl_method = dl_blockoflines_list
dl_method = dl_blockoflines


# data = dl_method("sample.txt")
# data = dl_method("sample_2.txt")
data = dl_method("input.txt")


data = {
    d.split(":\n")[0] : [c.strip().split(" ") for c in d.split(":\n")[1].split("\n")]
    for d in data
}

data = {
    k : [
            [int(__v) for __v in _v if __v!=''] for _v in v if len(_v)>1
    ]
    for k, v in data.items()
}


seeds = data["seeds"][0]

del data["seeds"]

maps = data
print(seeds)
print(maps)
mappings = {}
for name, map in maps.items():
    name = name.replace(" map", "")
    source = name.split("-to-")[0]
    dest= name.split("-to-")[1]
    mapping = []
    for line in map:
        drs = line[0]
        srs = line[1]
        rl = line[2]
        mapping.append((srs, srs+rl-1, drs-srs))
        # for _i in range(rl):
            # print(srs+_i, drs+_i)
            # mapping.append( (srs, ) )
    mappings[source] =  {
        "mapping" : mapping, "dest":dest
    }
    # print(mapping)

print(mappings.keys())
llocations = []
lseeds = []
for seed in seeds:
    path = [seed]
    keypath = ["seed"]
    source  = "seed"
    dest = source
    while source != "location":
        value = path[-1]
        for start, end, add in mappings[source]["mapping"]:
            if start<=value<=end:
                value = value + add
                break
        dest = mappings[source]["dest"]
        path.append(value)
        keypath.append(source)
        print(dest)
        source = dest
    # print(keypath)
    print(path)
    llocations.append(path[-1])

print("part1" , min(llocations))    # OK complete in 5'


# part 2 I realized that I need to optimize the search

 
minlocations = np.inf
bestseed = 0
bestss = 0
bestrs = 0
for i in range(0, len(seeds), 2):
    ss = seeds[i]
    rs = seeds[i+1]
    previous_path = 0
    diff = 0
    path = np.inf
    naug = 0
    for seed in range(ss, ss+rs, 10000): # no time for Bayesian search I will perform N resolution grid search
        previous_path = path
        path = seed
        
        # keypath = ["seed"]
        source  = "seed"
        dest = source
        while source != "location":
            value = path
            for start, end, add in mappings[source]["mapping"]:
                if start<=value<=end:
                    value = value + add
                    break
            dest = mappings[source]["dest"]
            path = value
            # keypath.append(source)
            # print(dest)
            source = dest
        if path < minlocations:
            minlocations = path #.append(path)
            bestseed = seed
            bestss = ss
            bestrs = rs
            
print("part2.a" , minlocations, bestseed, bestss, bestseed-bestss)    
minlocation = np.inf

for seed in range(bestseed-1000, bestseed+1000, 1): # from the point found before I hoped that -1000;1000 will be enough => which relies on pure luck
    path = seed

    source  = "seed"
    dest = source
    while source != "location":
        value = path
        for start, end, add in mappings[source]["mapping"]:
            if start<=value<=end:
                value = value + add
                break
        dest = mappings[source]["dest"]
        path = value
        source = dest
    if path < minlocations:
        minlocations = path #.append(path)

print("part2" , minlocations)  # turns out that pure luck sometimes works :)

# complete in ~1 hours  

