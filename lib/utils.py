import numpy as np
import itertools


def dl_lines(fp="input.txt"):
    with open(fp, mode="r") as f:
        data = [n.replace("\n", "") for n in f.readlines()]
    return data


def dl_blockoflines_str(fp="input.txt"):
    with open(fp, mode="r") as f:
        data = [n.replace("\n", "") for n in f.readlines()]
        data = [d.replace("\n", " ") for d in data.split("\n\n")]
    return data


def dl_blockoflines_list(fp="input.txt"):
    with open(fp, mode="r") as f:
        data = [n.replace("\n", "") for n in f.readlines()]
        data = [d.split("\n") for d in data.split("\n\n")]
    return data

