# <span style="color:#fb8500">Subarray and Kadane’s Algorithm — First Principles Explanation</span>

---

## <span style="color:#ff006e">1. What is a Subarray? (First-Principles Understanding)</span>

### <span style="color:#8ecae6">1.1 Basic Definition</span>

A **subarray** is:

> A **contiguous sequence of elements** taken from an array.

If the original array is:

```
A = [a0, a1, a2, a3, ..., an]
```

A subarray is any sequence:

```
A[i], A[i+1], A[i+2], ..., A[j]
```

where:

```
0 ≤ i ≤ j < n
```

The key property is **contiguity** — the elements must appear **next to each other in the original array**.

---

### <span style="color:#8ecae6">1.2 Why Contiguity Matters</span>

Contiguity means we **cannot skip elements**.

Example:

```
Array: [1, 2, 3, 4]
```

Valid subarrays:

```
[1]
[2]
[3]
[4]
[1,2]
[2,3]
[3,4]
[1,2,3]
[2,3,4]
[1,2,3,4]
```

Invalid subarrays:

```
[1,3]
[1,4]
[2,4]
```

These are **subsequences**, not subarrays.

---

### <span style="color:#8ecae6">1.3 Total Number of Subarrays</span>

For an array of size **n**:

```
Total subarrays = n(n+1)/2
```

Reason:

- Choose start index `i`
- Choose end index `j ≥ i`

Example for `n = 4`:

```
4 * 5 / 2 = 10
```

This is why brute-force subarray problems often become **O(n²)**.

---

## <span style="color:#ff006e">2. The Core Problem Kadane’s Algorithm Solves</span>

The classic problem:

> **Find the maximum sum of any contiguous subarray.**

Example:

```
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

Best subarray:

```
[4, -1, 2, 1]
```

Maximum sum:

```
6
```

Brute force would check all:

```
O(n²) subarrays
```

Kadane solves it in:

```
O(n)
```

---

## <span style="color:#ff006e">3. First-Principles Idea Behind Kadane’s Algorithm</span>

The key insight:

> If a prefix of a subarray has a **negative sum**, keeping it will only **hurt future sums**.

Example:

```
prefix sum = -5
next element = 10

Keeping prefix:
-5 + 10 = 5

Dropping prefix:
10
```

Dropping is better.

Therefore:

> Whenever the running sum becomes negative, we **restart the subarray**.

---

## <span style="color:#ff006e">4. What Kadane’s Algorithm is Based On</span>

Kadane’s algorithm relies on **two invariants**.

### <span style="color:#8ecae6">Invariant 1 — Current Sum</span>

```
current_sum
```

Meaning:

> Maximum subarray sum **ending at index i**

---

### <span style="color:#8ecae6">Invariant 2 — Best Sum</span>

```
best_sum
```

Meaning:

> Maximum subarray sum **seen anywhere so far**

---

### <span style="color:#8ecae6">Relationship</span>

At each element:

```
current_sum = max(nums[i], current_sum + nums[i])
best_sum = max(best_sum, current_sum)
```

This maintains correctness for every prefix.

---

## <span style="color:#ff006e">5. Kadane Algorithm Pseudocode</span>

### <span style="color:#8ecae6">Pseudocode</span>

```
current_sum = nums[0]
best_sum = nums[0]

for i from 1 to n-1:
    current_sum = max(nums[i], current_sum + nums[i])
    best_sum = max(best_sum, current_sum)

return best_sum
```

Key decision:

```
extend previous subarray
or
start new subarray
```

---

## <span style="color:#ff006e">6. Dry Run of Kadane’s Algorithm</span>

Example:

```
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

| i   | value | current_sum   | best_sum |
| --- | ----- | ------------- | -------- |
| 0   | -2    | -2            | -2       |
| 1   | 1     | max(1,-1)=1   | 1        |
| 2   | -3    | max(-3,-2)=-2 | 1        |
| 3   | 4     | max(4,2)=4    | 4        |
| 4   | -1    | max(-1,3)=3   | 4        |
| 5   | 2     | max(2,5)=5    | 5        |
| 6   | 1     | max(1,6)=6    | 6        |
| 7   | -5    | max(-5,1)=1   | 6        |
| 8   | 4     | max(4,5)=5    | 6        |

Final answer:

```
6
```

Subarray:

```
[4,-1,2,1]
```

---

## <span style="color:#ff006e">7. How the Mechanism Works</span>

Kadane’s algorithm maintains:

```
best possible subarray ending at i
```

If extending the previous subarray **improves the sum**, continue.

Otherwise:

```
start new subarray
```

This ensures we never carry **harmful prefixes**.

---

## <span style="color:#ff006e">8. Problems Where Kadane’s Algorithm is Used</span>

Kadane appears in many variants.

---

### <span style="color:#8ecae6">Maximum Subarray (Classic)</span>

Problem:

Find the largest contiguous sum.

---

### <span style="color:#8ecae6">Maximum Product Subarray</span>

Variant where:

```
products instead of sums
```

Requires tracking both **max and min products**.

---

### <span style="color:#8ecae6">Maximum Circular Subarray</span>

Subarray may wrap around the array.

Solution combines:

```
Kadane + total_sum - minimum_subarray
```

---

### <span style="color:#8ecae6">2D Maximum Submatrix</span>

Kadane is applied row-wise to reduce a 2D problem to 1D.

---

## <span style="color:#ff006e">9. Constraints and Limitations</span>

### <span style="color:#8ecae6">Limitation 1 — Requires Contiguity</span>

Kadane works only when the problem requires **contiguous elements**.

---

### <span style="color:#8ecae6">Limitation 2 — Only Works for Additive Problems</span>

Kadane relies on:

```
prefix negativity property
```

This works for:

```
sums
```

But not directly for:

```
products
bit operations
non-linear scoring
```

---

### <span style="color:#8ecae6">Limitation 3 — Single Subarray</span>

Basic Kadane finds:

```
one maximum subarray
```

If the problem requires **k subarrays**, more advanced DP is required.

---

## <span style="color:#ff006e">10. Time and Space Complexity</span>

### <span style="color:#8ecae6">Time Complexity</span>

```
O(n)
```

Single pass through the array.

---

### <span style="color:#8ecae6">Space Complexity</span>

```
O(1)
```

Only two variables are maintained.

---

# <span style="color:#fb8500">Final First-Principle Insight</span>

Kadane’s algorithm works because:

> A negative prefix can never improve a future sum.

So the algorithm keeps only **useful history**, discarding everything else — allowing the optimal subarray to be found in **one linear scan**.
