# Sets

## Introduction and Uses

A set is a data structure where the order of the items inside is not important and each item in the set must be unique. This means that a set cannot contain duplicates and is very efficient when it comes to determining whether an item is in the set. The O(1) efficiency of operations in a set is due to hashing. Hashing maps an item in the set to a specific index location through a function that converts the item's value into an index number, especially if hte item is not an integer. This is a key part of the set data structure and allows for quick recall using the `index(n) = n` formula. As an example, if we add the numbers 0, 2, and 3 to a set, the numbers would be located at index(0) = 0, index(2) = 2, and index(3) = 3. This is called a sparse list because the items do not necessarily get added from exactly left to right like a stack. Only one value can be placed at that index, so no duplicates can be added.

| 0 |   | 2  | 3  |   |
| :------: | :------: | :------: | :------: | :------: |
| 0 | 1 | 2 | 3 | 4 |

This method does not work very well once we get to larger numbers since it would demand that there be a lot of empty space if you only put in a few numbers which would be a huge waste of memory that could be used for something else. This is why we use another formula for these kinds of situations: `index(n) = n % spare list size`. This would mean that if we wanted to add the number 275,061,404 we would say that index(275,061,404) = 275,061,404 % 5 since `len(set) = 5`, which would give us an index of 4. We can use a hashing to add things that are not intergers using the formula `index(n) = hash(n) % sparse list size` with the `hash(n)` function in python. For non-integers, the hashing function will produce a different value each time the fucntion is run. 

| 0 |   | 2  | 3  | 275061404  |
| :------: | :------: | :------: | :------: | :------: |
| 0 | 1 | 2 | 3 | 4 |

But what if we also wanted to add the number 4 to the set? This would create what is called a conflict. 

One common error when working with sets is trying to hash a list, which cannot be done. 

What is the purpose of the data structure?
What kind of problems can be solved using the data structure?
How would the data structure be used in Python?

## Important Concepts

## Efficiency

| Set Operation | Code | Performance | Description |
| :---: | :---: | :---: | :---: |
| Add | set.add(value) | O(1) | Add value to set |
| Remove | set.remove(value) | O(1) | Remove value from set |
| Size | length = len(set) | O(1) | Size of set |
| Member | if value in set: | O(1) | Check if value is in set | 

## Example Problem

## Problem to Solve


[Back to Welcome Page](https://github.com/katereclark/data_structures_tutorial/blob/main/0-welcome.md)
