# <span style="color:#fb8500">Prefix Sum — First Principles, Mechanism, and Algorithm Design</span>

---

## <span style="color:#ff006e">1. What is a Prefix Sum? (First-Principles Definition)</span>

A **prefix sum** represents the **cumulative sum of elements from the beginning of an array up to a given index**.

For an array:

```
A = [a0, a1, a2, a3, ..., an]
```

The prefix sum array **P** is defined as:

```
P[i] = a0 + a1 + a2 + ... + ai
```

So:

```
P[0] = a0
P[1] = a0 + a1
P[2] = a0 + a1 + a2
...
```

---

### <span style="color:#8ecae6">Example</span>

Array:

```
A = [3, 1, 4, 2, 5]
```

Prefix sum array:

```
P = [3, 4, 8, 10, 15]
```

Meaning:

```
P[2] = 3 + 1 + 4 = 8
```

Prefix sums **compress the history of the array into cumulative totals**.

---

## <span style="color:#ff006e">2. How Prefix Sum Works (Core Mechanism)</span>

Prefix sums rely on this key identity:

```
sum(i, j) = P[j] - P[i-1]
```

Where:

```
sum(i, j) = ai + ai+1 + ... + aj
```

Example:

```
A = [3,1,4,2,5]
P = [3,4,8,10,15]
```

Find:

```
sum(2,4)
```

Compute:

```
P[4] - P[1] = 15 - 4 = 11
```

Which equals:

```
4 + 2 + 5 = 11
```

---

### <span style="color:#8ecae6">Why This Works</span>

Because:

```
P[j] = a0 + a1 + ... + aj
P[i-1] = a0 + a1 + ... + a(i-1)
```

Subtracting removes the earlier prefix.

---

## <span style="color:#ff006e">3. Why Prefix Sum is Powerful</span>

Without prefix sums:

```
Range sum query → O(n)
```

With prefix sums:

```
Range sum query → O(1)
```

Example:

If we must answer **10⁶ range queries**, brute force would be extremely slow.

Prefix sums shift work from:

```
many repeated calculations
```

to

```
one preprocessing step
```

---

## <span style="color:#ff006e">4. When Prefix Sum Works</span>

Prefix sums work when:

### <span style="color:#8ecae6">1. The operation is associative</span>

Meaning:

```
(a + b) + c = a + (b + c)
```

Examples:

```
sum
count
frequency
XOR
```

---

### <span style="color:#8ecae6">2. Range queries depend on cumulative aggregation</span>

Example:

```
sum(i,j)
count(i,j)
XOR(i,j)
```

---

### <span style="color:#8ecae6">3. The array is mostly static</span>

Prefix sums assume:

```
data does not change frequently
```

If values change often, recomputing prefix sums becomes expensive.

---

## <span style="color:#ff006e">5. When Prefix Sum Breaks</span>

Prefix sums fail when operations **cannot be reversed by subtraction**.

---

### <span style="color:#8ecae6">Example: Maximum Element</span>

If:

```
P[i] = max(a0...ai)
```

Then:

```
max(i,j) ≠ P[j] - P[i-1]
```

Because max is **not invertible**.

---

### <span style="color:#8ecae6">Example: Product with Zeros</span>

Products break if zeros appear:

```
P[j] / P[i-1]
```

Division by zero becomes undefined.

---

### <span style="color:#8ecae6">Example: Non-associative operations</span>

Operations like:

```
median
mode
sorting
```

cannot use prefix sums.

---

## <span style="color:#ff006e">6. Using Prefix Sum in Algorithm Design</span>

The design pattern is:

1. Precompute prefix sums
2. Convert repeated range operations into constant-time calculations

---

### <span style="color:#8ecae6">Algorithm Pattern</span>

```
build prefix array

for each query:
    answer = P[r] - P[l-1]
```

---

## <span style="color:#ff006e">7. Example Problem</span>

### Problem

Find the sum of every subarray of length **k**.

Example:

```
nums = [2,4,1,3,5]
k = 3
```

---

### Step 1: Build Prefix Sum

```
P = [2,6,7,10,15]
```

---

### Step 2: Compute subarray sums

Subarray `[0..2]`

```
sum = P[2] = 7
```

Subarray `[1..3]`

```
P[3] - P[0] = 10 - 2 = 8
```

Subarray `[2..4]`

```
P[4] - P[1] = 15 - 6 = 9
```

---

### Result

```
[7,8,9]
```

---

## <span style="color:#ff006e">8. Dry Run Visualization</span>

Array:

```
[2,4,1,3,5]
```

Prefix sums:

```
[2,6,7,10,15]
```

Range `[1..4]`

```
15 - 2 = 13
```

Which equals:

```
4 + 1 + 3 + 5
```

---

## <span style="color:#ff006e">9. Constraints and Limitations</span>

### <span style="color:#8ecae6">Memory Overhead</span>

Requires extra array:

```
O(n)
```

---

### <span style="color:#8ecae6">Updates are expensive</span>

If element changes:

```
A[i] = new value
```

All prefix sums after `i` must be recomputed.

---

### <span style="color:#8ecae6">Doesn't work for dynamic arrays</span>

Better structures for dynamic data:

```
Fenwick Tree
Segment Tree
```

---

## <span style="color:#ff006e">10. Types of Problems Prefix Sum Solves</span>

### <span style="color:#8ecae6">Range Sum Queries</span>

Example:

```
sum(i,j)
```

---

### <span style="color:#8ecae6">Subarray Sum Problems</span>

Example:

```
subarray sum = k
```

---

### <span style="color:#8ecae6">Counting Problems</span>

Example:

```
number of subarrays with sum k
```

---

### <span style="color:#8ecae6">Difference Array Problems</span>

Efficient range updates.

---

### <span style="color:#8ecae6">2D Matrix Sum Queries</span>

Prefix sums extend to matrices.

Example:

```
sum of rectangle in matrix
```

---

## <span style="color:#ff006e">11. When to Use Prefix Sum (Checklist)</span>

Use prefix sum if:

- Many **range queries**
- Data is **static**
- Operation is **associative**
- Operation can be **reversed using subtraction**

---

Avoid prefix sum if:

- Frequent updates
- Non-invertible operations
- Need ordering statistics

---

# <span style="color:#fb8500">Final First-Principle Insight</span>

Prefix sums work because they **store the history of the array in cumulative form**, allowing any subarray query to be answered by **subtracting two historical checkpoints** instead of recomputing the entire range.
