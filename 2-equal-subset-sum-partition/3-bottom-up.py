from typing import *

# Can you partition the given set into two subsets with equal sum?

# i.e. does there exist a subset where its elements == sum / 2 ?
# (because then it means that the remaining elements also sum to the same thing)

# i.e. does there exist a knapsack where the sum(elements) == sum / 2

# top down memo
# the changing stuff is the index, and also the remaining sum
# these are the subproblems

# (remaining_sum, item_index) => [items]
store: Dict[Tuple[int, int], List[int]] = {}


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


def init(h: Helper):
    # with remaining_sum == 0, all tuples map to empty array of items
    # in other words, when u dont have any sum left, you can't pick any items
    for i in range(len(h.items)):
        store[(0, i)] = []

    # with any remaining_sum s, and at the first index 0
    # you only got one item to choose from, so you choose it
    # as long as it == the sum
    # there are no sub problems to solve for this first item index
    # (i.e. there is nothing else to choose from)
    for s in range(h.remaining_sum + 1):
        if h.items[0] == s:
            store[(s, 0)] = [h.items[0]]
        else:
            store[(s, 0)] = []

    return h


def generate(h: Helper):

    # work index
    for i in range(1, len(h.items)):

        for s in range(1, h.remaining_sum + 1):

            # don't choose the current item
            # so sum remains unchanged
            # the solution to the current problem is therefore the same sum,
            # and with the remaining items
            without_set = store[(s, i - 1)]

            # choose the current item
            # subtract its weight from the sum
            # the solution to the current problem is therefore with the remaining sum
            # and with the remaining items
            with_set = store[(s - h.items[i], i - 1)] if h.items[i] <= s else []

            # find out which one equals the target sum
            with_set_sum = sum(with_set) if h.items[i] <= s else 0
            without_set_sum = sum(without_set)

            if with_set_sum == s:
                store[(s, i)] = with_set
            elif without_set_sum == s:
                store[(s, i)] = without_set
            else:
                store[(s, i)] = []

    # return target sum with all items available to use
    return store[(h.remaining_sum, len(h.items) - 1)]


def generate_wrapper(h: Helper):
    if sum(h.items) % 2 != 0:
        return []
    return generate(h)


s1 = generate_wrapper(init(Helper(items=[1, 2, 3, 4])))
s2 = generate_wrapper(init(Helper([1, 1, 3, 4, 7])))
s3 = generate_wrapper(init(Helper(items=[2, 3, 4, 6])))
s4 = generate_wrapper(init(Helper(items=[2, 4])))
print(s1)
print(s2)
print(s3)
print(s4)
