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
    if not p.index > len(p.items) - 1:
        return []

    # choose to keep current index item if capacity remaining
    if p.weights[p.index] <= p.capacity:
        with_set = [p.items[p.index]]
        with_set.extend(
            solution(
                # fmt: off
                Problem(
                    p.capacity - p.weights[0],
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
    with_set_profit = [p.profits[p.items.index(item)] for item in with_set]
    without_set_profit = [p.profits[p.items.index(item)] for item in without_set]

    return with_set if with_set_profit > without_set_profit else without_set


solution(
    Problem(
        capacity=5,
        weights=[2, 3, 1, 4],
        profits=[4, 5, 3, 7],
        items=["apple", "orange", "banana", "melon"],
    )
)
