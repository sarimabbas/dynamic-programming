# 0-1 Knapsack Problem 

## Problem

We're given a bunch of items: `items = [A, B, C, D]`.
Their corresponding weights: `weights = [1, 2, 3, 5]`.
Their corresponding profits: `profits = [1, 6, 10, 16]`.
And a weight limit/capacity: `capacity = 7`.

We want to find a combination of items which maximizes profit while being <= capacity.

## Brute force 

We want to iterate all possible knapsack bundles that are <= capacity, and check the profit for each one.

For an array of `N` items, `2^N` combinations are possible. For each item, you decide whether or not to keep it (i.e. flipping a binary switch). For e.g: `[A, B, C]` gives these `2^3 = 8` combinations: 

```
[]
[A]
[B]
[C]
[A, B]
[B, C]
[A, C]
[A, B, C]
```

This happens to be the powerset of `[A, B, C]`. For each combination, we check if it's <= capacity and then select the one that gives the most profit. 

### Algo 1

1. Generate the powerset `ps` of the `items`
2. Filter `ps` such that it only contains subsets <= capacity
3. Return the subset which has the highest profit

TC `O(2^N)`

### Similar Algo 2

1. Let `with_set` be the knapsack with the current item (`i == 0` to start) `item[i]` if within capacity + the optimal knapsack recursively constructed from all other items `items[i:]` and the remaining capacity `capacity - weights[i]`
2. Let `without_set` be the knapsack without the current item (`i == 0` to start) + the optimal knapsack recursively constructed from all other items `items[i:]` and the remaining unchanged capacity `capacity`
3. Return the one that maximises profit 

<!-- TODO: why is powerset and this recursive approach similar -->

TC `O(2^N)`

### Recursion call tree

![Call tree](./calltree.png)

- The green path is the optimal one
