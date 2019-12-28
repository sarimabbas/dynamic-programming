# Equal subset sum partition

## Problem

Similar to the 0-1 Knapsack problem.

- Given a list of numbers: `items = [1, 2, 3, 4]`
- Can you split into two sets such that they have the same sum?
  - E.g. `[1, 2, 3, 4] = [2, 3] + [1, 4]` and `sum([2,3]) == sum([1, 4]) == 5`.
- Reformulated: can you create a single set from `items` such that the subset is equal to `sum(items) / 2`? (Because if you can create a single set that sums to `sum(items) / 2`, then that means the other set also sums to the same number).
  - E.g. if we can create a set `[1, 4]` that sums to `(10 / 2) == 5`, then we're done.

## Brute force

### Recursive algo

1. Let `with_set` be the knapsack with the current item (`i == 0` to start) `item[i]` if <= `remaining_sum` + the optimal knapsack recursively constructed from all other items `items[i + 1:]` and the remaining sum: `remaining_sum - items[i]`
2. Let `without_set` be the knapsack without the current item (`i == 0` to start) + the optimal knapsack recursively constructed from all other items `items[i + 1:]` and the remaining unchanged sum `remaining_sum`
3. Return the one that is == `remaining_sum`
