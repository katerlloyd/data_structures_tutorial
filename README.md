# Data Structures Tutorial
Welcome to the Data Structures Tutorial. Every programmer should understand these data structures and what they are capable of:

* [Stacks](https://github.com/katereclark/data_structures_tutorial/blob/main/1-stacks.md)
* [Sets](https://github.com/katereclark/data_structures_tutorial/blob/main/2-sets.md)
* [Trees](https://github.com/katereclark/data_structures_tutorial/blob/main/3-trees.md)

Each module will contain descriptions and examples. At the end of each module, you will find a problem to solve on your own. You should only look at the solution after you have attempted to solve the problem first.

## Big O Notation
Before you take a look at each of these data structures, however, it is important to understand how they differ in efficiency from each other when used. Big O notation is used to determine the performance or efficiency of an algorithm or parts of an algorithm. There are generally five levels of efficiency. When listed from the best performance to the worst performance, they are: O(1), O(log n), O(n), O(n log n), and O(n<sup>2</sup>). 

**O(1)** is called constant time, meaning that the performance stays the same no matter how large the size of the data (n) is. This code usually only involves expressions.

**O(log n)** is called logarithmic time. This means that the performance decreases based upon the size of the data (n), but not as significantly as O(n). This code divides the size of the data being processed in half multiple times, usually through specific loops.

**O(n)** is called linear time. This means that as the size of the data (n) increases, the performance decreases at the same rate. This code usually has one loop that is based on the size of the data.

**O(n log n)** is called n log n time, coincidentally. This code usually uses an O(log n) algorithm combined with an O(n) algorithm, like an O(n) loop inside of an O(log n) loop or vice versa.

**O(n<sup>2</sup>)** is called polynomial time. This is the worst of the efficiency levels and should be avoided whenever possible. This code usually has one loop inside of another loop. If there were three nested loops, then this could be O(n<sup>2</sup>) efficiency.

## Contact Information
For questions or comments, please send them to:

**Kate Lloyd** | BYU-Idaho

[cla16022@byui.edu](cla16022@byui.edu)
