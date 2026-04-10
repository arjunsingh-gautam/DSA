# **<span style="color:#7aa2f7">Linked List – Concept, Properties, Behavior, and Implementation</span>**

A **Linked List** is a linear data structure where elements are stored in **separate memory locations** and connected using **links (pointers/references)**.

Unlike arrays, the elements are **not stored in contiguous memory**. Each element knows **where the next element is located**, forming a chain.

---

# **<span style="color:#9ece6a">1. What is a Linked List</span>**

A **linked list** is a collection of nodes where each node contains:

1. **Data** – the value stored in the node
2. **Reference (pointer)** – the address of the next node

Structure of a node:

```
[data | next]
```

Example list:

```
10 → 20 → 30 → 40 → None
```

Each element **points to the next element**, and the last node points to **None** indicating the end of the list.

---

# **<span style="color:#9ece6a">2. Essential Properties of a Linked List</span>**

These characteristics define a true linked list.

### **Dynamic Memory Allocation**

Nodes are created **when needed**. The list can grow or shrink dynamically.

---

### **Non-Contiguous Memory**

Nodes may exist anywhere in memory.

Example:

```
Node1 → memory location 2000
Node2 → memory location 4500
Node3 → memory location 1020
```

The nodes are connected through **references**, not memory adjacency.

---

### **Sequential Access**

You **cannot jump directly** to an element.

To reach element `k`, you must traverse:

```
Head → Node1 → Node2 → ... → Node k
```

Access complexity:

```
O(n)
```

---

### **Pointer Based Structure**

Nodes are connected through references:

```
current_node.next
```

This link is what makes the structure a **linked list**.

---

### **Dynamic Size**

Size changes through insertion or deletion.

Unlike arrays, no resizing or shifting of memory blocks is needed.

---

# **<span style="color:#9ece6a">3. Behavior of a Linked List</span>**

The linked list behaves differently from arrays.

### **Insertion**

Insertion only requires **changing references**.

Example:

Insert `15` between `10` and `20`.

Before:

```
10 → 20
```

After:

```
10 → 15 → 20
```

Operations required:

```
new.next = node10.next
node10.next = new
```

Time complexity:

```
O(1)  (if position known)
```

---

### **Deletion**

Deleting a node simply reconnects links.

Before:

```
10 → 20 → 30
```

Delete `20`.

After:

```
10 → 30
```

Operations:

```
node10.next = node20.next
```

---

### **Traversal**

Since nodes are not indexed, traversal must follow links:

```
current = head
while current:
    process(current.data)
    current = current.next
```

Time complexity:

```
O(n)
```

---

# **<span style="color:#9ece6a">4. Linked List Analogy</span>**

Imagine a **treasure hunt game**.

Each clue contains:

- A message (data)
- The location of the next clue

Example:

```
Clue1 → "Go to the library"
Clue2 → "Check the desk"
Clue3 → "Look under the chair"
```

You cannot jump directly to clue 3.

You must follow the chain:

```
Clue1 → Clue2 → Clue3
```

Similarly in linked lists:

```
Node1 → Node2 → Node3
```

Each node only knows **where the next node is located**.

---

# **<span style="color:#9ece6a">5. Components of a Linked List</span>**

A linked list contains three main components.

---

## **Node**

A **node** is the fundamental building block.

Structure:

```
Node
 ├── data
 └── next
```

Example:

```
[data = 10 | next = address_of_next_node]
```

---

## **Head Pointer**

The **head** stores the reference to the first node.

Example:

```
head → 10 → 20 → 30 → None
```

If the list is empty:

```
head = None
```

---

## **Links (References)**

Each node stores a pointer to the next node.

```
node.next
```

This link connects the entire structure.

---

# **<span style="color:#9ece6a">6. How a Linked List Works Internally</span>**

Example list:

```
head → 5 → 10 → 15 → None
```

Memory representation:

```
Address     Data    Next
1000        5       2500
2500        10      4300
4300        15      None
```

Execution flow:

```
head → address 1000
1000.next → 2500
2500.next → 4300
4300.next → None
```

Traversal follows these pointers step by step.

---

# **<span style="color:#9ece6a">7. Use Cases of Linked Lists</span>**

Linked lists are useful when **frequent insertions or deletions** occur.

---

## **Memory Efficient Dynamic Structures**

Dynamic data structures often rely on linked lists:

- Stacks
- Queues
- Graph adjacency lists

---

## **Undo / Redo Systems**

Applications store operations sequentially.

Example:

```
State1 → State2 → State3
```

---

## **Hash Tables (Chaining)**

Collision handling:

```
index → linked list of keys
```

---

## **Operating Systems**

Used in:

- Process scheduling
- Memory allocation
- Free memory lists

---

## **Graph Representation**

Adjacency list representation:

```
1 → 2 → 4
2 → 3
3 → 1
```

Each vertex stores a linked list of neighbors.

---

# **<span style="color:#9ece6a">8. Naive Linked List Implementation in Python</span>**

### **Step 1 – Create Node Class**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Each node contains:

```
data
next pointer
```

---

### **Step 2 – Create Linked List Class**

```python
class LinkedList:

    def __init__(self):
        self.head = None
```

Initially the list is empty.

---

### **Step 3 – Insert at End**

```python
def insert(self, data):

    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        return

    current = self.head

    while current.next:
        current = current.next

    current.next = new_node
```

Steps:

1. Create new node
2. Traverse to last node
3. Update last node's next pointer

---

### **Step 4 – Traverse Linked List**

```python
def display(self):

    current = self.head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")
```

---

### **Step 5 – Complete Example**

```python
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def insert(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node


    def display(self):

        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)

ll.display()
```

Output:

```
10 -> 20 -> 30 -> None
```

---

# **<span style="color:#7aa2f7">Key Takeaways</span>**

A linked list:

- Stores elements in **nodes**
- Uses **references to connect nodes**
- Supports **efficient insertion and deletion**
- Has **sequential access**
- Is the foundation for many complex data structures

---

If you want, I can also explain:

1. **Why linked lists exist even though arrays exist**
2. **Types of linked lists (Singly, Doubly, Circular)**
3. **Complete linked list implementation with all operations**
4. **How linked lists are used inside real systems like Linux kernel and databases**.
