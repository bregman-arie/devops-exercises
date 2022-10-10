## Software Development

### Agile Software Development

<details>
<summary>What is Agile in regards to software development?</summary><br><b>

[Atlassian](https://www.atlassian.com/agile/kanban/kanban-vs-scrum): "is a structured and iterative approach to project management and product development. It recognizes the volatility of product development, and provides a methodology for self-organizing teams to respond to change without going off the rails."
</b></details>

<details>
<summary>What is Kanban in regards to software development?</summary><br><b>

* Kanban is an agile software development framework

* It focuses on having flexible and fluid process - no deadlines, fewer meetings, less formal roles
* While arguable, Kanban seems to fit better small teams rather than big teams who might benefit more from structurized process
</b></details>

<details>
<summary>What is Scrum in regards to software development?</summary><br><b>

* Scrum is an agile software development framework

* Fixed length iterations
* Requires the team to have roles like scrum master and product owner
</b></details>

<details>
<summary>Can you compare between Kanban and Scrum?</summary><br><b>

* Kanban is continuous, fluid and visualized process whereas Scrum is short and structured, where work is shipped during fixed intervals known as sprints


* Kanban is less structured compared to other frameworks like scrum
* Kanban is more visualized way of managing the development process
* Kanban has fewer meetings and formal roles compared to other frameworks like scrum
</b></details>

### Programming

<details>
<summary>What programming language do you prefer to use for DevOps related tasks? Why specifically this one?</summary><br><b>
</b></details>

<details>
<summary>What are static typed (or simply typed) languages?</summary><br><b>

In static typed languages the variable type is known at compile-time instead of at run-time.
Such languages are: C, C++ and Java
</b></details>

<details>
<summary>Explain expressions and statements</summary><br><b>

An expression is anything that results in a value (even if the value is None). Basically, any sequence of literals so, you can say that a string, integer, list, ... are all expressions.

Statements are instructions executed by the interpreter like variable assignments, for loops and conditionals (if-else).
</b></details>

<details>
<summary>What is Object Oriented Programming? Why is it important?</summary><br><b>
</b></details>

<details>
<summary>Explain Composition</summary><br><b>
</b></details>

<details>
<summary>What is a compiler?</summary><br><b>
</b></details>

<details>
<summary>What is an interpreter?</summary><br><b>
</b></details>

<details>
<summary>Are you familiar with SOLID design principles?</summary><br><b>

SOLID design principles are about:

* Make it easier to extend the functionality of the system
* Make the code more readable and easier to maintain

SOLID is:

* Single Responsibility - A class should only have a single responsibility
* Open-Closed - An entity should be open for extension, but closed for modification. What this practically means is that you should extend functionality by adding a new code and not by modifying it. Your system should be separated into components so it can be easily extended without breaking everything.
* Liskov Substitution - Any derived class should be able to substitute the its parent without altering its corrections. Practically, every part of the code will get the expected result no matter which part is using it
* Interface segregation - A client should never depend on anything it doesn't uses
* Dependency Inversion - High level modules should depend on abstractions, not low level modules
</b></details>

<details>
<summary>What is YAGNI? What is your opinion on it?</summary><br><b>
</b></details>

<details>
<summary>What is DRY? What is your opinion on it?</summary><br><b>
</b></details>

<details>
<summary>What are the four pillars of object oriented programming?</summary><br><b>
</b></details>

<details>
<summary>Explain recursion</summary><br><b>
</b></details>

<details>
<summary>Explain Inversion of Control</summary><br><b>
</b></details>

<details>
<summary>Explain Dependency Injection</summary><br><b>
</b></details>

<details>
<summary>True or False? In Dynamically typed languages the variable type is known at run-time instead of at compile-time</summary><br><b>

True
</b></details>

<details>
<summary>Explain what are design patterns</summary><br><b>

[refactoring.guru](https://refactoring.guru/): "Design patterns are typical solutions to commonly occurring problems in software design. They are like pre-made blueprints that you can customize to solve a recurring design problem in your code."
</b></details>

<details>
<summary>Explain big O notation</summary><br><b>
</b></details>

<details>
<summary>What is "Duck Typing"?</summary><br><b>
</b></details>

<details>
<summary>Explain string interpolation</summary><br><b>
</b></details>

##### Common algorithms

<details>
<summary>Binary search:

  * How does it works?
  * Can you implement it? (in any language you prefer)
  * What is the average performance of the algorithm you wrote?</summary><br><b>

It's a search algorithm used with sorted arrays/lists to find a target value by dividing the array each iteration and comparing the middle value to the target value. If the middle value is smaller than target value, then the target value is searched in the right part of the divided array, else in the left side. This continues until the value is found (or the array divided max times)

[python implementation](coding/python/binary_search.py)

The average performance of the above algorithm is O(log n). Best performance can be O(1) and worst O(log n).
</b></details>

##### Code Review

<details>
<summary>What are your code-review best practices?</summary><br><b>
</b></details>

<details>
<summary>Do you agree/disagree with each of the following statements and why?:

  * The commit message is not important. When reviewing a change/patch one should focus on the actual change
  * You shouldn't test your code before submitting it. This is what CI/CD exists for.</summary><br><b>
</b></details>

#### Strings

<details>
<summary>In any language you want, write a function to determine if a given string is a palindrome</summary><br><b>
</b></details>

<details>
<summary>In any language you want, write a function to determine if two strings are Anagrams </summary><br><b>
</b></details>

#### Integers

<details>
<summary>In any language you would like, print the numbers from 1 to a given integer. For example for input: 5, the output is: 12345</summary><br><b>
</b></details>

#### Time Complexity

<details>
<summary>Describe what would be the time complexity of the operations <code>access</code>, <code>search</code> <code>insert</code> and <code>remove</code> for the following data structures:</summary><br><b>

  * Stack
  * Queue
  * Linked List
  * Binary Search Tree
</b></details>

<details>
<summary>What is the complexity for the best, worst and average cases of each of the following algorithms?:

  * Quick sort
  * Merge sort
  * Bucket Sort
  * Radix Sort</summary><br><b>
</b></details>

#### Data Structures & Types

<details>
<summary>Implement Stack in any language you would like</summary><br><b>
</b></details>

<details>
<summary>Tell me everything you know about Linked Lists</summary><br><b>

  * A linked list is a data structure
  * It consists of a collection of nodes. Together these nodes represent a sequence
  * Useful for use cases where you need to insert or remove an element from any position of the linked list
  * Some programming languages don't have linked lists as a built-in data type (like Python for example) but it can be easily implemented
</b></details>

<details>
<summary>Describe (no need to implement) how to detect a loop in a Linked List</summary><br><b>

There are multiple ways to detect a loop in a linked list. I'll mention three here:

Worst solution:<br>
Two pointers where one points to the head and one points to the last node. Each time you advance the last pointer by one and check whether the distance between head pointer to the moved pointer is bigger than the last time you measured the same distance (if not, you have a loop).<br>
The reason it's probably the worst solution, is because time complexity here is O(n^2)

Decent solution:<br>

Create an hash table and start traversing the linked list. Every time you move, check whether the node you moved to is in the hash table. If it isn't, insert it to the hash table. If you do find at any point the node in the hash table, it means you have a loop. When you reach None/Null, it's the end and you can return "no loop" value.
This one is very easy to implement (just create a hash table, update it and check whether the node is in the hash table every time you move to the next node) but since the auxiliary space is O(n) because you create a hash table then, it's not the best solution

Good solution:<br>
Instead of creating a hash table to document which nodes in the linked list you have visited, as in the previous solution, you can modify the Linked List (or the Node to be precise) to have a "visited" attribute. Every time you visit a node, you set "visited" to True.<br>
Time compleixty is O(n) and Auxiliary space is O(1), so it's a good solution but the only problem, is that you have to modify the Linked List.

Best solution:<br>
You set two pointers to traverse the linked list from the beginning. You move one pointer by one each time and the other pointer by two. If at any point they meet, you have a loop. This solution is also called "Floyd's Cycle-Finding"<br>
Time complexity is O(n) and auxiliary space is O(1). Perfect :)
</b></details>

<details>
<summary>Implement Hash table in any language you would like</summary><br><b>
</b></details>

<details>
<summary>What is Integer Overflow? How is it handled?</summary><br><b>
</b></details>

<details>
<summary>Name 3 design patterns. Do you know how to implement (= provide an example) these design pattern in any language you'll choose?</summary><br><b>
</b></details>

<details>
<summary>Given an array/list of integers, find 3 integers which are adding up to 0 (in any language you would like)</summary><br><b>

```
def find_triplets_sum_to_zero(li):
    li = sorted(li)
    for i, val in enumerate(li):
        low, up = 0, len(li)-1
        while low < i < up:
            tmp = var + li[low] + li[up]
            if tmp > 0:
                up -= 1
            elif tmp < 0:
                low += 1
            else:
                yield li[low], val, li[up]
                low += 1
                up -= 1
```
</b></details>

