from typing import *

# Can you partition the given set into two subsets with equal sum?

# i.e. does there exist a subset where its elements == sum / 2 ?
# (because then it means that the remaining elements also sum to the same thing)

# i.e. does there exist a knapsack where the sum(elements) == sum / 2

# brute force strategy
# find all possible subsets, and check which one == sum / 2
# if none, return false, else return that subset


class Helper:
    def __init__(
        self, items: List[int], remaining_sum: int = None, item_index: int = 0,
    ):
        if remaining_sum is None:
            self.remaining_sum = int(sum(items) / 2)
        else:
            self.remaining_sum = remaining_sum
        self.item_index = item_index
        self.items = items


def generate(h: Helper):

    if h.item_index > len(h.items) - 1:
        return []

    # decide to keep item
    curr_item = h.items[h.item_index]
    with_set = []
    if curr_item <= h.remaining_sum:
        with_set = [curr_item]
    # get the recursive outcome of the other subproblems
    with_set.extend(
        generate(
            Helper(
                remaining_sum=h.remaining_sum - curr_item,
                items=h.items,
                item_index=h.item_index + 1,
            )
        )
    )

    # decice not to keep item
    without_set = []
    without_set.extend(
        generate(
            Helper(
                remaining_sum=h.remaining_sum,
                items=h.items,
                item_index=h.item_index + 1,
            )
        )
    )

    # check if any set has desired sum
    with_set_sum = sum(with_set)
    without_set_sum = sum(without_set)

    if with_set_sum == h.remaining_sum:
        return with_set
    if without_set_sum == h.remaining_sum:
        return without_set
    return []


s1 = generate(Helper(items=[1, 2, 3, 4]))
print(s1)

