# Stacks

## Introduction and Uses

What is the purpose of the data structure?

What is the performance of the data structure (you will need to talk about big O notation)?

What kind of problems can be solved using the data structure?

How would the data structure be used in Python (in some cases you will need to discuss recursion)?

What kind of errors are common when using the data structure?

## Important Concepts

```python docking_steps = ["4. Connect spaceship port to docking platform", "2. Line up with space station docking platform", "1. Maintain orbit with space station", "5. Engage locking mechanisms", "6. Depressurize docking bay", "3. Engage thrusters"]```

## Efficiency

## Example Problem
After traveling for weeks the space station has finally come into sight! Man, if we mess up the docking phase... Well, let's just make sure that we don't. Good thing we made that list of spaceship docking steps! Now, how could we be sure that they would come out in the right order so we don't expload our new ship? We need a data structure that is ordered and lets us take out the information in a certain order. A stack should do the trick!

We will start with an empty list (stack) to create a docking procedure with.

`docking_procedure = []`

Because a stack allows us to take out the data in the opposite order that we put them in, we will be adding the steps in from the `docking_steps` lists starting with the last step first.

```python
docking_procedure.append("6. Depressurize docking bay")
docking_procedure.append("5. Engage locking mechanisms")
docking_procedure.append("4. Connect spaceship port to docking platform")
docking_procedure.append("3. Engage thrusters")
docking_procedure.append("2. Line up with space station docking platform")
docking_procedure.append("1. Maintain orbit with space station")
```

Now that the steps have all been added, we can remove them once they have been completed and stop once the stack is empty.

```python
for step in docking_procedure:
  if len(docking_procedure) == 0:
    print("Docking Complete")
  else:
    print(f"Completed: {step}")
    dockiing_procedure.pop(step)
```

## Problem to Solve
spaceship launch codes - boss told you that he wants you to use the most recent one that was created and put in. how can we know which one that was?

[Back to Welcome Page](https://github.com/katereclark/data_structures_tutorial/blob/main/0-welcome.md)
