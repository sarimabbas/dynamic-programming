from typing import *

# uses an index to iterate through the original set
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


# uses slicing to create progressively smaller input sets
def generate_alt(input_set: List):
    # base case
    if not input_set:
        return []

    # the recursive part
    down_the_tree = generate(input_set[1:])

    # keep the current index and recursively tack on the rest
    with_set = [[input_set[0]] + x for x in down_the_tree]

    # don't keep the current item and recursively tack on the rest
    without_set = [[] + x for x in down_the_tree]

    # return both to the next level
    return with_set + without_set


s1 = generate(["A", "B", "C"])
s2 = generate_alt(["A", "B", "C"])
assert s1 == s2

print(s1)
