# Powersets

The 0-1 knapsack problem involves choosing or not choosing an element to build a knapsack. We have to similarly choose or not choose an element to construct all possible combinations/subsets of a set (i.e. the power set).

## Choosing the current item

The output of the recursion should give the powerset of the remaining items. Then, the current item is "tacked" onto each of those via concatenation.

## Not choosing the current item

The output of the recursion should give the powerset of the remaining items. Then, the empty set is "tacked" onto each of those via concatenation. This is the identity function, i.e. the remaining items are left as is. `[] + x for x in down_the_tree` is not strictly required and can just be `x for x in down_the_tree`.

## Combining both sets

Once the current item has been both tacked onto the result of the recursion, and "not tacked on", we merge both sets together and return the powerset.

## Where does the empty set come from?

This is added when no elements are chosen (look at the yellow shaded path in the tree of recursive calls).