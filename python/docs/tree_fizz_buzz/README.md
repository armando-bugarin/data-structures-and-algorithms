# Code Challenge: Class 18 Fizz Buzz Tree
<!-- Description of the challenge -->

- Write a function called fizz buzz tree
- Arguments: k-ary tree
- Return: new k-ary tree

Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

- If the value is divisible by 3, replace the value with “Fizz”
- If the value is divisible by 5, replace the value with “Buzz”
- If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
- If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process
<!-- Embedded whiteboard image -->

[Whiteboard Image 18](challenge18.png)

![Whiteboard Image 18](challenge18.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

The time complexity (Big O) of the breadth-first traversal algorithm you've implemented is O(N), where N is the number of nodes in the binary tree. In the worst case, you have to visit each node once.

## Solution
<!-- Show how to run your code, and examples of it in action -->

def breadth_first(tree):
    result = []
    if not tree.root:
        return result

    queue = [tree.root]

    while queue:
        current_node = queue.pop(0)
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result
