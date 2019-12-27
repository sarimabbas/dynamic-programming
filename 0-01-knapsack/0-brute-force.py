from typing import List, Set, Dict, Tuple, Optional


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


def solution(p: Problem):
    # base case: no items to choose from, so return empty array
    if p.index > len(p.items) - 1:
        return []

    # choose to keep current index item if capacity remaining
    with_set = []
    if p.weights[p.index] <= p.capacity:
        with_set = [p.items[p.index]]
        with_set.extend(
            solution(
                # fmt: off
                Problem(
                    p.capacity - p.weights[p.index],
                    p.weights,
                    p.profits,
                    p.items,
                    p.index + 1,
                )
                # fmt: on
            )
        )

    # choose not to keep it
    without_set = []
    without_set.extend(
        solution(
            # fmt: off
            Problem(
                p.capacity,
                p.weights,
                p.profits,
                p.items,
                p.index + 1
            )
            # fmt: on
        )
    )

    # calculate profits
    with_set_profit = sum([p.profits[p.items.index(item)] for item in with_set])
    without_set_profit = sum([p.profits[p.items.index(item)] for item in without_set])

    return with_set if with_set_profit > without_set_profit else without_set


s1 = solution(
    Problem(
        capacity=7,
        weights=[1, 2, 3, 5],
        profits=[1, 6, 10, 16],
        items=["A", "B", "C", "D"],
    )
)

print(s1)
