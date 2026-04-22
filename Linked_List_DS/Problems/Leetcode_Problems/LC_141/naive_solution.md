# **<span style="color:#ff6b6b">Problem: Linked List Cycle Detection</span>**

Given the head of a singly linked list, determine whether the list contains a **cycle**.

A cycle occurs when:

```text
a node's next pointer points to a previously visited node
```

Example:

```
1 → 2 → 3 → 4
      ↑     ↓
      ← ← ←
```

Here node `4` points back to `2`, forming a **cycle**.

Return:

```text
True  → cycle exists
False → no cycle
```

---

# **<span style="color:#4ecdc4">Your Solution</span>**

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=set()
        current=head
        while current:
            if current in visited:
                return True
            else:
                visited.add(current)
                current=current.next
        return False
```

Your idea:

```text
Store visited nodes in a set.
If a node appears again → cycle exists.
```

This is a **correct and commonly used naive solution**.

---

# **<span style="color:#ffd166">Approach Used</span>**

Pattern used:

```text
HashSet / Visited Node Tracking
```

Idea:

```text
Each node should be visited only once in a normal linked list.
If we encounter the same node again → cycle exists.
```

---

# **<span style="color:#a29bfe">Step-by-Step Explanation</span>**

### **Step 1: Create a Set**

```python
visited=set()
```

This set stores **node references**.

Important:

```text
It stores nodes themselves, not values.
```

Example stored elements:

```
{node1, node2, node3}
```

---

### **Step 2: Traverse the Linked List**

```python
current = head
```

Move through the list.

---

### **Step 3: Check if Node Was Seen Before**

```python
if current in visited
```

If yes:

```text
cycle detected
```

Return:

```text
True
```

---

### **Step 4: Otherwise Add Node to Set**

```python
visited.add(current)
```

Move to next node:

```python
current = current.next
```

---

# **<span style="color:#00d2d3">Example Dry Run</span>**

Linked list:

```
1 → 2 → 3 → 4
      ↑     ↓
      ← ← ←
```

Traversal:

| Step | Node | Visited Set             |
| ---- | ---- | ----------------------- |
| 1    | 1    | {1}                     |
| 2    | 2    | {1,2}                   |
| 3    | 3    | {1,2,3}                 |
| 4    | 4    | {1,2,3,4}               |
| 5    | 2    | already visited → cycle |

Return:

```text
True
```

---

# **<span style="color:#feca57">Time Complexity</span>**

Let:

```text
n = number of nodes
```

Traversal:

```text
O(n)
```

Set lookup:

```text
O(1)
```

Total:

```text
O(n)
```

---

# **<span style="color:#ff9f43">Space Complexity</span>**

Set stores visited nodes.

Worst case:

```text
O(n)
```

---

# **<span style="color:#48dbfb">Rating Your Approach</span>**

| Category            | Rating     |
| ------------------- | ---------- |
| Correctness         | ⭐⭐⭐⭐⭐ |
| Efficiency          | ⭐⭐⭐⭐   |
| Pattern recognition | ⭐⭐⭐⭐   |

Overall:

```text
8.5 / 10
```

Good solution but **not the optimal one**.

---

# **<span style="color:#ff6b6b">Optimal Solution (Floyd’s Cycle Detection)</span>**

The optimal approach uses **two pointers**.

Also called:

```text
Floyd's Tortoise and Hare Algorithm
```

Idea:

```
slow pointer → moves 1 step
fast pointer → moves 2 steps
```

If a cycle exists:

```text
fast pointer will eventually meet slow pointer
```

---

# **<span style="color:#a29bfe">Optimal Code</span>**

```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

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

# **<span style="color:#00d2d3">Why This Works</span>**

Imagine runners on a circular track.

```
slow runner → 1 step
fast runner → 2 steps
```

If the track is circular:

```text
fast runner will eventually lap the slow runner.
```

So they meet.

If there is **no cycle**:

```text
fast pointer reaches None
```

---

# **<span style="color:#1dd1a1">Optimal Complexity</span>**

Time:

```text
O(n)
```

Space:

```text
O(1)
```

No extra memory needed.

---

# **<span style="color:#f368e0">Pattern Used</span>**

Two patterns exist for this problem:

### **Approach 1**

```
HashSet visited nodes
```

### **Approach 2 (Optimal)**

```
Fast and Slow Pointer
```

---

# **<span style="color:#00d2d3">Similar LeetCode Problems</span>**

Problems using **fast-slow pointer pattern**:

1. Linked List Cycle
2. Linked List Cycle II
3. Find Middle of Linked List
4. Happy Number
5. Detect Cycle in Circular Array

---

# **<span style="color:#ff6b6b">Key Insight</span>**

Whenever a linked list problem involves:

```text
cycle detection
middle element
loop detection
```

Think immediately:

```text
Fast and Slow Pointer
```

This pattern appears frequently in **linked list interview questions**.

---

If you'd like, I can also show you something **very important for interviews**:

**The mathematical proof of why the slow and fast pointer must meet if a cycle exists.**
