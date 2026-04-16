# **<span style="color:#ff6b6b">Is `x in set` Constant Time or O(n)?</span>**

The lookup operation:

```python
x in my_set
```

has complexity:

```text
Average Case → O(1)
Worst Case → O(n)
```

But in practice (and in algorithm analysis), we treat it as:

```text
O(1)
```

because the worst case almost never happens.

---

# **<span style="color:#4ecdc4">Why Set Lookup Is Usually O(1)</span>**

Python **sets use a hash table** internally.

When you insert an element:

```python
my_set.add(x)
```

Python computes a **hash value**:

```text
hash(x)
```

This hash determines where the element is stored in memory.

So when checking:

```python
x in my_set
```

Python:

1. Computes `hash(x)`
2. Directly jumps to that location
3. Checks the value

So lookup happens in **constant time**.

---

# **<span style="color:#ffd166">Simple Analogy</span>**

Imagine a **library with numbered lockers**.

Each book is stored in a locker based on its **ID number**.

If someone asks:

```text
Do you have book 438?
```

You don't search every shelf.

Instead:

```text
Go directly to locker 438.
```

This is why lookup is **O(1)**.

---

# **<span style="color:#a29bfe">Why Worst Case Can Be O(n)</span>**

Worst case occurs when **many elements produce the same hash value**.

Example:

```text
hash(x1) = hash(x2) = hash(x3)
```

This creates a **collision chain**.

Now Python must check elements one-by-one.

So lookup becomes:

```text
O(n)
```

But Python's hashing system is designed to **minimize collisions**.

---

# **<span style="color:#00d2d3">Complexity Summary</span>**

| Operation  | Average | Worst |
| ---------- | ------- | ----- |
| `x in set` | O(1)    | O(n)  |
| Insert     | O(1)    | O(n)  |
| Delete     | O(1)    | O(n)  |

In algorithm design we assume:

```text
Set lookup = O(1)
```

---

# **<span style="color:#feca57">Comparison With List Lookup</span>**

Checking membership in a **list**:

```python
x in my_list
```

requires scanning the list.

Example:

```python
[3,7,9,1,5]
```

Python checks sequentially:

```text
3 → 7 → 9 → 1 → 5
```

So complexity:

```text
O(n)
```

---

# **<span style="color:#ff9f43">Example Comparison</span>**

Suppose:

```text
n = 1,000,000
```

### List lookup

Worst case:

```text
1,000,000 comparisons
```

### Set lookup

```text
1 hash computation
```

This is why **sets are dramatically faster for membership checks**.

---

# **<span style="color:#1dd1a1">Why HashSets Are So Important in DSA</span>**

Many problems require **fast membership checking**.

Using a set reduces:

```text
O(n²) → O(n)
```

Examples:

- Two Sum
- Longest Consecutive Sequence
- Contains Duplicate
- Jewels and Stones
- Intersection of Arrays

---

# **<span style="color:#a29bfe">Key Rule to Remember</span>**

When you see problems that ask:

```text
Does element X exist in collection Y?
```

Use:

```text
Set / HashMap
```

Because lookup becomes:

```text
O(1)
```

instead of:

```text
O(n)
```

---

If you'd like, I can also show you something extremely useful for interviews:

**Why Python sets and dictionaries almost never degrade to O(n) in real problems (and how they prevent hash collision attacks).**
