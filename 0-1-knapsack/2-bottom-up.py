from typing import List, Set, Dict, Tuple, Optional

# the capacity and the index is the only thing that changes
# i.e., given these remaining items, and this remaining capacity,
# can you find the optimal knapsack?

# and this is a repeated sub problem that can be stored somewhere

# with bottom up its a bit harder to understand
# you need to solve for (capacity, item_index) backwards
# i.e. (0, 3), (0, 2), (0, 1), (0, 0) first
# because (0, 0) depends on
#               (0, 1) depends on
#                   (0, 2) depends on
#                       (0, 3) depends on

# you need to fill the store with all the base cases in advance
# (it's no longer part of the recursion)


class Problem:
    def __init__(
        self,
        capacity: int,
        weights: List[int],
        profits: List[int],
        items: List[str],
        index: int = 0,
    ):
        self.capacity = capacity
        self.weights = weights
        self.profits = profits
        self.items = items
        self.index = index


# (capacity, index) => [items]
store: Dict[Tuple[int, int], List[str]] = {}


def init(p: Problem):
    # with capacity == 0, all tuples map to empty array of items
    # in other words, when u dont have any capacity, you can't pick any items
    for i in range(len(p.items)):
        store[(0, i)] = []

    # with any capacity c, and at the first index 0
    # you only got one item to choose from, so you choose it
    # as long as it doesn't exceed capacity
    # there are no sub problems to solve for this first item index
    # (i.e. there is nothing else to choose from)
    for c in range(p.capacity + 1):
        if p.weights[0] <= c:
            store[(c, 0)] = [p.items[0]]
        else:
            store[(c, 0)] = []

    return p


# strangely, it seems easiest to work backwards
# i.e you first decide whether you want to choose the item at index 3
# and then that decision is based on what it would do to item at index 2 and so on


def solution(p: Problem):

    # work index
    for i in range(1, len(p.items)):

        for c in range(1, p.capacity + 1):

            # don't choose the current item
            # so capacity remains unchanged
            # the solution to the current problem is therefore the same capacity,
            # and with the remaining items
            without_set = store[(c, i - 1)]

            # choose the current item
            # subtract its weight from the capacity
            # the solution to the current problem is therefore the remaining capacity
            # and with the remaining items
            with_set = store[(c - p.weights[i], i - 1)] if p.weights[i] <= c else []

            # find out which one gives more profits
            without_set_profit = sum(
                [p.profits[p.items.index(item)] for item in without_set]
            )
            # with_set is the sum of the previous problem + the current chosen item
            with_set_profit = (
                (
                    sum([p.profits[p.items.index(item)] for item in with_set])
                    + p.profits[i]
                )
                if p.weights[i] <= c
                else 0  # prevents overreaching in the start
            )

            # the solution is the set which gives the most profits
            if without_set_profit > with_set_profit:
                store[(c, i)] = without_set
            else:
                store[(c, i)] = with_set + [p.items[i]]  # concatenate lists

    # return target capacity with all items available to use
    return store[(p.capacity, len(p.items) - 1)]


s1 = solution(
    init(
        Problem(
            capacity=7,
            weights=[1, 2, 3, 5],
            profits=[1, 6, 10, 16],
            items=["A", "B", "C", "D"],
        ),
    )
)

print(s1)
