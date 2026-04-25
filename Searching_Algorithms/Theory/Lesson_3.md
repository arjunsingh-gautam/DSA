# **<span style="color:#ff6b6b">Binary Search — Complete Deep Dive</span>**

Binary Search is one of the most powerful searching algorithms.

It works on a simple idea:

```text
"Eliminate half of the search space every step"
```

---

# **<span style="color:#4ecdc4">1. Complete Binary Search Algorithm</span>**

### **Core Idea**

```text
1️⃣ Find middle element
2️⃣ Compare with target
3️⃣ If equal → return
4️⃣ If target < mid → search left half
5️⃣ If target > mid → search right half
```

---

### **Algorithm Steps**

```text
1️⃣ low = 0, high = n - 1

2️⃣ While low ≤ high:
      mid = (low + high) // 2

      if arr[mid] == target:
          return mid

      elif target < arr[mid]:
          high = mid - 1

      else:
          low = mid + 1

3️⃣ Return -1 (not found)
```

---

# **<span style="color:#ffd166">2. Where It Works and Where It Doesn't</span>**

## **✔ Works Well When**

```text
✔ Data is sorted
✔ Random access is available (arrays)
✔ Large datasets
```

👉 Because:

```text
You can eliminate half of data each step
```

---

## **❌ Doesn't Work When**

```text
❌ Data is unsorted
❌ Data is changing frequently
❌ No random access (linked list)
```

👉 Why?

```text
Binary search depends on ordering + index access
```

---

# **<span style="color:#a29bfe">3. When to Use vs When NOT to Use</span>**

## **✔ Use Binary Search When**

```text
✔ Sorted array/list
✔ Static data
✔ Large input size
✔ Need fast lookup (log n)
```

---

## **❌ Avoid Binary Search When**

```text
❌ Unsorted data → sorting overhead
❌ Small data → linear is simpler
❌ Linked list → no direct access
```

---

# **<span style="color:#00d2d3">4. Input Data Structures</span>**

## **✔ Works On**

```text
✔ Arrays
✔ Python lists
✔ Sorted vectors
✔ Monotonic functions (search space problems)
```

---

## **❌ Not Suitable For**

```text
❌ Linked Lists (O(n) access)
❌ Unordered structures (sets without order)
❌ Streams (no fixed bounds)
```

---

# **<span style="color:#feca57">5. Python Implementation</span>**

### **Iterative Version (Most Important)**

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2   # safe mid

        if arr[mid] == target:
            return mid

        elif target < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1

    return -1
```

---

### **Recursive Version**

```python
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_recursive(arr, low, mid - 1, target)
    else:
        return binary_search_recursive(arr, mid + 1, high, target)
```

---

# **<span style="color:#ff9f43">6. Dry Run (Step-by-Step)</span>**

### Example:

```text
arr = [2, 5, 8, 12, 16, 23, 38]
target = 16
```

---

### Step 1:

```text
low = 0, high = 6
mid = 3 → arr[3] = 12
```

👉 16 > 12 → search right

```text
low = 4
```

---

### Step 2:

```text
low = 4, high = 6
mid = 5 → arr[5] = 23
```

👉 16 < 23 → search left

```text
high = 4
```

---

### Step 3:

```text
low = 4, high = 4
mid = 4 → arr[4] = 16 ✅
```

Return index:

```text
4
```

---

# **<span style="color:#48dbfb">7. Constraints & Overheads</span>**

## **Constraints**

```text
✔ Data MUST be sorted
✔ Requires random access
✔ Boundaries must be known
```

---

## **Overheads**

```text
❌ Sorting cost → O(n log n)
❌ Maintaining sorted order
❌ Harder implementation than linear search
```

---

# **<span style="color:#1dd1a1">8. Advantages</span>**

```text
✔ Very fast → O(log n)
✔ Scales to huge datasets
✔ Basis of many advanced algorithms
✔ Used in search space problems
```

---

# **<span style="color:#ff6b6b">9. Time & Space Analysis</span>**

## **Time Complexity**

| Case    | Complexity |
| ------- | ---------- |
| Best    | O(1)       |
| Average | O(log n)   |
| Worst   | O(log n)   |

---

### **Why O(log n)?**

Each step:

```text
Search space is halved
```

Example:

```text
n → n/2 → n/4 → n/8 → ... → 1
```

---

## **Space Complexity**

```text
Iterative → O(1)
Recursive → O(log n) (call stack)
```

---

# **<span style="color:#4ecdc4">Final Mental Model</span>**

Think of binary search like:

```text
Searching a word in a dictionary
→ Open middle page
→ Decide left or right
→ Repeat
```

---

# **<span style="color:#ff6b6b">Key Insight</span>**

Binary search is not just an algorithm — it's a **pattern**:

```text
"If you can eliminate half the search space → use binary search"
```

---

# **<span style="color:#ffd166">Advanced Insight (Interview Level)</span>**

Binary search is also used in:

```text
✔ Search on answer (e.g., minimum max value)
✔ Peak finding
✔ Rotated arrays
✔ Infinite arrays
✔ Monotonic functions
```

---

If you want next, I can:

- Show **Binary Search patterns (most important for interviews)**
- Compare **Linear vs Binary deeply**
- Give **edge-case traps interviewers test (very important)**
