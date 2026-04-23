# <span style="color:#2E86C1"><b> Types of Linked Lists — Complete Guide (SLL, CSLL, DLL, CDLL)</b></span>

This is a **core DSA concept**. Interviewers expect you to not just define these, but also understand:

- Structure
- Operations
- Trade-offs
- Real-world usage

Let’s go step by step.

---

# <span style="color:#117A65"><b>1. Singly Linked List (SLL)</b></span>

## <span style="color:#5D6D7E"><b>Definition</b></span>

A linked list where each node points to the **next node only**.

```
[Data | Next] → [Data | Next] → NULL
```

---

## <span style="color:#5D6D7E"><b>Components</b></span>

Each node contains:

```cpp
struct Node {
    int data;
    Node* next;
};
```

- `data` → value
- `next` → pointer to next node

---

## <span style="color:#5D6D7E"><b>Operations</b></span>

| Operation         | Time |
| ----------------- | ---- |
| Insertion at head | O(1) |
| Insertion at tail | O(n) |
| Deletion          | O(n) |
| Search            | O(n) |
| Traversal         | O(n) |

---

## <span style="color:#5D6D7E"><b>Pros</b></span>

- Dynamic size
- Efficient insertion at head
- Less memory (only 1 pointer)

---

## <span style="color:#5D6D7E"><b>Constraints / Cons</b></span>

- Cannot traverse backward
- Slow access (no indexing)
- Tail operations costly

---

## <span style="color:#5D6D7E"><b>Use Cases</b></span>

- Implementing stacks
- Simple data streams
- Memory-efficient lists

---

# <span style="color:#117A65"><b>2. Circular Singly Linked List (CSLL)</b></span>

## <span style="color:#5D6D7E"><b>Definition</b></span>

Last node points back to **head**, forming a circle.

```
[Data] → [Data] → [Data]
   ↑                     ↓
   ← ← ← ← ← ← ← ← ← ← ←
```

---

## <span style="color:#5D6D7E"><b>Components</b></span>

Same as SLL:

```cpp
struct Node {
    int data;
    Node* next;
};
```

But:

```cpp
last->next = head;
```

---

## <span style="color:#5D6D7E"><b>Operations</b></span>

| Operation         | Time                      |
| ----------------- | ------------------------- |
| Insertion at head | O(1)                      |
| Insertion at tail | O(1) (if tail maintained) |
| Traversal         | O(n)                      |
| Deletion          | O(n)                      |

---

## <span style="color:#5D6D7E"><b>Pros</b></span>

- No NULL pointers
- Can start traversal from any node
- Efficient cyclic operations

---

## <span style="color:#5D6D7E"><b>Constraints / Cons</b></span>

- Risk of infinite loop
- Harder to debug
- Slightly complex logic

---

## <span style="color:#5D6D7E"><b>Use Cases</b></span>

- Round-robin scheduling
- Multiplayer games turn system
- Circular buffers

---

# <span style="color:#117A65"><b>3. Doubly Linked List (DLL)</b></span>

## <span style="color:#5D6D7E"><b>Definition</b></span>

Each node points to both:

- Previous node
- Next node

```
NULL ← [Prev | Data | Next] ⇄ [Prev | Data | Next] → NULL
```

---

## <span style="color:#5D6D7E"><b>Components</b></span>

```cpp
struct Node {
    int data;
    Node* prev;
    Node* next;
};
```

---

## <span style="color:#5D6D7E"><b>Operations</b></span>

| Operation | Time                 |
| --------- | -------------------- |
| Insertion | O(1)                 |
| Deletion  | O(1) (if node known) |
| Traversal | O(n)                 |
| Search    | O(n)                 |

---

## <span style="color:#5D6D7E"><b>Pros</b></span>

- Bidirectional traversal
- Easier deletion
- More flexible

---

## <span style="color:#5D6D7E"><b>Constraints / Cons</b></span>

- Extra memory (2 pointers)
- More pointer handling
- Higher complexity

---

## <span style="color:#5D6D7E"><b>Use Cases</b></span>

- Browser history
- Undo/Redo systems
- Navigation systems

---

# <span style="color:#117A65"><b>4. Circular Doubly Linked List (CDLL)</b></span>

## <span style="color:#5D6D7E"><b>Definition</b></span>

Combination of:

- Circular
- Doubly

```
   ← ← ← ← ← ← ← ← ← ←
  ↓                   ↑
[Prev | Data | Next] ⇄ [Prev | Data | Next]
```

- Last → head
- Head → last

---

## <span style="color:#5D6D7E"><b>Components</b></span>

```cpp
struct Node {
    int data;
    Node* prev;
    Node* next;
};
```

With:

```cpp
head->prev = tail;
tail->next = head;
```

---

## <span style="color:#5D6D7E"><b>Operations</b></span>

| Operation | Time |
| --------- | ---- |
| Insertion | O(1) |
| Deletion  | O(1) |
| Traversal | O(n) |

---

## <span style="color:#5D6D7E"><b>Pros</b></span>

- Full bidirectional traversal
- No NULL pointers
- Efficient rotations

---

## <span style="color:#5D6D7E"><b>Constraints / Cons</b></span>

- Most complex implementation
- High memory usage
- Debugging is difficult

---

## <span style="color:#5D6D7E"><b>Use Cases</b></span>

- Advanced scheduling systems
- Music playlist looping
- Cache systems

---

# <span style="color:#922B21"><b>5. Comparative Study</b></span>

| Feature            | SLL     | CSLL             | DLL     | CDLL             |
| ------------------ | ------- | ---------------- | ------- | ---------------- |
| Traversal          | One-way | One-way circular | Two-way | Two-way circular |
| Memory             | Low     | Low              | High    | Highest          |
| Insertion          | Easy    | Easy             | Easy    | Easy             |
| Deletion           | Hard    | Hard             | Easy    | Easy             |
| Backward traversal | No      | No               | Yes     | Yes              |
| Complexity         | Simple  | Medium           | Medium  | Complex          |

---

# <span style="color:#6C3483"><b>6. When to Use What (Interview Insight)</b></span>

### Use **SLL**

- When memory is critical
- Simple operations

---

### Use **CSLL**

- When repetition/cycles needed
- Round-robin tasks

---

### Use **DLL**

- When frequent deletion
- Need backward traversal

---

### Use **CDLL**

- When both cyclic + bidirectional needed
- Complex systems

---

# <span style="color:#1F618D"><b>7. Key Interview Takeaways</b></span>

- SLL → minimal memory
- DLL → flexible operations
- Circular → no NULL, cyclic traversal
- Trade-off → **memory vs flexibility**

---

If you want, I can next give you:

- **C++ implementation of all 4 types (clean + interview ready)**
- **Top 10 linked list problems asked in FAANG**
- **Patterns like fast-slow pointer, reversal, cycle detection**
