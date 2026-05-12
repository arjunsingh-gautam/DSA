# **<span style="color:#ff6b6b">Selection Sort — Complete Deep Dive</span>**

Selection Sort is a simple sorting algorithm based on one powerful idea:

```text id="w1m9q3"
Repeatedly select the correct element
and place it into its final position
```

Unlike Bubble Sort:

```text id="x7n2k5"
Selection Sort does NOT repeatedly swap neighbors
```

Instead:

```text id="u4v8m1"
It finds the minimum element
and places it correctly
```

---

# **<span style="color:#4ecdc4">Simple Mental Model</span>**

Imagine:

```text id="f8q2m7"
Students standing randomly
```

You want to arrange them by height.

Selection Sort works like:

```text id="k3v1n9"
1️⃣ Find shortest student
2️⃣ Put them at first position

3️⃣ Find second shortest
4️⃣ Put them at second position

...
```

It builds the sorted portion:

```text id="n7x4q2"
one correct element at a time
```

---

# **<span style="color:#ffd166">Core Idea of Selection Sort</span>**

Suppose array:

```text id="z5m2q8"
[29, 10, 14, 37, 13]
```

Selection Sort:

```text id="r4v7n1"
✔ Find minimum element
✔ Swap it with first unsorted position
✔ Repeat for remaining array
```

---

# **<span style="color:#a29bfe">Core Invariant</span>**

After every pass:

```text id="m8q3x6"
Left portion of array becomes permanently sorted
```

Example:

```text id="d2v7n4"
| Sorted | Unsorted |
```

The sorted region grows:

```text id="f1q8m3"
left → right
```

---

# **<span style="color:#00d2d3">Complete Control Flow</span>**

Selection Sort uses:

```text id="g7m2v5"
1️⃣ Outer loop → controls current position
2️⃣ Inner loop → finds minimum element
3️⃣ Swap → places minimum correctly
```

---

# **<span style="color:#feca57">Language Agnostic Pseudocode</span>**

```text id="n9x4q7"
FOR i = 0 to n-1

    min_index = i

    FOR j = i+1 to n-1

        IF arr[j] < arr[min_index]

            min_index = j

    SWAP arr[i], arr[min_index]
```

---

# **<span style="color:#ff9f43">Understanding Each Step Deeply</span>**

---

# **<span style="color:#48dbfb">1️⃣ Outer Loop</span>**

```text id="u2m8q4"
FOR i = 0 to n-1
```

Purpose:

```text id="h5v1n7"
Choose position where correct element should go
```

Example:

```text id="y8q3m2"
i = 0 → find smallest element
i = 1 → find second smallest
```

---

# **<span style="color:#1dd1a1">2️⃣ min_index Variable</span>**

```text id="q7v2m5"
min_index = i
```

Purpose:

```text id="f4n8q1"
Tracks smallest element found so far
```

---

# **<span style="color:#ff6b6b">3️⃣ Inner Loop</span>**

```text id="x3m7v9"
FOR j = i+1 to n-1
```

Purpose:

```text id="t1q5m8"
Search remaining unsorted region
```

---

# **<span style="color:#4ecdc4">4️⃣ Comparison Step</span>**

```text id="k9v2m4"
IF arr[j] < arr[min_index]
```

Purpose:

```text id="r5m8q2"
Update smallest element
```

---

# **<span style="color:#ffd166">5️⃣ Swap Step</span>**

After inner loop finishes:

```text id="g2q7m1"
Swap minimum into correct position
```

This is the key operation.

---

# **<span style="color:#a29bfe">Detailed Dry Run</span>**

Array:

```text id="b4m9q7"
[29, 10, 14, 37, 13]
```

---

# **<span style="color:#00d2d3">PASS 1 (i = 0)</span>**

Goal:

```text id="p8v2m5"
Find smallest element
```

---

## Initial

```text id="n3q7m1"
min_index = 0 → value = 29
```

---

## Compare 10 and 29

```text id="m7v1q4"
10 < 29
```

Update:

```text id="x2m8q5"
min_index = 1
```

---

## Compare 14 and 10

```text id="v5q2m9"
14 > 10
```

No update.

---

## Compare 37 and 10

No update.

---

## Compare 13 and 10

No update.

---

## End of Pass

Minimum found:

```text id="u1m7q3"
10
```

Swap:

```text id="w9q2m4"
29 ↔ 10
```

Array:

```text id="f6m8q1"
[10, 29, 14, 37, 13]
```

---

### Important Observation

```text id="z4q7m2"
10 permanently fixed
```

---

# **<span style="color:#feca57">PASS 2 (i = 1)</span>**

Unsorted region:

```text id="g8m2q4"
[29, 14, 37, 13]
```

---

## Find minimum

