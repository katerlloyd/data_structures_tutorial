# Sets

## Introduction and Uses

A set is a data structure where the order of the items inside is not important and each item in the set must be unique. This means that a set cannot contain duplicates and is very efficient when it comes to determining whether an item is in the set. Sets can be used for a variety of things in Python, but some of the most common include situations where a fast lookup is vary valuable, when you want to make completely sure that there won't be any duplicates at all in your data or results, and when you want to merge data together (merge two sets together) into one or find which items are the same in both sets. 

If we have two sets that we want to merge, we can use the `union` function in Python. 

```python
groceries = {"pizza", "brownies", "bacon", "cheese"}
desserts = {"brownies", "cookies", "tarts"}

all_foods = union(groceries, desserts) # or you can write all_foods = groceries | desserts

# all_foods will contain {"pizza", "tarts", "bacon", "cheese", "cookies", "brownies"}
```
We can use the `intersection` function to find out what items are in both of the sets.

```python
matching_foods = intersection(groceries, desserts) # or you can write matching_foods = groceries & desserts

# matching_foods will contain {"brownies"}
```

If you wanted to determine which items were different between each set, then you could use the `difference` function.

```python
different_foods = groceries.difference(desserts)

# different_foods will contain {"cheese", "pizza", "bacon}
```

## Important Concepts

The O(1) efficiency of operations in a set is due to hashing. Hashing maps an item in the set to a specific index location through a function that converts the item's value into an index number, especially if the item is not an integer. This is a key part of the set data structure and allows for quick recall and lookup using the `index(n) = n` formula. As an example, if we add the numbers 0, 2, and 3 to a set, the numbers would be located at index(0) = 0, index(2) = 2, and index(3) = 3. This is called a sparse list because the items do not necessarily get added from exactly left to right like a stack. Only one value can be placed at that index, so no duplicates can be added.

| 0 |   | 2  | 3  |   |  |  |
| :------: | :------: | :------: | :------: | :------: | :------: |  :------: |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |

This method does not work very well once we get to larger numbers since it would demand that there be a lot of empty space if you only put in a few numbers which would be a huge waste of memory that could be used for something else. This is why we use another formula for these kinds of situations: `index(n) = n % spare list size`. This would mean that if we wanted to add the number 275061497 we would say that index(275061497) = 275061497 % 7 since `len(set) = 7`, which would give us an index of 4. We can use a hashing to add things that are not intergers using the formula `index(n) = hash(n) % sparse list size` with the `hash(n)` function in python. For non-integers, the hashing function will produce a different value each time the fucntion is run. 

| 0 |   | 2  | 3  | 275061497  |  |  |
| :------: | :------: | :------: | :------: | :------: |  :------: |  :------: |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |

But what if we also wanted to add the number 4 to the set? This would create what is called a conflict. One way to resolve a conflict with sets it by using open addressing. This tells us to move the offending item (the one that also wants to go into the same index) to the next open spot. So 4 would be placed at index 5. If we wanted to add the number 5 or the number 2202 (2202 % 7 = 4) to the set, now we would have to move it to index 6 instead since both index 4 and index 5 are taken. Each time we do this we create another conflict and this can easily get out of hand rather quickly.  

| 0 |   | 2  | 3  | 275061497  | 4 | 5 |
| :------: | :------: | :------: | :------: | :------: |  :------: |  :------: |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |

There is a better way. This second option is called chaining. This method tells us to make a list of the values that occupies the same index. So if we added 4 to the set when 275061497 is already occupying index 4, then we would created a list at index 4 and add each number to the list. Adding the number 2202 to index 4 would look the same. This means that when we add the number 5 to index 5 there are no conflicts. Unfortunately both of these solutions negatively impact the performance, so we need to increase the size of the set if there are too many conflicts and then use the `index(n)` function again to reposition all of the items. 

| 0 |   | 2  | 3  | 275061497, 4, 2202  | 5 |  |
| :------: | :------: | :------: | :------: | :------: |  :------: |  :------: |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 |

One common error that can be made when working with sets is trying to hash a list or a dictionary, which cannot be done since they are both mutable or changeable data structures and cannot be hashed. Some other errors are trying to remove an items from a set that is not actually contained in the set or trying to change an item that has already been placed in a set. You cannot change an item once it has been added to the set since they are immutable or unchangeable.

## Efficiency

These performance levels depends on the hashing and may become O(n) in a worst case scenario but are O(1) in most situations. 

| Set Operation | Code | Performance | Description |
| :---: | :---: | :---: | :---: |
| Add | set.add(value) | O(1) | Add value to set |
| Remove | set.remove(value) | O(1) | Remove value from set |
| Size | length = len(set) | O(1) | Size of set |
| Member | if value in set: | O(1) | Check if value is in set | 

## Example Problem

... To do this, we need to create an empty set. In Python, a set is made by writing `set_name = set()`.

rocket_ship_models = ["W-19 Pegasus", "X-98 Megaship", "L-75 Titan", "R-26 Surveyer", "W-19 Pegaus", "T-13 Lander", "D-47 Schmidt", "L-74 Titan", "L-75 Titan"]

oh no! the list they gave us has duplicate rocket ship models and now the sytem thinks that there are more models (or aliens) than there really are! How do we fix it? We could use a set since it doesn't allow any duplicates. Now each model is only listed once and we won't accidentally select one twice and the system knows how many there actually are.

need fast lookup of spaceship models (or aliens in next problem)

## Problem to Solve

showcasing the aliens you brought back - don't want any diplicates of each type - order doesn't matter since we don't know how to classify them yet

[Back to Welcome Page](https://github.com/katereclark/data_structures_tutorial/blob/main/0-welcome.md)
