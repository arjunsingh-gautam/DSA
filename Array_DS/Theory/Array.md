# <span style="color:yellow">**Array Data Structure**</span>

## 1. **What is an Array Data Structure?**

An **array** is a collection of elements (values), stored at **contiguous memory locations**, and accessed using an **index**.

- Each element in an array is of the same data type.
- Indexing is usually **0-based** (first element is at index 0).
- Direct/constant-time access: (O(1)).

👉 Think of it like a **row of lockers** numbered 0, 1, 2, … where each locker stores one element.

---

## 2. **Uses of Arrays**

- **Fast random access** → you can directly access any element if you know its index.
- **Storing lists of items**: numbers, strings, objects, etc.
- Used in implementing:

  - **Vectors & matrices**
  - **Dynamic programming tables**
  - **Heaps / priority queues**
  - **Hash tables (backing storage)**

- Basis of **string storage** (strings are arrays of characters).

---

## 3. **Implementation of Arrays in Python**

Python doesn’t have _low-level fixed arrays_ like C, but provides:

- **List** → a _dynamic array_ under the hood (resizable).
- **array module** → supports fixed-type arrays (`array('i', [1,2,3])`).

Example:

```python
# Using Python list
arr = [10, 20, 30, 40]

# Access element
print(arr[2])   # 30

# Update element
arr[1] = 25
print(arr)      # [10, 25, 30, 40]
```

---

## 4. **What is a Dynamic Array?**

- A **dynamic array** automatically grows/shrinks when elements are added or removed.
- Python lists behave like **dynamic arrays**.

👉 How it works internally:

1. Start with a small fixed-size array.
2. When full, create a new array with **double capacity**, copy old elements into it, and then add new element.

   - Amortized **append** cost = (O(1)).

Example (simulate growth):

```python
import sys

arr = []
for i in range(10):
    arr.append(i)
    print(i, sys.getsizeof(arr))  # watch memory size grow
```

---

## 5. **Operations on Arrays (with Python examples)**

| Operation              | Time Complexity         | Example in Python        |
| ---------------------- | ----------------------- | ------------------------ |
| **Access by index**    | (O(1))                  | `arr[3]`                 |
| **Update**             | (O(1))                  | `arr[2] = 50`            |
| **Traversal**          | (O(n))                  | `for x in arr: print(x)` |
| **Insertion (end)**    | Amortized (O(1))        | `arr.append(99)`         |
| **Insertion (middle)** | (O(n)) (shift elements) | `arr.insert(2, 15)`      |
| **Deletion (end)**     | (O(1))                  | `arr.pop()`              |
| **Deletion (middle)**  | (O(n))                  | `arr.pop(2)`             |

---

### Example: All operations

```python
arr = [1, 2, 3, 4, 5]

# Access
print("3rd element:", arr[2])

# Update
arr[2] = 99
print("After update:", arr)

# Insert at end
arr.append(6)
print("After append:", arr)

# Insert at index 2
arr.insert(2, 50)
print("After insert:", arr)

# Delete last
arr.pop()
print("After pop:", arr)

# Delete at index 1
arr.pop(1)
print("After removing index 1:", arr)

# Traverse
for i in arr:
    print(i, end=" ")
```

---

## 🔑 Quick Recap:

- Array = contiguous memory, fast access by index.
- Python lists = dynamic arrays.
- Key operations: access, insert, delete, traverse.
- Insert/delete in middle = slow ((O(n))), append = fast ((O(1)) amortized).

---
