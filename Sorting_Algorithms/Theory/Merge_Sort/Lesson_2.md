# **<span style="color:#ff6b6b">Merge Sort — Python Implementation</span>**

---

# **<span style="color:#4ecdc4">Core Idea Recap</span>**

Merge Sort works in two phases:

```text id="t4m8q1"
1️⃣ Divide recursively
2️⃣ Merge sorted pieces
```

The algorithm does NOT directly sort.

Instead:

```text id="x7q2m5"
It recursively creates tiny sorted arrays
```

Then combines them.

---

# **<span style="color:#ffd166">Python Implementation</span>**

```python id="es1w3g"
def merge_sort(arr):

    # Base case
    if len(arr) <= 1:
        return arr

    # Find middle
    mid = len(arr) // 2

    # Divide into halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge sorted halves
    return merge(left_half, right_half)


def merge(left, right):

    result = []

    i = 0   # pointer for left
    j = 0   # pointer for right

    # Compare elements from both arrays
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining left elements
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add remaining right elements
    while j < len(right):
        result.append(right[j])
        j += 1

    return result
```

---

# **<span style="color:#a29bfe">Understanding the Overall Flow</span>**

Merge Sort repeatedly performs:

```text id="q5m7v2"
Divide → Divide → Divide
```

Until:

```text id="n1q8m4"
Single-element arrays
```

Then:

```text id="r8m2q5"
Merge → Merge → Merge
```

Until whole array rebuilt.

---

# **<span style="color:#00d2d3">Understanding the Recursive Divide Phase</span>**

Suppose array:

```text id="g4m8q1"
[38, 27, 43, 3]
```

---

# **<span style="color:#feca57">Step 1: First Call</span>**

```python id="7kgc3r"
merge_sort([38, 27, 43, 3])
```

---

## Find Middle

```python id="1s4y7u"
mid = 2
```

Split:

```text id="u7q2m5"
left  = [38, 27]
right = [43, 3]
```

---

## Recursive Calls

```python id="sl1kx8"
merge_sort([38, 27])
merge_sort([43, 3])
```

---

# **<span style="color:#ff9f43">Step 2: Recursive Left Side</span>**

Call:

```python id="pzx0it"
merge_sort([38, 27])
```

---

## Split Again

```text id="w2m8q4"
left  = [38]
right = [27]
```

---

## Recursive Calls

```python id="k9v1tb"
merge_sort([38])
merge_sort([27])
```

---

# **<span style="color:#48dbfb">Base Case Reached</span>**

Single-element arrays:

```text id="x6q2m7"
[38]
[27]
```

Already sorted.

Return immediately.

---

# **<span style="color:#1dd1a1">Now Merge Happens</span>**

We merge:

```text id="g1m8q5"
[38] and [27]
```

---

# **<span style="color:#ff6b6b">Understanding Merge Function Deeply</span>**

---

# **<span style="color:#4ecdc4">Pointers</span>**

```python id="v0vwyj"
i = 0  # left pointer
j = 0  # right pointer
```

These pointers track:

```text id="m7q2v4"
current smallest unprocessed elements
```

---

# **<span style="color:#ffd166">Merge Step-by-Step</span>**

Left:

```text id="k4m8q2"
[38]
```

Right:

```text id="r9q2m1"
[27]
```

---

## Compare 38 and 27

```text id="u3m7q5"
27 smaller
```

Append:

```python id="lw9ms0"
result = [27]
```

Move right pointer:

```python id="g5ld0d"
j = 1
```

---

## Right Array Exhausted

Now copy remaining left elements:

```python id="jlwmr0"
result = [27, 38]
```

Return:

```text id="x8q2m4"
[27, 38]
```

---

# **<span style="color:#a29bfe">Right Side Recursion</span>**

Similarly:

```text id="p2m8q7"
[43,3]
```

becomes:

```text id="t6q2m5"
[3,43]
```

---

# **<span style="color:#00d2d3">Final Merge</span>**

Now merge:

