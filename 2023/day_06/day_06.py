import sys
sys.path.append("../..")

import numpy as np
import itertools
from lib.utils import dl_lines, dl_blockoflines_str, dl_blockoflines
import re
dl_method = dl_lines


data = dl_method("sample.txt")
data = {
    re.split(r':\s+', d)[0] : re.split(r'\s+', re.split(r':\s+', d)[1])
    for d in data
}

print(data)

races = [
    (int(t), int(d))
    for t, d in zip(data["Time"], data["Distance"])
]

print(races)

lnwin = []
for time, dmax in races:
    nwin = 0
    for v in range(time):
        timeleft = time-v
        dist = timeleft * v
        if dist > dmax:
            nwin += 1
    print(time, nwin, dmax)
    lnwin.append(nwin)

respart1 = 1
for nwin in lnwin:
    respart1 *= nwin
print("part1", respart1) # easy 


# data = dl_method("sample.txt")
# data = dl_method("sample_2.txt")
data = dl_method("input.txt") # here I've been lazy so I copy paste every thing
# print
print(data)
data = {
    re.split(r':\s+', d)[0] : re.split(r':\s+', d)[1].replace(" ", "")
    for d in data
}

print(data)

races = [ (int(data["Time"]), int(data["Distance"]))]

print(races)

lnwin = []
time, dmax = races[0]
nwin = 0
previous_dist = 0
megamax = time**2 / 4 #here I loste my time with dumb-and-completly-false math 
delta = megamax-dmax # again

lower = ( time - np.sqrt( time**2 - 4*dmax) ) / 2 # I finally remember my class math
higher = ( time + np.sqrt( time**2 - 4*dmax) ) / 2
print(lower, higher)
print(np.round(lower), np.round(higher))
print(np.ceil(higher)-np.ceil(lower)) # np.ceil is pure luck again
