import sys
sys.path.append("../..")

import numpy as np
import itertools

from lib.utils import dl_lines

dl_method = dl_lines
# data = dl_method("sample.txt")
data = dl_method("input.txt")


data = [
    [
        int(elem.replace(" ", ""))
        for elem in line.split(" ")
    ] 
    for line in data
]

import numpy as np

        
        

def safe(s):
    d =  np.diff(s)
    same_sign = len(np.unique(np.sign(d))) == 1
    # I lost 10 minutes here because I never read instructions ... -_-' 
    # "all increasing or all decreasing"
    not_moving = np.sum(d) == 0 
    max_diff = np.max( np.abs(d) ) <= 3
    if same_sign and max_diff and not not_moving:
        return True
    return False

n_safe = 0
for s in data:
    if safe(s):
        n_safe += 1 # This way of counting stuffs is to damn ugly
print(n_safe)
    
n_safe_2 = 0
for n, s in enumerate(data):
    if safe(s):
        n_safe_2+=1 
    else: # OMG what I am doing ?
        for i in range(len(s)):
            sub_s = s.copy()
            del sub_s[i] # why not a this point
            if safe(sub_s):
                n_safe_2 += 1
                break
            
    
print(n_safe_2)

# 30 minutes. I need to read instructions.
