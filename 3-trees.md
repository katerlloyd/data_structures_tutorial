# Trees

## Introduction and Uses

What is the purpose of the data structure?

What kind of problems can be solved using the data structure?

## Recursion

Before we can go into how to use a binary search tree, we need to make sure that the concept of recursion is understood. **Recursion** is where a function calls itself. This can be dangerous, however, because this will result in a function calling itself forever unless we specify a situation where recursion would not be required. This stopping place is called a **base case**. A recursive function also needs to be called on a smaller version of the problem. In other words, we need to make sure that the problem we are trying to solve gets smaller with each recursive call so that it will eventually get to the base case and stop instead of going on forever. Here is an example with the base case and smaller problem labeled:

```python
count_down = 10

def system_check(count_down):
  if count_down <= 0: # Base case (stops when the count down reaches 0)
    print("System Check Completed.")
    return
  else:
    print("Sytem Check In Progress...")
    system_check(count_down - 1) # Smaller problem (subtracts 1 from the count down with each call)
```

Another key concept that is related to recursion is called memoization. **Memoization** is where we reduce the number of recursive calls that are needed to solve the problem by *remembering* the results from the previous recursive call. Here is the another example of recursion, but this time using memoization as well:

```python
# CODE
```

## Important Concepts

How would the data structure be used in Python (in some cases you will need to discuss recursion)?

What kind of errors are common when using the data structure?

## Efficiency

Recursion is used in these operations to search through each of the subtrees.

| BST Operation | Performance | Description |
| :---: | :---: | :--- |
| insert(value) | O(log n) | Finds empty spot to insert into using recursion |
| remove(value) | O(log n) | Finds the value to remove using recursion |
| contains(value) | O(log n) | Finds the value using recursion |
| traverse_forward | O(log n) | Traverses left and then right subtrees using recursion (smallest to largest) |
| traverse_reverse | O(log n) | Traverses right and then left subtrees using recursion (largest to smallest) |
| height(node) | O(log n) | Finds the height of left and right subtrees using recursion and returns maximum height (adding one for the root node) |
| size() | O(1) | Size of tree from BST class |
| empty() | O(1) | Checks if root node is empty or size is zero |

## Example Problem

sort or search through aliens that brought back by their names, size, etc

## Problem to Solve

space ship capacity to carry them all back to see if have enough space and what ship model would have the capacity to carry them all back

[Back to Welcome Page](https://github.com/katereclark/data_structures_tutorial/blob/main/0-welcome.md)
