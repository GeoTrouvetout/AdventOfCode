import sys
sys.path.append("../..")

import numpy as np
import itertools
from lib.utils import dl_lines, dl_blockoflines_str, dl_blockoflines
import re


score_hand = {
    "five" : 7,
    "four" : 6,
    "full" : 5,
    "three" : 4,
    "doublepair" : 3,
    "pair" : 2,
    "highcard" : 1
}


def detect_hand(hand):
    r, c = np.unique(hand["hand"], return_counts=True)
    n = len(r)
    counts = dict(zip(r, c))
    # print(counts)
    # print(r, counts)
    if n == 1:
        return score_hand["five"]
    if n == 2:
        if 4 in counts.values():
            return score_hand["four"]
        else:
            return score_hand["full"]
    if n==3:
        if 3 in counts.values():
            return score_hand["three"]
        else:
            return score_hand["doublepair"]
    if n==4:
        return score_hand["pair"]
    if n == 5:
        return score_hand["highcard"]

def detect_hand_with_joker(hand):
    r, c = np.unique(hand["hand"], return_counts=True)
    n = len(r)
    counts = dict(zip(r, c))
    n_joker= 0
    if "J" in counts.keys():
        n_joker = counts.pop("J")
        # print("njoker", n_joker)
        if n_joker == 5:
            counts = {"J" : 5}
    bestcard = max(counts, key=counts.get)
    counts[bestcard] += n_joker
    
    new_hand = []
    for k, v in counts.items():
        for i in range(v):
            new_hand.append(k)
    r, c = np.unique(new_hand, return_counts=True)
    n = len(r)
    # print(hand["hand"], new_hand)
    if n == 1:
        # print("ici", n_joker)
        return score_hand["five"]
    if n == 2:
        if 4 in counts.values():
            return score_hand["four"]# + n_joker
        else:
            return score_hand["full"]# + n_joker
    if n==3:
        if 3 in counts.values():
            return score_hand["three"]# + n_joker
        else:
            return score_hand["doublepair"]# + n_joker
    if n==4:
        return score_hand["pair"]# + n_joker
    if n == 5:
        return score_hand["highcard"]# + n_joker

rank_cards_joker = {c:r for r, c in enumerate(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"])}
rank_cards = {c:r for r, c in enumerate(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])}

def compare_hands(h1, h2, rank_cards = rank_cards, detect = detect_hand):
    score_h1 = detect(h1)
    score_h2 = detect(h2)
    # print(score_h1, score_h2)
    if score_h1 > score_h2:
        return h1.copy()
    if score_h1 < score_h2:
        return h2.copy()
    else:
        for c1, c2 in zip(h1["hand"], h2["hand"]):
            if rank_cards[c1] < rank_cards[c2]:
                return h1.copy()
            elif rank_cards[c1] > rank_cards[c2]:
                return h2.copy()
            




dl_method = dl_lines


data = dl_method("input.txt")
# data = dl_method("sample.txt")

data = [(list(d.split(" ")[0]), d.split(" ")[1]) for d in data]

hands = [ { "id" : i, "hand" : hand, "bid" : bid, "rank" : 1, "score" : 0} for i, (hand, bid) in enumerate(data)]

hands_joker = [ { "id" : i, "hand" : hand, "bid" : bid, "rank" : 1, "score" : 0} for i, (hand, bid) in enumerate(data)]

for h1, h2 in itertools.combinations(hands, 2): # honestly I am lazy -_-'
    # print(h1["id"], h2["id"])
    # print("".join(h1["hand"]), "".join(h2["hand"]))
    besthand = compare_hands(h1, h2)
    hands[besthand["id"]]["rank"] += 1
    besthand_joker = compare_hands(h1, h2, rank_cards=rank_cards_joker, detect=detect_hand_with_joker)
    # print("".join(besthand["hand"])) 
    hands_joker[besthand_joker["id"]]["rank"] += 1
    if int(h1["id"]) % 100 == 0 and int(h2["id"]) % 100 == 0:
        print(h1["id"], h2["id"])

# print("part1:" , [ ("".join(hand["hand"]), hand["rank"]) for hand in hands_joker])

print("part1:" , sum([ hand["rank"] * int(hand["bid"]) for hand in hands]))
print("part2:" , sum([ hand["rank"] * int(hand["bid"]) for hand in hands_joker]))

