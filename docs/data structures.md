## Data Structure 

A data structure is a way of organizing and storing data efficiently. It determines how data is accessed, modified, and managed in a program.
The data is manipulated with abstraction, you dont know how is implement behind 


The data is manipulated through abstraction, meaning you don't need to know the underlying implementation details.
Abstraction is important because it hides the complexities of data manipulation, allowing developers to focus on high-level problem-solving rather than low-level implementation details. These structures are also called **Abstract Data Type (ADT)** because the basic data types are arrays, integers, floats. 


### Python Native 

### **Common Abstract Data Structures:**  
| **ADS**  | **Description** | **Possible Implementations** |
|----------|----------------|------------------------------|
| **List** | Ordered collection of elements | Array, Linked List |
| **Stack** | Last-In-First-Out (LIFO) | Array, Linked List |
| **Queue** | First-In-First-Out (FIFO) | Linked List, Circular Array |
| **Deque** | Double-ended queue | Doubly Linked List, Circular Array |
| **Set** | Unordered unique elements | Hash Table, Binary Search Tree |
| **Dictionary (Map)** | Key-value pairs | Hash Table, Tree Map |

1. List (Ordered, Mutable, Allows Duplicates)

```python
fruits = ["apple", "banana", "cherry", "apple"]
print("List Example:", fruits)
fruits.append("orange")  # Adding an element
print("After Append:", fruits)
```

2. Tuple (Ordered, Immutable, Allows Duplicates)

```python
numbers = (1, 2, 3, 4, 1)
print("Tuple Example:", numbers)
# numbers[0] = 10  # This would raise an error because tuples are immutable
```

3. Stack (LIFO - Last In, First Out)
A stack is a linear data structure where elements are added and removed from the same end (called the top). It follows the LIFO principle.

```python
stack = []  
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print("Stack:", stack)

stack.pop()  # Pop
print("After Pop:", stack)
```
Use Cases: Undo operations, backtracking (e.g., browser history).

4. Queue (FIFO - First In, First Out)
A queue is a linear data structure where elements are added at the rear and removed from the front. It follows the FIFO principle.


```python

from queue import Queue

queue = Queue()

# Enqueue
queue.put("X")
queue.put("Y")
queue.put("Z")

# Dequeue
print("Dequeued:", queue.get())  
print("Dequeued:", queue.get())

```
Use Cases: Task scheduling, printer queue, handling requests.

5. Deque (Double-Ended Queue)
A deque is a generalization of a queue where elements can be added or removed from both ends efficiently.


```python
from collections import deque

deque_obj = deque()
deque_obj.append(1)  # Add to rear
deque_obj.appendleft(2)  # Add to front
print("Deque:", deque_obj)

deque_obj.pop()  # Remove from rear
deque_obj.popleft()  # Remove from front
print("After Operations:", deque_obj)
```
Use Cases: Browser history (forward & backward navigation), sliding window problems.


6. Set (Unordered, Mutable, No Duplicates)


```python
unique_numbers = {1, 2, 3, 4, 1}
print("Set Example:", unique_numbers)
unique_numbers.add(5)
print("After Adding 5:", unique_numbers)
```

7. Dictionary (Key-Value Pairs, Unordered, Mutable, No Duplicate Keys)

```python
student = {"name": "Alice", "age": 22, "major": "Computer Science"}
print("Dictionary Example:", student)
student["age"] = 23  # Updating a value
print("After Updating Age:", student)
```

## Algorithms