```text id="n5m7q1"
[27,38]
[3,43]
```

---

# **<span style="color:#feca57">Detailed Final Merge Dry Run</span>**

---

## Initial

```python id="6v95l1"
i = 0
j = 0
result = []
```

---

## Compare 27 and 3

```text id="v1q8m4"
3 smaller
```

Append:

```python id="7jlwmf"
result = [3]
```

Move:

```python id="brh9lz"
j = 1
```

---

## Compare 27 and 43

```text id="g7m2q5"
27 smaller
```

Append:

```python id="jlwm8r"
result = [3, 27]
```

Move:

```python id="p1j5fz"
i = 1
```

---

## Compare 38 and 43

```text id="u4q8m2"
38 smaller
```

Append:

```python id="jlwmc2"
result = [3, 27, 38]
```

Move:

```python id="jlwmk8"
i = 2
```

---

## Left Array Exhausted

Copy remaining right elements:

```python id="jlwm0w"
result = [3, 27, 38, 43]
```

---

# **<span style="color:#ff9f43">Recursion Tree Visualization</span>**

```text id="n8m2q4"
                [38,27,43,3]
                 /        \
          [38,27]        [43,3]
            /   \          /   \
         [38] [27]      [43] [3]
```

Then merging upward:

```text id="x3q8m1"
[38]+[27] → [27,38]
[43]+[3]  → [3,43]

[27,38]+[3,43]
→ [3,27,38,43]
```

---

# **<span style="color:#48dbfb">Understanding the Recursion Mechanically</span>**

Very important concept:

---

# **<span style="color:#1dd1a1">Recursive Calls Go DOWN</span>**

The program stack keeps splitting:

```text id="p6m7q2"
larger → smaller → smaller
```

Until:

```text id="z2q8m5"
base case
```

---

# **<span style="color:#ff6b6b">Merging Happens While Returning UP</span>**

This is crucial.

Sorting actually occurs:

```text id="y5m8q1"
during recursion unwinding
```

NOT during splitting.

---

# **<span style="color:#4ecdc4">Important Internal Mechanics</span>**

---

# **<span style="color:#ffd166">1️⃣ Divide Operation</span>**

Contributes:

```text id="v8q2m4"
log n recursion depth
```

Because array halves repeatedly.

---

# **<span style="color:#a29bfe">2️⃣ Merge Operation</span>**

Most important step.

Every merge processes:

```text id="r4m7q5"
all elements linearly
```

Cost per level:

```text id="g1q8m7"
O(n)
```

---

# **<span style="color:#00d2d3">3️⃣ Recursion Stack</span>**

Recursive calls consume memory.

Depth:

\log_2 n

---

# **<span style="color:#feca57">Time Complexity Derivation</span>**

Levels:

\log n

Work per level:

```text id="m9q2v4"
O(n)
```

Total:

O(n \log n)

---

# **<span style="color:#ff9f43">Space Complexity</span>**

Temporary arrays:

```text id="k3m8q2"
O(n)
```

Recursion stack:

```text id="u7q2m5"
O(log n)
```

Overall:

```text id="x1m8q4"
O(n)
```

---

# **<span style="color:#48dbfb">Why Merge Sort Is So Powerful</span>**

Because:

```text id="n6q2m7"
Merging sorted arrays is easy
```

The algorithm transforms:

```text id="t5m7q1"
One hard sorting problem
```

into:

```text id="w8q2m4"
many tiny easy merging problems
```

---

# **<span style="color:#1dd1a1">Final Mental Model</span>**

Merge Sort behaves like:

```text id="r2m8q5"
Breaking a giant organization task
into tiny teams
```

Each team solves small task.

Then:

```text id="g5q7m1"
Results are systematically combined
```

into one final solution.

---

# **<span style="color:#ff6b6b">Key Insight</span>**

Merge Sort’s real intelligence is NOT:

```text id="m1q8v4"
the splitting
```

It is:

```text id="p7m2q5"
the efficient merging of sorted structures
```

That is the heart of the algorithm.
