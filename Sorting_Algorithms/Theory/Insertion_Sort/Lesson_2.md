# **<span style="color:#ff6b6b">Insertion Sort — Python Implementation</span>**

---

# **<span style="color:#4ecdc4">Core Idea Recap</span>**

Insertion Sort works like:

```text id="k1m8q4"
Taking one element
and inserting it into correct position
inside a sorted region
```

The algorithm maintains:

```text id="q7m2v5"
Left side → sorted
Right side → unsorted
```

After every pass:

```text id="x4q8m1"
Sorted region grows by one element
```

---

# **<span style="color:#ffd166">Python Implementation</span>**

```python id="4wdsay"
def insertion_sort(arr):

    n = len(arr)

    # Start from second element
    for i in range(1, n):

        # Element to insert
        key = arr[i]

        # Start comparing with previous element
        j = i - 1

        # Shift larger elements rightward
        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        # Insert key into correct position
        arr[j + 1] = key

    return arr
```

---

# **<span style="color:#a29bfe">Understanding the Control Flow</span>**

We will deeply understand:

```text id="p3m7q2"
✔ Outer loop
✔ key variable
✔ Inner while loop
✔ Shifting
✔ Final insertion
```

---

# **<span style="color:#00d2d3">1️⃣ Outer Loop</span>**

```python id="p6f1zq"
for i in range(1, n):
```

Purpose:

```text id="v8q2m5"
Pick next unsorted element
```

---

## Why start from index 1?

Because:

```text id="m2q8v4"
Single element is already sorted
```

Example:

```text id="t5m7q1"
[5]
```

needs no sorting.

---

# **<span style="color:#feca57">2️⃣ key Variable</span>**

```python id="c8pz1l"
key = arr[i]
```

Purpose:

```text id="u4q8m2"
Store current element safely
```

Very important.

Because during shifting:

```text id="y7m2q5"
Original value may get overwritten
```

---

# **<span style="color:#ff9f43">3️⃣ j Variable</span>**

```python id="q0rttk"
j = i - 1
```

Purpose:

```text id="n1q8m4"
Start comparing with previous sorted elements
```

---

# **<span style="color:#48dbfb">4️⃣ While Loop</span>**

```python id="kpu1qk"
while j >= 0 and arr[j] > key:
```

Purpose:

```text id="r6m7q2"
Find correct insertion position
```

This loop continues:

```text id="w3q8m1"
Until correct location found
```

---

# **<span style="color:#1dd1a1">5️⃣ Shifting Step</span>**

```python id="3mp74m"
arr[j + 1] = arr[j]
```

Purpose:

```text id="x8m2q4"
Move larger elements rightward
```

This creates empty space for insertion.

---

# **<span style="color:#ff6b6b">6️⃣ Insert Step</span>**

```python id="5k4f9y"
arr[j + 1] = key
```

Purpose:

```text id="p2q8m5"
Place element into correct sorted position
```

---

# **<span style="color:#4ecdc4">Complete Detailed Dry Run</span>**

Array:

```text id="g7m2q1"
[5, 2, 4, 6, 1, 3]
```

---

# **<span style="color:#ffd166">PASS 1 (i = 1)</span>**

Current array:

```text id="t4m8q7"
[5, 2, 4, 6, 1, 3]
```

---

## Step 1: Select key

```python id="2g9ncz"
key = 2
```

---

## Step 2: Initialize j

```python id="9qmu7w"
j = 0
```

Compare:

```text id="y1m7q4"
arr[0] = 5
```

---

## Step 3: While Condition

```text id="m5q8v2"
5 > 2 → TRUE
```

Shift:

```python id="ml8gmu"
arr[1] = arr[0]
```

Array becomes:

```text id="u8q2m1"
[5, 5, 4, 6, 1, 3]
```

Move left:

```python id="qhyqys"
j = -1
```

---

## Step 4: Exit While Loop

Because:

```text id="r3m7q5"
j < 0
```

---

## Step 5: Insert key

```python id="ip5g1u"
arr[j + 1] = key
```

Means:

```python id="pwqh4w"
arr[0] = 2
```

Final array:

```text id="f6q8m2"
[2, 5, 4, 6, 1, 3]
```

---

