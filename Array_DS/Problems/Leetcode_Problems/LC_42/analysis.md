# **<span style="color:#ff6b6b">Problem: Trapping Rain Water</span>**

You are given an elevation map where the width of each bar is `1`.

Each element represents **height of a wall**.

After raining, water gets trapped between walls.

Example:

```text
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

Water trapped =

```text
6
```

---

# **<span style="color:#4ecdc4">Your Solution</span>**

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxL=0
        maxR=0
        L=[0]*n
        R=[0]*n
        water=0
        for i in range(n):
            current=height[i]
            L[i]=maxL
            maxL=max(current,maxL)

        for j in range(n-1,-1,-1):
            current=height[j]
            R[j]=maxR
            maxR=max(current,maxR)

        for i in range(n):
            potential=min(L[i],R[i])
            if (potential-height[i]<=0):
                continue
            else:
                water+=(potential-height[i])

        return water
```

Your solution uses the **Prefix Maximum + Suffix Maximum pattern**.

This is a **standard optimal approach (O(n))**.

---

# **<span style="color:#ffd166">Core Idea of the Problem</span>**

Water trapped above a bar depends on:

```text
1. Tallest wall on the left
2. Tallest wall on the right
```

Water level is limited by the **shorter boundary**.

Formula:

```text
water_at_i = min(maxLeft[i], maxRight[i]) - height[i]
```

If the result is negative → no water.

---

# **<span style="color:#a29bfe">Approach Used in Your Code</span>**

Your algorithm works in **3 phases**:

### **Step 1 — Compute Left Maximum Array**

```python
for i in range(n):
    L[i]=maxL
    maxL=max(current,maxL)
```

Meaning:

```text
L[i] = tallest wall to the left of index i
```

Example:

```text
height = [0,1,0,2,1]
```

Left max array:

```text
L = [0,0,1,1,2]
```

---

### **Step 2 — Compute Right Maximum Array**

```python
for j in range(n-1,-1,-1):
    R[j]=maxR
    maxR=max(current,maxR)
```

Meaning:

```text
R[i] = tallest wall to the right of index i
```

Example:

```text
R = [2,2,2,1,0]
```

---

### **Step 3 — Compute Water Above Each Bar**

```python
potential=min(L[i],R[i])
```

Water level at position `i`:

```text
min(maxLeft , maxRight)
```

Water stored:

```text
water = potential - height[i]
```

If negative → ignore.

---

# **<span style="color:#00d2d3">Simple Analogy</span>**

Imagine buildings forming **a valley**.

Example:

```text
wall height:

5     4
|     |
|     |
|  1  |
|_____|
```

Water fills until the **shorter wall height**.

Because water spills over the smaller boundary.

So trapped water:

```text
min(left wall , right wall) - valley height
```

---

# **<span style="color:#feca57">Example Dry Run</span>**

Example:

```text
height = [4,2,0,3,2,5]
```

Left max:

```text
L = [0,4,4,4,4,4]
```

Right max:

```text
R = [5,5,5,5,5,0]
```

Compute water:

| i   | height | min(L,R) | water |
| --- | ------ | -------- | ----- |
| 0   | 4      | 0        | 0     |
| 1   | 2      | 4        | 2     |
| 2   | 0      | 4        | 4     |
| 3   | 3      | 4        | 1     |
| 4   | 2      | 4        | 2     |
| 5   | 5      | 0        | 0     |

Total water:

```text
9
```

---

# **<span style="color:#ff9f43">Time Complexity</span>**

Three passes through array:

```text
Left scan   → O(n)
Right scan  → O(n)
Water calc  → O(n)
```

Total:

```text
O(n)
```

---

# **<span style="color:#48dbfb">Space Complexity</span>**

Extra arrays:

```text
L array → O(n)
R array → O(n)
```

Total:

```text
O(n)
```

---

# **<span style="color:#1dd1a1">Rating Your Approach</span>**

| Category      | Rating     |
| ------------- | ---------- |
| Correctness   | ⭐⭐⭐⭐⭐ |
| Pattern usage | ⭐⭐⭐⭐⭐ |
| Efficiency    | ⭐⭐⭐⭐   |
| Code clarity  | ⭐⭐⭐⭐   |

Overall:

```text
9 / 10
```

Very good solution.

---

# **<span style="color:#ff6b6b">More Optimal Approach</span>**

Your approach uses:

```text
O(n) extra space
```

But we can solve it using **two pointers with O(1) space**.

Idea:

```text
Track maxLeft and maxRight while moving pointers inward.
```

---

### Two Pointer Code

```python
left=0
right=len(height)-1
maxL=0
maxR=0
water=0

while left<right:

    if height[left] < height[right]:

        if height[left] >= maxL:
            maxL = height[left]
        else:
            water += maxL - height[left]

        left += 1

    else:

        if height[right] >= maxR:
            maxR = height[right]
        else:
            water += maxR - height[right]

        right -= 1
```

Space complexity becomes:

```text
O(1)
```

---

# **<span style="color:#a29bfe">Pattern Used</span>**

This problem uses:

```text
Prefix Max / Suffix Max Pattern
```

And the optimized version uses:

```text
Two Pointer Boundary Tracking
```

---

# **<span style="color:#00d2d3">LeetCode Problems With Similar Pattern</span>**

Problems using **prefix/suffix or boundary logic**:

1. Trapping Rain Water
2. Container With Most Water
3. Product of Array Except Self
4. Maximum Product Subarray
5. Find Pivot Index

---

# **<span style="color:#f368e0">Practice Questions With Same Pattern</span>**

### Question 1

Given an array, compute **prefix maximum values**.

---

### Question 2

Find the **maximum difference between left max and right max**.

---

### Question 3

Find the **total water trapped between buildings**.

---

### Question 4

Compute **maximum profit from stock prices** using prefix minimum.

---

### Question 5

Find the **largest rectangle in histogram**.

---

# **<span style="color:#a29bfe">Key Insight to Remember</span>**

The trapped water at index `i` depends on:

```text
smaller boundary - height[i]
```

Where boundaries are:

```text
max wall to the left
max wall to the right
```

This idea appears in many **array boundary problems**.

---

If you'd like, I can also show you something **very powerful for interviews**:

**A geometric intuition for why the two-pointer trapping rainwater solution works (most candidates misunderstand this).**
