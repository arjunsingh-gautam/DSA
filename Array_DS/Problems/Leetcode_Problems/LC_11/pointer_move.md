# **<span style="color:#ff6b6b">Pointer Moving Logic in “Container With Most Water”</span>**

Your algorithm uses **two pointers**:

```text
left  → start of array
right → end of array
```

At every step you compute the container area:

```
area = (right - left) × min(height[left], height[right])
```

The important question is:

```
Which pointer should move?
```

The rule is:

```
Move the pointer with the smaller height.
```

Understanding **why this works** is the key.

---

# **<span style="color:#4ecdc4">Simple Real-World Analogy</span>**

Imagine **two vertical walls holding water**.

```
Wall A (height = 3)
Wall B (height = 10)
Distance between them = 10
```

Water level can only rise to the **shorter wall**.

So water height becomes:

```
3
```

Even if the second wall is **10 units tall**, water will **spill over the smaller wall first**.

So the container capacity depends on:

```
shorter wall
```

---

# **<span style="color:#ffd166">Key Insight</span>**

Area formula:

```
area = width × min(height_left , height_right)
```

Two factors control area:

```
1. width
2. smaller height
```

When we move pointers inward:

```
width always decreases
```

So the **only way to increase area** is to find a **taller shorter wall**.

---

# **<span style="color:#a29bfe">Why We Move the Smaller Pointer</span>**

Suppose:

```
height[left] = 3
height[right] = 10
```

Area:

```
width × 3
```

If we move the **right pointer**:

```
width decreases
height limit still = 3
```

Area becomes **even smaller**.

So moving the **right pointer cannot help**.

The only hope is:

```
Find a taller left wall
```

So we move:

```
left++
```

---

# **<span style="color:#00d2d3">Visual Example</span>**

Heights:

```
[1,8,6,2,5,4,8,3,7]
```

Initial pointers:

```
left  = 1
right = 7
```

Container:

```
|                |
|                |
|                |
|                |
|                |
|                |
|                |
|________________|
```

Area:

```
width = 8
height = min(1,7) = 1
area = 8
```

Since:

```
1 < 7
```

Move **left pointer**.

---

Next state:

```
left = 8
right = 7
```

Now:

```
width = 7
height = min(8,7) = 7
area = 49
```

This is the maximum.

---

# **<span style="color:#feca57">Important Intuition</span>**

Think of it like **searching for a taller wall**.

If the smaller wall is limiting the water level:

```
move that wall inward
```

because only that side can improve the height.

---

# **<span style="color:#ff9f43">Mathematical Reason</span>**

Current area:

```
A = width × min(h_left, h_right)
```

If:

```
h_left < h_right
```

then

```
A = width × h_left
```

Moving right pointer:

```
width ↓
height limit still h_left
```

Area **cannot increase**.

Only moving left pointer gives possibility of larger height.

---

# **<span style="color:#48dbfb">Simple Memory Trick</span>**

Remember this rule:

```
The shorter wall is the bottleneck.
Move the bottleneck.
```

---

# **<span style="color:#1dd1a1">Time Complexity Reason</span>**

Both pointers move inward.

Each pointer moves at most:

```
n times
```

Total operations:

```
O(n)
```

---

# **<span style="color:#a29bfe">Pattern Used</span>**

This problem uses the **Two Pointer Optimization Pattern**.

Typical structure:

```
left = 0
right = n-1

while left < right:
    compute value
    move one pointer
```

---

If you'd like, I can also show you something **very powerful for interviews**:

**A geometric proof of why moving the larger pointer can never give a better solution** (this trick appears in multiple FAANG problems).