### Important Observation

Sorted region:

```text id="n2m7q4"
[2, 5]
```

---

# **<span style="color:#a29bfe">PASS 2 (i = 2)</span>**

Current array:

```text id="x5q8m1"
[2, 5, 4, 6, 1, 3]
```

---

## Select key

```python id="xjlwmj"
key = 4
```

---

## Initialize j

```python id="i9l5tu"
j = 1
```

---

## Compare 5 and 4

```text id="v8m2q7"
5 > 4 → shift
```

Array:

```text id="g1q8m4"
[2, 5, 5, 6, 1, 3]
```

Move left:

```python id="2ljj3o"
j = 0
```

---

## Compare 2 and 4

```text id="k4m7q2"
2 > 4 → FALSE
```

Stop shifting.

---

## Insert key

```python id="mjv4ux"
arr[j+1] = key
```

Means:

```python id="n0uz3k"
arr[1] = 4
```

Final array:

```text id="p7q8m5"
[2, 4, 5, 6, 1, 3]
```

---

# **<span style="color:#00d2d3">PASS 3 (i = 3)</span>**

Key:

```text id="y3m7q1"
6
```

Compare:

```text id="u6q8m4"
5 > 6 → FALSE
```

No shifting needed.

Array unchanged.

---

# **<span style="color:#feca57">PASS 4 (i = 4)</span>**

Current array:

```text id="q9m2v5"
[2, 4, 5, 6, 1, 3]
```

---

## Select key

```python id="nqkkf5"
key = 1
```

---

## Shift 6

Array:

```text id="w2q8m1"
[2, 4, 5, 6, 6, 3]
```

---

## Shift 5

```text id="m7q2v4"
[2, 4, 5, 5, 6, 3]
```

---

## Shift 4

```text id="t1m8q5"
[2, 4, 4, 5, 6, 3]
```

---

## Shift 2

```text id="f5q7m2"
[2, 2, 4, 5, 6, 3]
```

---

## Insert 1

Final array:

```text id="v8q2m4"
[1, 2, 4, 5, 6, 3]
```

---

# **<span style="color:#ff9f43">Internal Mechanics of Insertion Sort</span>**

Insertion Sort repeatedly performs:

---

# **<span style="color:#48dbfb">1️⃣ Select Next Element</span>**

```text id="g3m8q1"
Choose next unsorted value
```

---

# **<span style="color:#1dd1a1">2️⃣ Shift Larger Elements</span>**

Important:

```text id="k6q2m7"
Shifting preserves sorted order
```

---

# **<span style="color:#ff6b6b">3️⃣ Insert Correctly</span>**

Once correct position found:

```text id="r4m7q5"
Insert key
```

---

# **<span style="color:#4ecdc4">Why Shifting is Better Than Swapping</span>**

Bubble Sort repeatedly swaps:

```text id="u1q8m2"
many temporary exchanges
```

Insertion Sort:

```text id="x7m2q4"
moves blocks efficiently
```

This is why insertion sort performs better practically.

---

# **<span style="color:#ffd166">Time Complexity</span>**

Worst-case comparisons:

1+2+3+\dots+(n-1)

Result:

\frac{n(n-1)}{2}

Therefore:

```text id="n5q8m1"
O(n²)
```

---

# **<span style="color:#a29bfe">Best Case</span>**

Already sorted array:

```text id="w8m2q5"
Only one comparison per element
```

So:

```text id="j2q7m4"
O(n)
```

---

# **<span style="color:#00d2d3">Space Complexity</span>**

Only uses:

```text id="m6q8v1"
key + indices
```

Therefore:

```text id="t3m7q2"
O(1)
```

---

# **<span style="color:#ff6b6b">Final Mental Model</span>**

Insertion Sort behaves like:

```text id="p9q2m5"
Maintaining a continuously sorted hand of cards
```

Each new card:

```text id="v4m8q1"
slides into proper position
```

instead of repeatedly swapping randomly.

---

# **<span style="color:#1dd1a1">Key Insight</span>**

Insertion Sort is fundamentally:

```text id="y7q2m4"
incremental ordered insertion
```

It continuously preserves:

```text id="g1m8q7"
sorted structure
```

through intelligent shifting.
