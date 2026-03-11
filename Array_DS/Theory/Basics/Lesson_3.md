# **<span style="color:#fb8500">Static Arrays vs Dynamic Arrays — First-Principles, Internal Behavior & Time Complexity</span>**

---

## **<span style="color:#ff006e">1. First-Principle Motivation</span>**

Before definitions, ask **why two kinds exist**.

> Memory is **finite and rigid**, but programs need **flexible growth**.

This tension creates:

- **Static arrays** → predictable, rigid, fast
- **Dynamic arrays** → flexible, amortized efficiency

Both **use contiguous memory**.
The difference is **who manages resizing and when**.

---

## **<span style="color:#ff006e">2. Static Array — Internal Behavior</span>**

### <span style="color:#8ecae6">2.1 What Is a Static Array?</span>

A **static array**:

- Size fixed **at creation**
- Allocated **once**
- Never resized

Conceptually:

```
Allocate N × element_size bytes
Done.
```

---

### <span style="color:#8ecae6">2.2 Memory Allocation (Internal)</span>

Example:

```
int A[5]
```

Memory manager:

```
Requests 5 × 4 = 20 bytes (contiguous)
Returns base address (say 1000)
```

Memory:

```
1000 1004 1008 1012 1016
```

No metadata. No spare capacity.

---

### <span style="color:#8ecae6">2.3 Internal Data Model</span>

Static array stores:

```
Base address
Fixed length N
```

Nothing else.

---

### <span style="color:#8ecae6">2.4 Operation Behavior & Complexity</span>

| Operation       | Internal Logic        | Time |
| --------------- | --------------------- | ---- |
| Access          | Base + i × size       | O(1) |
| Write           | Direct overwrite      | O(1) |
| Traversal       | Loop N times          | O(n) |
| Insert (end)    | ❌ impossible if full | —    |
| Insert (middle) | Shift (if space)      | O(n) |
| Delete          | Shift left            | O(n) |

📌 **Key limitation**:

> If array is full → insertion is **impossible**

---

## **<span style="color:#ff006e">3. Dynamic Array — Internal Behavior</span>**

### <span style="color:#8ecae6">3.1 What Is a Dynamic Array?</span>

A **dynamic array**:

- Grows and shrinks automatically
- Still stores elements **contiguously**
- Uses **reallocation strategy**

Examples conceptually:

- vector (C++)
- ArrayList (Java)
- list (Python)

---

### <span style="color:#8ecae6">3.2 Internal Structure (Critical)</span>

A dynamic array maintains:

```
struct DynamicArray {
    pointer to data block
    size        // number of elements used
    capacity    // total allocated slots
}
```

Example:

```
size = 4
capacity = 8
```

Memory:

```
[10, 20, 30, 40, _, _, _, _]
```

---

### <span style="color:#8ecae6">3.3 Append Operation (Normal Case)</span>

Append when size < capacity:

```
A[size] = x
size++
```

Internal:

- No reallocation
- No shifting

🟢 **O(1)**

---

## **<span style="color:#ff006e">4. Dynamic Array Resize — Core Mechanism</span>**

### <span style="color:#8ecae6">4.1 What Triggers Resize?</span>

```
if size == capacity
    resize()
```

---

### <span style="color:#8ecae6">4.2 Resize Algorithm (Step-by-Step)</span>

Assume:

```
capacity = 4
size = 4
Append 50
```

#### Steps:

1. Allocate **new block** (usually 2× capacity)

   ```
   new_capacity = 8
   ```

2. Copy all elements to new block
3. Free old block
4. Update pointer
5. Insert new element

---

### <span style="color:#8ecae6">4.3 Dry Run</span>

Before:

```
[10, 20, 30, 40]
capacity = 4
```

After allocation:

```
[10, 20, 30, 40, _, _, _, _]
capacity = 8
```

Insert:

```
[10, 20, 30, 40, 50, _, _, _]
size = 5
```

---

### <span style="color:#8ecae6">4.4 Time Complexity of Resize</span>

- Copy n elements → **O(n)**

⚠️ Resize is **expensive but rare**

---

## **<span style="color:#ff006e">5. Amortized Time Complexity (Key Insight)</span>**

### <span style="color:#8ecae6">Why Append Is Amortized O(1)</span>

If capacity doubles:

- Total cost of copying over many appends is linear
- Spread across operations → constant per append

Example:

```
Total moves ≈ 1 + 2 + 4 + 8 + ... + n = O(n)
Total appends = n
Cost per append = O(1)
```

---

## **<span style="color:#ff006e">6. Operation-wise Comparison</span>**

| Operation       | Static Array  | Dynamic Array  |
| --------------- | ------------- | -------------- |
| Access          | O(1)          | O(1)           |
| Write           | O(1)          | O(1)           |
| Traversal       | O(n)          | O(n)           |
| Append          | O(1) if space | Amortized O(1) |
| Insert (middle) | O(n)          | O(n)           |
| Delete          | O(n)          | O(n)           |
| Resize          | ❌            | O(n) (rare)    |

---

## **<span style="color:#ff006e">7. Why Dynamic Arrays Are Still “Arrays”</span>**

Important clarification:

> A dynamic array is **not a linked list**

Why?

- Elements still stored **contiguously**
- Index → address formula still holds

Resize simply **rebuilds a new array**.

---

## **<span style="color:#ff006e">8. Memory Trade-offs</span>**

### <span style="color:#8ecae6">Static Array</span>

✔ No overhead
✔ Cache-friendly
❌ Wasted or insufficient memory

---

### <span style="color:#8ecae6">Dynamic Array</span>

✔ Flexible growth
✔ Efficient average performance
❌ Extra memory (unused capacity)
❌ Occasional expensive resize

---

## **<span style="color:#ff006e">9. One-Line First-Principle Summary</span>**

> Static arrays trade flexibility for predictability, while dynamic arrays trade occasional expensive resizing for amortized constant-time growth — both preserving contiguous memory and O(1) access.

---
