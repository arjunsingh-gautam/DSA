# **<span style="color:#ff6b6b">Floyd’s Tortoise and Hare Algorithm (Cycle Detection)</span>**

Floyd’s algorithm is used to **detect cycles in a linked list** using **two pointers moving at different speeds**.

Pointers:

```text
slow → moves 1 step
fast → moves 2 steps
```

If a cycle exists:

```text
fast pointer eventually catches the slow pointer
```

If there is **no cycle**:

```text
fast pointer reaches NULL
```

---

# **<span style="color:#4ecdc4">Core Idea</span>**

Think of two runners on a circular track.

```text
slow runner → 1 step each time
fast runner → 2 steps each time
```

Since the fast runner is faster:

```text
fast runner eventually laps slow runner
```

So they **meet inside the cycle**.

---

# **<span style="color:#ffd166">Basic Algorithm</span>**

```python
slow = head
fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True

return False
```

---

# **<span style="color:#a29bfe">Why We Use Different Speeds</span>**

Suppose both pointers move at **same speed**:

```text
slow → 1 step
fast → 1 step
```

Then:

```text
distance between them stays constant
```

They will **never meet**.

Therefore we need:

```text
fast speed > slow speed
```

The simplest choice:

```text
slow = 1
fast = 2
```

---

# **<span style="color:#00d2d3">Mathematical Reason Why They Meet</span>**

Let:

```text
k = length before cycle starts
c = cycle length
```

When slow enters the cycle, fast is already ahead.

Inside the cycle the **distance between them reduces every step**.

Relative speed:

```text
fast_speed - slow_speed
```

Example:

```text
fast = 2
slow = 1
relative speed = 1
```

So each iteration the gap decreases by **1 node**.

Eventually:

```text
gap becomes 0 → pointers meet
```

---

# **<span style="color:#feca57">Example Linked List With Cycle</span>**

Example:

```text
1 → 2 → 3 → 4 → 5
          ↑     ↓
          ← ← ←
```

Cycle starts at **3**.

Cycle length:

```text
3 → 4 → 5 → 3
```

Length:

```text
3
```

---

# **<span style="color:#ff9f43">Pointer Movement Dry Run</span>**

Initial:

```text
slow = 1
fast = 1
```

---

### Step 1

```text
slow → 2
fast → 3
```

Positions:

```text
slow = 2
fast = 3
```

---

### Step 2

```text
slow → 3
fast → 5
```

Positions:

```text
slow = 3
fast = 5
```

---

### Step 3

```text
slow → 4
fast → 4
```

Positions:

```text
slow = 4
fast = 4
```

Pointers meet.

Cycle detected.

---

# **<span style="color:#48dbfb">Visualizing Pointer Movement</span>**

Cycle portion:

```text
3 → 4 → 5 → 3
```

Movement inside cycle:

| Step | Slow | Fast |
| ---- | ---- | ---- |
| 1    | 3    | 5    |
| 2    | 4    | 4    |

Fast catches slow.

---

# **<span style="color:#1dd1a1">Why Fast Eventually Catches Slow</span>**

Inside the cycle, both pointers keep moving.

Difference in speed:

```text
fast moves 2 nodes
slow moves 1 node
```

So relative speed:

```text
1 node per iteration
```

This means fast **closes the gap** by 1 node each step.

If cycle length is `c`:

```text
they must meet within ≤ c steps
```

---

# **<span style="color:#a29bfe">Important Insight</span>**

Even if slow enters the cycle later:

```text
fast will still catch up
```

Because inside the loop both pointers **circulate infinitely**.

Eventually fast lands on slow.

---

# **<span style="color:#ff6b6b">Why Gap Doesn't Matter</span>**

Suppose gap between them inside cycle is:

```text
g nodes
```

Every step reduces gap by:

```text
relative_speed = fast - slow = 1
```

So after `g` steps:

```text
gap = 0
```

Pointers meet.

---

# **<span style="color:#ffd166">Time Complexity</span>**

Traversal occurs at most:

```text
O(n)
```

Where `n` is number of nodes.

---

# **<span style="color:#4ecdc4">Space Complexity</span>**

No extra memory.

```text
O(1)
```

---

# **<span style="color:#00d2d3">How To Choose Speed Gap</span>**

General rule:

```text
fast speed > slow speed
```

Common choice:

```text
slow = 1 step
fast = 2 steps
```

Why?

- minimal extra complexity
- simplest implementation
- guarantees meeting

Even if:

```text
slow = 1
fast = 3
```

it would still work.

But **2x speed is optimal and simplest**.

---

# **<span style="color:#f368e0">Where This Algorithm Is Used</span>**

This technique appears in many problems:

1. Linked List Cycle
2. Linked List Cycle II
3. Find Middle of Linked List
4. Happy Number
5. Detect Loop in Array

---

# **<span style="color:#ff6b6b">Key Intuition to Remember</span>**

Think:

```text
two runners on a circular track
```

If one runs faster:

```text
they must eventually meet
```

That meeting point proves a **cycle exists**.

---

If you'd like, I can also show you something **very important for interviews**:

**How Floyd’s algorithm can also find the exact node where the cycle begins (Linked List Cycle II)** — which uses a beautiful mathematical trick.
