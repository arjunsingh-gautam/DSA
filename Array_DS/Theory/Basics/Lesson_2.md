# **<span style="color:#fb8500"> Array Basic Operations — Internal Logic, Dry Runs & Time Complexity</span>**

---

## **<span style="color:#ff006e">Pre-requisite Mental Model (Very Important)</span>**

Assume:

```
Array A of size n = 5
Element size = 4 bytes
Base address = 1000
```

```
Index:   0     1     2     3     4
Value:  10    20    30    40    50
Addr: 1000  1004  1008  1012  1016
```

**Address formula (core invariant):**

```
Address(A[i]) = Base + i × Size
```

This invariant drives **all operations**.

---

## **<span style="color:#ff006e">1. Access (Random Access)</span>**

### <span style="color:#8ecae6">What does “access” mean?</span>

Access means:

> **Fetch the element at a given index without modifying it**

```
x = A[3]
```

---

### <span style="color:#8ecae6">Internal Logic</span>

1. Compute address:

   ```
   Address = 1000 + (3 × 4) = 1012
   ```

2. CPU directly jumps to 1012
3. Reads value `40`

No loops. No traversal.

---

### <span style="color:#8ecae6">Dry Run</span>

```
Input index = 3
Base = 1000
Size = 4

→ Address = 1000 + 12 = 1012
→ Value = 40
```

---

### <span style="color:#8ecae6">Time Complexity</span>

- Best = Worst = Average = **O(1)**

📌 **Reason:** Address computation is constant time.

---

## **<span style="color:#ff006e">2. Read vs Write (Very Important Distinction)</span>**

### <span style="color:#8ecae6">Read</span>

```
value = A[i]
```

- Reads value
- No memory change

### <span style="color:#8ecae6">Write</span>

```
A[i] = new_value
```

- Overwrites value
- Memory content changes

⚠️ Both use the **same address computation**

---

## **<span style="color:#ff006e"> 3. Write / Update Operation</span>**

### <span style="color:#8ecae6">Operation</span>

```
A[2] = 99
```

---

### <span style="color:#8ecae6">Internal Logic</span>

1. Compute address:

   ```
   1000 + (2 × 4) = 1008
   ```

2. Overwrite old value (30) with 99

---

### <span style="color:#8ecae6">Dry Run</span>

Before:

```
[10, 20, 30, 40, 50]
```

After:

```
[10, 20, 99, 40, 50]
```

---

### <span style="color:#8ecae6">Time Complexity</span>

- **O(1)**

📌 No shifting or traversal.

---

## **<span style="color:#ff006e">4. Traversal</span>**

### <span style="color:#8ecae6">What is Traversal?</span>

Traversal means:

> **Visiting every element exactly once**

```
for i = 0 to n-1
    process A[i]
```

---

### <span style="color:#8ecae6">Internal Logic</span>

1. Start at index 0
2. Access element
3. Increment index
4. Repeat until end

Each access is O(1), but repeated **n times**.

---

### <span style="color:#8ecae6">Dry Run</span>

```
i = 0 → 10
i = 1 → 20
i = 2 → 30
i = 3 → 40
i = 4 → 50
```

---

### <span style="color:#8ecae6">Time Complexity</span>

- **O(n)**

📌 Because **n constant-time operations**

---

## **<span style="color:#ff006e">5. Insertion Operation</span>**

Insertion depends on **where**.

---

### <span style="color:#8ecae6">Case 1: Insert at End (Append-like)</span>

```
A = [10, 20, 30]
Insert 40
```

---

#### Internal Logic

1. Use index `n`
2. Store value
3. Increase size

---

#### Dry Run

```
Index 3 → store 40
```

```
[10, 20, 30, 40]
```

---

#### Time Complexity

- **O(1)** (if space exists)

---

### <span style="color:#8ecae6">Case 2: Insert at Middle</span>

Insert `25` at index `2`

Before:

```
[10, 20, 30, 40]
```

---

#### Internal Logic (Key Insight)

To preserve contiguity:

1. Shift elements **right**
2. Free index
3. Insert value

---

#### Dry Run (Step-by-Step)

```
Initial:
[10, 20, 30, 40, _]

Shift:
index 3 → 4 : 40
index 2 → 3 : 30

Insert:
A[2] = 25
```

Final:

```
[10, 20, 25, 30, 40]
```

---

#### Time Complexity

- **O(n)** (worst case: insert at start)

📌 Shifting dominates cost.

---

## **<span style="color:#ff006e">6. Deletion Operation</span>**

### <span style="color:#8ecae6">Delete at Index i</span>

Delete element at index `1`

Before:

```
[10, 20, 30, 40]
```

---

### <span style="color:#8ecae6">Internal Logic</span>

1. Overwrite target by shifting left
2. Reduce logical size

---

### <span style="color:#8ecae6">Dry Run</span>

```
Shift:
index 2 → 1 : 30
index 3 → 2 : 40
```

After:

```
[10, 30, 40, _]
```

---

### <span style="color:#8ecae6">Time Complexity</span>

- **O(n)**

📌 Shifting required to maintain contiguity.

---

## **<span style="color:#ff006e">7. Append (Special Case of Insertion)</span>**

### <span style="color:#8ecae6">What is Append?</span>

Append means:

> **Insert element at the end**

```
A[n] = x
```

---

### <span style="color:#8ecae6">Internal Logic</span>

- No shifting
- Direct write

---

### <span style="color:#8ecae6">Dry Run</span>

```
[10, 20, 30]
Append 40
→ [10, 20, 30, 40]
```

---

### <span style="color:#8ecae6">Time Complexity</span>

- **O(1)** (fixed array with free space)

⚠️ In **dynamic arrays**, occasional resize causes:

- Rare **O(n)**
- Amortized **O(1)**

---

## **<span style="color:#ff006e"> 8. Summary Table (Truth Table)</span>**

| Operation       | Core Action         | Time Complexity |
| --------------- | ------------------- | --------------- |
| Access          | Address computation | O(1)            |
| Read            | Fetch value         | O(1)            |
| Write           | Overwrite value     | O(1)            |
| Traversal       | Visit all           | O(n)            |
| Insert (end)    | Direct write        | O(1)            |
| Insert (middle) | Shift right         | O(n)            |
| Delete          | Shift left          | O(n)            |
| Append          | Write at n          | O(1)            |

---

## **<span style="color:#ff006e">9. One Golden Rule (Never Forget)</span>**

> **Arrays are fast for access, slow for structural changes**

Because:

- Access = math
- Insert/Delete = movement

---
