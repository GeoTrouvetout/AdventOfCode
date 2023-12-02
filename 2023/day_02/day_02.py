import sys
sys.path.append("../..")
import pprint
import numpy as np
import itertools
from lib.utils import dl_lines

dl_method = dl_lines
# dl_method = dl_blockoflines_str
# dl_method = dl_blockoflines_list


# data = dl_method("sample.txt")
# data = dl_method("sample_2.txt")
data = dl_method("input.txt")


data = { # <- only thing I'm proud of => I wrote it straight without error
        int(d.split(":")[0].replace("Game ", "")) : [
            {
                
                    s.strip().split(" ")[1]: int(s.strip().split(" ")[0])
                 
                for s in c.split(", ")
            }
            for c in d.split(":")[1].split(";")]  

for d in data
} 


pprint.pprint(data) # I decided that I needed to lose time to pretty print stuff 


nb = { # <- nb is particularly useless => shamely keeping it for the record
    "red" : 12, 
    "green" :13,
    "blue" : 14
}
vnb = [12, 13, 14] 

def get_v(game) : # <- here I realized that i needed to transform games into vector            
    v = [
        max([ g["red"] for g in game if "red" in g]), # <- I lost 20' by confusing 'max' with 'sum' because I can't read instructions...
        max([ g["green"] for g in game if "green" in g]), # <- Indeed if you sum the 'greens' you'll get higher score 
        max([ g["blue"] for g in game if "blue" in g]), # <- And guess what? enven so 'sum' is stupid, it worked on sample.txt => but absolutely not with 'input.txt' => got stuck in part1 20' ... just sad
    ]
    return v 


vgames = {k: get_v(g) for k, g in data.items()}
pprint.pprint(vgames) # Why ? don't know. If any guess don't hesitate to contact me at pprint4nothing@junkidea.org 

lcombgameok = []
lcombvalueok = []
for n in range(1, 2): # <- this for-loop is pitiable => I tough that I would need it to find game combination in part2 -> turns out absolutely not -_-'
    for combgame in itertools.combinations(vgames.keys(), n): # <- this one is a deadfull consequence of the above for loop and splendidly complicate thing just for fun
        # print(combgame)
        bok = True
        vnb = np.array([12, 13, 14])
        for vg in combgame: # this for loop demonstrate how ridiculeously I am stuck in this for-loops hell from 
            vnb -= np.array(vgames[vg])
            if vnb[0] < 0 or vnb[1] < 0 or vnb[2] < 0:
                bok = False
                # break # <- This is a bteautiful exemple of something useless
        if bok:
            # print("conf ok", vnb, vgames[vg], combgame) 
            lcombgameok.append(combgame)
        lcombvalueok.append(vgames[vg])
        
# print(nmax)

def multi(x): # I forgot how to do it with numpy => I had to rewrite it very quickly in an outrageous way
    r = 1
    for _x in x:
        r *= _x
    return r

print("part1", sum([sum(c) for c in lcombgameok if c]))
print("part2", sum([multi(c) for c in lcombvalueok]))


# YEAH 1h35 !!
