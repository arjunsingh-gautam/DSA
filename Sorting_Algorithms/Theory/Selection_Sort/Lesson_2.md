# **<span style="color:#ff6b6b">Selection Sort — Python Implementation</span>**

---

# **<span style="color:#4ecdc4">Core Idea Recap</span>**

Selection Sort repeatedly:

```text id="e1v8m3"
1️⃣ Finds the minimum element
2️⃣ Places it into correct position
```

After every pass:

```text id="q7m2x5"
Left side becomes permanently sorted
```

---

# **<span style="color:#ffd166">Python Implementation</span>**

```python
def selection_sort(arr):
    n = len(arr)

    # Outer loop controls passes
    for i in range(n):

        # Assume current position has minimum
        min_index = i

        # Search remaining unsorted array
        for j in range(i + 1, n):

            # Update minimum index
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap minimum element into correct position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
```

---

# **<span style="color:#a29bfe">Understanding the Control Flow</span>**

---

# **<span style="color:#00d2d3">1️⃣ Outer Loop</span>**

```python
for i in range(n):
```

Purpose:

```text id="u8m2q5"
Controls which position should be fixed next
```

Example:

```text id="n4q7m1"
i = 0 → place smallest element
i = 1 → place second smallest
```

---

# **<span style="color:#feca57">2️⃣ min_index Variable</span>**

```python
min_index = i
```

Meaning:

```text id="g5m8q2"
Assume current element is minimum initially
```

---

# **<span style="color:#ff9f43">3️⃣ Inner Loop</span>**

```python
for j in range(i + 1, n):
```

Purpose:

```text id="x2m7q4"
Search remaining unsorted region
```

---

# **<span style="color:#48dbfb">4️⃣ Comparison</span>**

```python
if arr[j] < arr[min_index]:
```

Purpose:

```text id="b8q1m5"
Find actual minimum element
```

---

# **<span style="color:#1dd1a1">5️⃣ Swap Step</span>**

```python
arr[i], arr[min_index] = arr[min_index], arr[i]
```

Purpose:

```text id="t4m7q2"
Place minimum element into correct position
```

---

# **<span style="color:#ff6b6b">Complete Detailed Dry Run</span>**

Array:

```text id="y8m2q1"
[29, 10, 14, 37, 13]
```

---

# **<span style="color:#4ecdc4">PASS 1 (i = 0)</span>**

Goal:

```text id="p2m7q5"
Find smallest element for index 0
```

---

## Initial

```python
min_index = 0
```

Current minimum:

```text id="v5q1m8"
29
```

---

## Compare arr[1] = 10

```text id="g7m2q4"
10 < 29 → YES
```

Update:

```python
min_index = 1
```

---

## Compare arr[2] = 14

```text id="n1q8m3"
14 < 10 → NO
```

---

## Compare arr[3] = 37

```text id="f4m7q2"
37 < 10 → NO
```

---

## Compare arr[4] = 13

```text id="r8q2m5"
13 < 10 → NO
```

---

## End of Inner Loop

Minimum element found:

```text id="k3m7q1"
10 at index 1
```

---

## Swap

```python
arr[0], arr[1] = arr[1], arr[0]
```

Array becomes:

```text id="w6q2m8"
[10, 29, 14, 37, 13]
```

---

### Important Observation

```text id="x4m7q9"
10 permanently fixed
```

Sorted region:

```text id="t7q1m4"
[10]
```

---

# **<span style="color:#ffd166">PASS 2 (i = 1)</span>**

Current array:

```text id="z2m8q5"
[10, 29, 14, 37, 13]
```

Goal:

```text id="h5q1m7"
Find second smallest element
```

---

## Initial

```python
min_index = 1
```

Minimum:

```text id="p8m2q4"
29
```

---

## Compare 14

```text id="y3q7m1"
14 < 29 → YES
```

Update:

```python
min_index = 2
```

---

## Compare 37

```text id="c6m8q2"
37 < 14 → NO
```

---

## Compare 13

```text id="n9q2m5"
13 < 14 → YES
```

Update:

```python
min_index = 4
```

---

## Swap

```python
arr[1], arr[4] = arr[4], arr[1]
```

Array:

```text id="g1m7q4"
[10, 13, 14, 37, 29]
```

---

### Important Observation

Sorted region grows:

```text id="k8q2m7"
[10, 13]
```

---

# **<span style="color:#a29bfe">PASS 3 (i = 2)</span>**

Current array:

```text id="w2m8q5"
[10, 13, 14, 37, 29]
```

Minimum already:

```text id="t5q1m8"
14
```

No meaningful swap.

---

# **<span style="color:#00d2d3">PASS 4 (i = 3)</span>**

Compare:

```text id="v7m2q4"
37 and 29
```

Update minimum:

```python
min_index = 4
```

Swap:

```text id="b4q8m1"
37 ↔ 29
```

Array:

```text id="r1m7q5"
[10, 13, 14, 29, 37]
```

---

# **<span style="color:#feca57">Final Sorted Array</span>**

```text id="j8q2m4"
[10, 13, 14, 29, 37]
```

---

# **<span style="color:#ff9f43">Step-by-Step Internal Mechanics</span>**

Selection Sort repeatedly performs:

---

## **1️⃣ Scan Entire Unsorted Region**

Purpose:

```text id="u3m7q9"
Find global minimum
```

---

## **2️⃣ Track Best Candidate**

Using:

```python
min_index
```

---

## **3️⃣ Perform One Final Swap**

This is important.

Unlike Bubble Sort:

```text id="x6q2m5"
Selection Sort delays swapping
```

Until correct minimum found.

---

# **<span style="color:#48dbfb">Why Selection Sort Uses Fewer Swaps</span>**

Bubble Sort:

```text id="q9m1v7"
Swaps repeatedly during comparisons
```

Selection Sort:

```text id="k2q8m4"
Only one swap per pass
```

Maximum swaps:

```text id="f5m7q1"
n - 1
```

Very efficient when swapping expensive.

---

# **<span style="color:#1dd1a1">Time Complexity</span>**

Comparisons:

(n-1)+(n-2)+(n-3)+\dots+1

Result:

\frac{n(n-1)}{2}

Therefore:

```text id="m4q8v2"
O(n²)
```

---

# **<span style="color:#ff6b6b">Space Complexity</span>**

Only:

```text id="n7m2q5"
min_index + temporary swap variable
```

So:

```text id="z1q8m4"
O(1)
```

---

# **<span style="color:#4ecdc4">Final Mental Model</span>**

Selection Sort behaves like:

```text id="g6m7q2"
Repeatedly selecting the best candidate
for the next correct position
```

It grows a:

```text id="w9q2m1"
sorted region from left to right
```

---

# **<span style="color:#ff6b6b">Key Insight</span>**

Selection Sort optimizes:

```text id="v3m8q5"
movement cost (few swaps)
```

But not:

```text id="t1q7m4"
search cost (still scans everything)
```

That is why:

```text id="h8m2q7"
few swaps
but still O(n²)
```
