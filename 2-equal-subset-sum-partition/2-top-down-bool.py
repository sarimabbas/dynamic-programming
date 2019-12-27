from typing import *

# Can you partition the given set into two subsets with equal sum?

# i.e. does there exist a subset where its elements == sum / 2 ?
# (because then it means that the remaining elements also sum to the same thing)

# i.e. does there exist a knapsack where the sum(elements) == sum / 2

# top down memo
# the changing stuff is the index, and also the remaining sum
# these are the subproblems

# (remaining_sum, item_index) => [items]
store: Dict[Tuple[int, int], bool] = {}


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

    if h.remaining_sum == 0:
        return True

    if h.item_index > len(h.items) - 1:
        return False

    # if this subproblem is already solved, then return
    if (h.remaining_sum, h.item_index) in store:
        return store[(h.remaining_sum, h.item_index)]

    # decide to keep item
    curr_item = h.items[h.item_index]
    with_set = False
    if curr_item <= h.remaining_sum:
        if (
            generate(
                Helper(
                    remaining_sum=h.remaining_sum - curr_item,
                    items=h.items,
                    item_index=h.item_index + 1,
                )
            )
            == True
        ):
            with_set = True

    # decide not to keep item
    without_set = False
    if (
        generate(
            Helper(
                remaining_sum=h.remaining_sum,
                items=h.items,
                item_index=h.item_index + 1,
            )
        )
        == True
    ):
        without_set = True

    if with_set or without_set:
        store[(h.remaining_sum, h.item_index)] = True
        return True
    else:
        store[(h.remaining_sum, h.item_index)] = False
        return False


def generate_wrapper(h: Helper):
    if sum(h.items) % 2 != 0:
        return False
    return generate(h)


s1 = generate_wrapper(Helper(items=[1, 2, 3, 4]))
s2 = generate_wrapper(Helper([1, 1, 3, 4, 7]))
s3 = generate_wrapper(Helper(items=[2, 3, 4, 6]))
s4 = generate_wrapper(Helper(items=[2, 4]))
print(s1)
print(s2)
print(s3)
print(s4)
