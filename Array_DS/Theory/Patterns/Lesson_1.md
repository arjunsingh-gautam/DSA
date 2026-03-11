# **<span style="color:#fb8500"> Array Traversal in Python — Linear Scan from First Principles</span>**

---

## **<span style="color:#ff006e">1. What Is Array Traversal (First Principle)</span>**

**Array traversal** means:

> Visiting elements of an array **one-by-one in index order**, using the array’s core property:
> **contiguous memory + index-based access**

In Python, this applies to `list` (dynamic array).

Key invariant during traversal:

```
At step i → we have seen elements [0 ... i]
```

Traversal is the **foundation of almost all array algorithms**.

---

## **<span style="color:#ff006e">2. Linear Scan — What It Is and Why It Exists</span>**

### <span style="color:#8ecae6">2.1 Definition</span>

A **linear scan** is:

> A traversal where each element is visited **exactly once**, in increasing index order.

Formally:

```
i = 0 → n-1
process(arr[i])
```

---

### <span style="color:#8ecae6">2.2 Why Linear Scan Works</span>

Because arrays guarantee:

- O(1) index access
- Ordered memory layout

This allows:

- Deterministic iteration
- Predictable performance

---

### <span style="color:#8ecae6">2.3 Time & Space Complexity</span>

- Time: **O(n)**
- Extra space: **O(1)** (if no auxiliary structures)

---

## **<span style="color:#ff006e">3. Implementing Linear Scan in Python</span>**

### <span style="color:#8ecae6">3.1 Index-Based Scan (Most Fundamental)</span>

```python
arr = [10, 20, 30, 40]

for i in range(len(arr)):
    print(arr[i])
```

**What happens internally**:

1. `i` starts at 0
2. Address of `arr[i]` computed
3. Element fetched
4. `i` increments

---

### <span style="color:#8ecae6">3.2 Value-Based Scan (Syntactic Sugar)</span>

```python
for x in arr:
    print(x)
```

Internally:

- Python still uses index-based pointer traversal
- Behavior remains linear

---

## **<span style="color:#ff006e">4. What Is a Single Pass?</span>**

### <span style="color:#8ecae6">4.1 Definition</span>

A **single pass** algorithm:

> Processes the array using **one linear scan**, without restarting or nested traversal.

Formally:

```
One loop → i = 0 to n-1
```

---

### <span style="color:#8ecae6">4.2 Why Single Pass Is Powerful</span>

- Optimal time complexity (O(n))
- Minimal memory usage
- Scales well

Many “hard” problems are actually:

> **single-pass + correct state**

---

## **<span style="color:#ff006e">5. Maintain State — The Core Skill</span>**

### <span style="color:#8ecae6">5.1 What Is State?</span>

**State** is:

> Information accumulated from previously seen elements that affects future decisions.

Examples:

- current sum
- maximum so far
- last seen index
- count
- window boundaries

---

### <span style="color:#8ecae6">5.2 Why State Is Necessary</span>

Arrays don’t remember past values for you.

If you want to know:

- best so far
- pattern till now
- constraints over prefix

➡️ You must maintain it explicitly.

---

## **<span style="color:#ff006e">6. Example: Maintain Running State (Sum)</span>**

```python
arr = [3, 1, 4]

running_sum = 0

for i in range(len(arr)):
    running_sum += arr[i]
    print(running_sum)
```

State:

```
Before iteration i → sum of [0 ... i-1]
After iteration i  → sum of [0 ... i]
```

---

## **<span style="color:#ff006e">7. Compare Current vs Best — Core Pattern</span>**

This pattern appears in:

- max / min problems
- subarray problems
- greedy algorithms

---

### <span style="color:#8ecae6">7.1 What Does “Current” Mean?</span>

**Current**:

> Value derived using element at index `i`

Example:

- current element
- current sum ending at `i`
- current window size

---

### <span style="color:#8ecae6">7.2 What Does “Best” Mean?</span>

**Best**:

> Optimal value observed **so far** (from indices `0 ... i-1`)

---

### <span style="color:#8ecae6">7.3 The Core Rule</span>

At each step:

```
best = max(best, current)
```

This ensures:

> Best always represents optimal solution over prefix.

---

## **<span style="color:#ff006e">8. Classic Example: Maximum Element</span>**

```python
arr = [7, 2, 9, 4]

best = arr[0]

for i in range(1, len(arr)):
    current = arr[i]
    best = max(best, current)

print(best)
```

### Dry Run

| i   | current | best |
| --- | ------- | ---- |
| 1   | 2       | 7    |
| 2   | 9       | 9    |
| 3   | 4       | 9    |

---

## **<span style="color:#ff006e">9. More Advanced Example: Maximum Subarray (Kadane Intuition)</span>**

```python
arr = [-2, 1, -3, 4]

current_sum = arr[0]
best_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    best_sum = max(best_sum, current_sum)

print(best_sum)
```

State meaning:

- `current_sum` → best subarray ending at `i`
- `best_sum` → best subarray seen overall

---

## **<span style="color:#ff006e">10. Why Compare Current vs Best Always Works</span>**

Because:

- Array traversal is ordered
- Past decisions cannot change
- Only current extension matters

This transforms:

> exponential choices → linear scan

---

## **<span style="color:#ff006e">11. Mental Template (Memorize This)</span>**

When traversing arrays:

```
initialize state
initialize best

for each element:
    update state using current
    compare state vs best
    update best
```

This template solves **70% of array problems**.

---

## **<span style="color:#ff006e">12. Common Mistakes</span>**

❌ Recomputing from scratch
❌ Nested loops when single pass suffices
❌ Forgetting to initialize state correctly
❌ Updating best before updating current

---

## **<span style="color:#ff006e">13. Final First-Principle Takeaway</span>**

> Array traversal is not about looping — it’s about accumulating information in state while making optimal decisions at each step using current vs best comparison.

---
