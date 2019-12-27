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


def generate(h: Helper):

    if h.item_index > len(h.items) - 1:
        return []

    # if this subproblem is already solved, then return
    if (h.remaining_sum, h.item_index) in store:
        return store[(h.remaining_sum, h.item_index)]

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

    # decide not to keep item
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
        # add to store
        store[(h.remaining_sum, h.item_index)] = with_set
        # return as normal
        return with_set
    if without_set_sum == h.remaining_sum:
        # add to store
        store[(h.remaining_sum, h.item_index)] = without_set
        # return as normal
        return without_set
    store[(h.remaining_sum, h.item_index)] = []
    return []


# s1 = generate(
#     Helper(
#         items=[
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#             100,
#         ]
#     )
# )

s2 = generate(
    Helper(
        items=[
            35,
            69,
            8,
            10,
            56,
            85,
            20,
            67,
            39,
            15,
            57,
            19,
            80,
            45,
            12,
            81,
            92,
            98,
            25,
            26,
            51,
            3,
            31,
            16,
            30,
            37,
            55,
            52,
            61,
            17,
            30,
            82,
            52,
            85,
            84,
            83,
            98,
            29,
            79,
            29,
            99,
            70,
            97,
            20,
            42,
            22,
            44,
            44,
            65,
            75,
            70,
            86,
            97,
            100,
            45,
            69,
            91,
            53,
            88,
            96,
            65,
            88,
            92,
            73,
            16,
            57,
            34,
            11,
            64,
            3,
            92,
            48,
            98,
            29,
            39,
            16,
            47,
            92,
            22,
            19,
            50,
            86,
            78,
            68,
            52,
            51,
            70,
            80,
            2,
            58,
            79,
            70,
            91,
            94,
            23,
            47,
            81,
            4,
            18,
            15,
        ]
    )
)
print(s2)

