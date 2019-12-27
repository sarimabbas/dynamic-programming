from typing import *


def generate(input_set: List, index=0):

    # base case
    if index > len(input_set) - 1:
        return [[]]

    # the "recursive" part
    down_the_tree = generate(input_set, index + 1)

    # keep the current index and recursively tack on the rest
    with_set = [[input_set[index]] + x for x in down_the_tree]

    # don't keep the current item and recursively tack on the rest
    without_set = [[] + x for x in down_the_tree]

    # return both to the next level
    return with_set + without_set


s1 = generate(["A", "B"])

print(s1)
