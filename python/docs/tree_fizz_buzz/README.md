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

Traversing each node in the k-ary tree has a time complexity of O(N), where N is the number of nodes in the tree. The space complexity is O(N).

## Solution
<!-- Show how to run your code, and examples of it in action -->

def fizz_buzz_tree(tree):
    def fizz_buzz_recursive(node):
        if not node:
            return None

        value = node.value

        if value % 3 == 0 and value % 5 == 0:
            node.value = "FizzBuzz"
        elif value % 3 == 0:
            node.value = "Fizz"
        elif value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(value)

        for child in node.children:
            fizz_buzz_recursive(child)

    # Clone the input tree to avoid modifying the original tree
    cloned_tree = tree.clone()

    fizz_buzz_recursive(cloned_tree.root)

    return cloned_tree
