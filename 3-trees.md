# Trees

## Introduction and Uses

What is the purpose of the data structure?

What kind of problems can be solved using the data structure?

What kind of errors are common when using the data structure?

## Recursion

How would the data structure be used in Python (in some cases you will need to discuss recursion)?

## Important Concepts

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
