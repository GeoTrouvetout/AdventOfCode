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


data = {
        d.split(": ")[0] : (
            [ int(c) for c in d.split(": ")[1].split(" | ")[0].split(" ") if len(c) >0 ],
            [ int(c) for c in d.split(": ")[1].split(" | ")[1].split(" ") if len(c) >0 ],
        )
     
    for d in data
}


print(data)

l_score = []
for card, (mn, wn) in data.items() :
    # ncard = int(card.split("Card ")[1].replace(" ", ""))
    # print(ncard)
    score = 0
    ncardok = 0
    for num in mn:
        if num in wn:
            if score == 0:
                score = 1
            else:
                score *=2
            ncardok +=1
    l_score.append(score)
    # print(card, score)
    
    
print("part1", sum(l_score))

lcards = {int(card.split("Card ")[1].replace(" ", "")): [nums] for card, nums in data.items()} # I decided to store every duplicate card in a evergrowing list of cards => worst idea in term of optimization >:(

l_score = []
for idcard, lmnws in lcards.items() : # all of this part2 for loop is particularly not optimized 
    print(idcard, len(lcards[idcard])) # I add some printing log to look at progression during code running => I was also looking at htop to see my ram melting like snow in the sun ...
    for (mn, wn) in lmnws: # here I recompute everything everytime because I am not clever under time constraints (｡･･｡)
        score = 0# artefact of part 1 because I'm lazy AF => useless
        ncardsok = 0
        for num in mn: 
            if num in wn:
                if score == 0:# artefact of part 1 because I'm lazy AF => useless
                    score = 1 # artefact of part 1 because I'm lazy AF => useless 
                else:# artefact of part 1 because I'm lazy AF => useless
                    score *=2# artefact of part 1 because I'm lazy AF => useless
                ncardsok +=1
        if ncardsok > 0:
            for n in range(idcard+1, idcard+1+ncardsok):
                lcards[n].append(lcards[n][0])
        

for idcard, lmnws in lcards.items() :
    print(idcard, len(lmnws))

print("part2",  sum([len(v) for v in lcards.values()]))

# finished in 15'
