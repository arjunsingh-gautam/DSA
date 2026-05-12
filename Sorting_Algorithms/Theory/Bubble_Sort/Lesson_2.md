# **<span style="color:#ff6b6b">Bubble Sort Implementations</span>**

We will study:

```text id="4k8x9a"
1️⃣ Unoptimized Bubble Sort
2️⃣ Optimized Bubble Sort
```

And deeply understand:

```text id="v3n8k2"
✔ Control flow
✔ Inner mechanics
✔ Why optimization works
✔ Dry runs step-by-step
```

---

# **<span style="color:#4ecdc4">1. Unoptimized Bubble Sort</span>**

---

## **🔹 Python Implementation**

```python
def bubble_sort(arr):
    n = len(arr)

    # Outer loop → number of passes
    for i in range(n):

        # Inner loop → comparisons
        for j in range(0, n - i - 1):

            # Swap if wrong order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
```

---

# **<span style="color:#ffd166">Understanding the Control Flow</span>**

---

## **Outer Loop**

```python
for i in range(n):
```

Purpose:

```text id="3y0k4p"
Controls passes
```

Each pass:

```text id="1x0n7f"
Places one largest element
at its final position
```

---

## **Inner Loop**

```python
for j in range(0, n - i - 1):
```

Purpose:

```text id="h9s2p1"
Performs adjacent comparisons
```

---

## **Why n - i - 1 ?**

Because after every pass:

```text id="p8m2e5"
Last i elements are already sorted
```

No need to compare them again.

---

# **<span style="color:#a29bfe">Detailed Dry Run (Unoptimized)</span>**

Array:

```text id="q3w9m2"
[5, 1, 4, 2]
```

---

# **<span style="color:#00d2d3">PASS 1 (i = 0)</span>**

Inner loop:

```text id="k7c1v8"
j = 0 → 2
```

---

## Step 1

Compare:

```text id="f4s2x7"
5 and 1
```

Condition:

```text id="y1n8d2"
5 > 1 → swap
```

Array becomes:

```text id="w6q3l0"
[1, 5, 4, 2]
```

---

## Step 2

Compare:

```text id="e8m2p4"
5 and 4
```

Swap:

```text id="u3k7n1"
[1, 4, 5, 2]
```

---

## Step 3

Compare:

```text id="t9v1x6"
5 and 2
```

Swap:

```text id="g2p8y4"
[1, 4, 2, 5]
```

---

### Important Observation

```text id="j6s3q9"
Largest element 5 reached final position
```

---

# **<span style="color:#feca57">PASS 2 (i = 1)</span>**

Array:

```text id="d1k7w3"
[1, 4, 2, 5]
```

Inner loop:

```text id="z7m2n5"
j = 0 → 1
```

---

## Step 1

Compare:

```text id="m5q1v8"
1 and 4
```

No swap.

---

## Step 2

Compare:

```text id="r8x2k4"
4 and 2
```

Swap:

```text id="c6n3y1"
[1, 2, 4, 5]
```

---

### Important Observation

```text id="b9s4p7"
Second largest element 4 fixed
```

---

# **<span style="color:#ff9f43">PASS 3 (i = 2)</span>**

Array already sorted:

```text id="h4m8x2"
[1, 2, 4, 5]
```

But algorithm still performs comparisons.

This is inefficiency of unoptimized version.

---

# **<span style="color:#48dbfb">Problem with Unoptimized Bubble Sort</span>**

Even if array becomes sorted early:

```text id="x2n7q4"
Algorithm continues unnecessary passes
```

This wastes time.

---

# **<span style="color:#1dd1a1">2. Optimized Bubble Sort</span>**

---

## **🔹 Python Implementation**

```python
def optimized_bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        # If no swaps happened
        # array is already sorted
        if not swapped:
            break

    return arr
```

---

# **<span style="color:#ff6b6b">Understanding the Optimization</span>**

---

## **The Key Variable**

```python
swapped = False
```

Purpose:

```text id="y8m4q2"
Track whether any swap occurred
```

---

## **If Swap Happens**

```python
swapped = True
```

Meaning:

```text id="t1v9k6"
Array was not fully sorted
```

---

## **If No Swap Happens**

```python
if not swapped:
    break
```

Meaning:

```text id="p7n3x5"
Array already sorted
```

So stop immediately.

---

# **<span style="color:#4ecdc4">Detailed Dry Run (Optimized)</span>**

Example:

```text id="m2q7w4"
[1, 2, 3, 4]
```

Already sorted.

---

# **<span style="color:#ffd166">PASS 1</span>**

---

## Compare 1 and 2

No swap.

---

## Compare 2 and 3

No swap.

---

## Compare 3 and 4

No swap.

---

### End of Pass

```python
swapped == False
```

So:

```python
break
```

Algorithm terminates immediately.

---

# **<span style="color:#a29bfe">Why Optimization Improves Complexity</span>**

Without optimization:

```text id="f3x8k2"
Always performs O(n²) comparisons
```

With optimization:

```text id="u9m2q5"
Can stop early
```

Best case becomes:

```text id="r1v7n4"
O(n)
```

---

# **<span style="color:#00d2d3">Step-by-Step Mechanics Internally</span>**

Bubble sort repeatedly performs:

---

## **1️⃣ Adjacent Comparison**

```python
arr[j] > arr[j+1]
```

This identifies:

```text id="z7x2m8"
Local disorder
```

---

## **2️⃣ Swap**

```python
arr[j], arr[j+1] = arr[j+1], arr[j]
```

This fixes:

```text id="n4q8v1"
One inversion
```

---

## **3️⃣ Repeated Passes**

Repeated local corrections eventually create:

```text id="h2m7x9"
Global sorted order
```

---

# **<span style="color:#feca57">Visualization of Bubble Movement</span>**

Example:

```text id="g5n1q4"
[5, 1, 4, 2, 8]
```

Largest element movement:

```text id="b8v3k7"
5 → moves right
```

Pass-by-pass:

```text id="p4m2x6"
[5,1,4,2,8]
[1,5,4,2,8]
[1,4,5,2,8]
[1,4,2,5,8]
```

👉 Large element slowly drifts rightward.

---

# **<span style="color:#ff9f43">Time Complexity Analysis</span>**

---

## **Worst Case**

Reverse sorted:

```text id="k2m7n4"
[5,4,3,2,1]
```

Comparisons:

(n-1)+(n-2)+(n-3)+\dots+1

Result:

\frac{n(n-1)}{2}

Complexity:

```text id="s7q1v9"
O(n²)
```

---

## **Best Case (Optimized)**

Already sorted:

```text id="x1m4q8"
Only one pass needed
```

Complexity:

```text id="j6v2n7"
O(n)
```

---

# **<span style="color:#48dbfb">Space Complexity</span>**

Only temporary variable for swapping.

So:

```text id="m3q7x1"
O(1)
```

---

# **<span style="color:#1dd1a1">Final Mental Model</span>**

Bubble sort behaves like:

```text id="n8v2q4"
Repeatedly fixing neighboring mistakes
```

Each pass guarantees:

```text id="z5m1x7"
One element reaches permanent correct position
```

The optimized version adds intelligence:

```text id="u4q9n2"
"Stop if no mistakes remain"
```

---

# **<span style="color:#ff6b6b">Key Insight</span>**

Bubble sort is fundamentally a:

```text id="f7m2v8"
local correction algorithm
```

It only fixes:

```text id="r2q6x1"
adjacent disorder
```

That is why it is simple but slow.