Compare:

```text id="j3q7m9"
14 < 29 → min_index = 2
13 < 14 → min_index = 4
```

---

## Swap

```text id="t5m1q8"
29 ↔ 13
```

Array:

```text id="k7q2m4"
[10, 13, 14, 37, 29]
```

---

# **<span style="color:#ff9f43">PASS 3</span>**

Find minimum in:

```text id="r1m8q5"
[14, 37, 29]
```

Minimum already:

```text id="n6q2m7"
14
```

No meaningful swap.

---

# **<span style="color:#48dbfb">Final Sorted Array</span>**

```text id="y3m7q2"
[10, 13, 14, 29, 37]
```

---

# **<span style="color:#1dd1a1">Which Operations Contribute to Complexity?</span>**

---

# **<span style="color:#ff6b6b">1️⃣ Comparisons (Main Cost)</span>**

Selection Sort always scans remaining array.

Comparisons:

```text id="p4q8m1"
(n-1) + (n-2) + (n-3) + ...
```

Total:

\frac{n(n-1)}{2}

Therefore:

```text id="v2m7q5"
O(n²)
```

---

# **<span style="color:#4ecdc4">2️⃣ Swaps</span>**

Very important property:

```text id="g5q1m8"
Only ONE swap per pass
```

Maximum swaps:

```text id="k8m2q7"
n - 1
```

This is much smaller than Bubble Sort.

---

# **<span style="color:#ffd166">3️⃣ Extra Memory</span>**

Only uses:

```text id="u7q3m9"
min_index variable
```

So:

```text id="w1m8q4"
O(1)
```

---

# **<span style="color:#a29bfe">Constraints of Selection Sort</span>**

---

## **❌ O(n²) Comparisons**

Bad for large datasets.

---

## **❌ Not Adaptive**

Even sorted array still performs:

```text id="q3m7v2"
same number of comparisons
```

---

## **❌ Poor Performance in Practice**

Advanced algorithms outperform it heavily.

---

## **❌ Not Stable (Normally)**

Swapping can change order of equal elements.

---

# **<span style="color:#00d2d3">Advantages of Selection Sort</span>**

---

## **✔ Very Simple**

Easy to implement.

---

## **✔ Few Swaps**

Very important.

Useful when:

```text id="h9m2q5"
Swapping is expensive
```

Example:

```text id="b7q1m8"
EEPROM memory
Flash storage
```

---

## **✔ In-Place**

No extra memory.

---

## **✔ Predictable Performance**

Always:

```text id="y2m7q4"
O(n²)
```

regardless of input.

---

# **<span style="color:#feca57">Time Complexity Analysis</span>**

---

## **Worst Case**

Comparisons:

(n-1)+(n-2)+(n-3)+\dots+1

Result:

\frac{n(n-1)}{2}

Complexity:

```text id="c5q8m1"
O(n²)
```

---

## **Best Case**

Still scans entire array.

So:

```text id="n1m7q4"
O(n²)
```

---

## **Average Case**

```text id="v7q2m5"
O(n²)
```

---

# **<span style="color:#ff9f43">Space Complexity</span>**

Only temporary variables.

So:

```text id="g4m8q2"
O(1)
```

---

# **<span style="color:#48dbfb">Bubble Sort vs Selection Sort</span>**

| Feature        | Bubble Sort            | Selection Sort         |
| -------------- | ---------------------- | ---------------------- |
| Core Idea      | Swap adjacent elements | Select minimum element |
| Swaps          | Many swaps             | Few swaps              |
| Comparisons    | O(n²)                  | O(n²)                  |
| Stability      | Stable                 | Usually unstable       |
| Adaptive       | Yes (optimized)        | No                     |
| Best Case      | O(n)                   | O(n²)                  |
| Movement Style | Local movement         | Direct placement       |

---

# **<span style="color:#1dd1a1">Deep Intuition Difference</span>**

---

## **Bubble Sort**

Works like:

```text id="z8m2q4"
Repeatedly fixing local disorder
```

Elements move slowly.

---

## **Selection Sort**

Works like:

```text id="w5q1m7"
Finding exact correct element
and placing it directly
```

Much fewer swaps.

---

# **<span style="color:#ff6b6b">Final Mental Model</span>**

Selection Sort behaves like:

```text id="q2m7v5"
Repeatedly selecting the best candidate
for the next correct position
```

Each pass grows the sorted region:

```text id="f8q3m1"
left → right
```

---

# **<span style="color:#ffd166">Key Insight</span>**

Selection Sort reduces:

```text id="g1m8q7"
movement cost
```

but NOT:

```text id="v4q2m9"
comparison cost
```

That is why:

```text id="y7m1q5"
few swaps
but still O(n²)
```
