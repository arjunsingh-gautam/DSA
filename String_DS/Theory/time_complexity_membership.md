Excellent question 👍 — this depends on

## 🔹 1. **Lists / Tuples / Strings**

- `x in some_list` → **O(n)** time complexity
- Because Python has to scan each element **sequentially** until it finds a match (linear search).

Example:

```python
nums = [1, 2, 3, 4, 5]
print(3 in nums)  # True, but needs scanning
```

👉 Worst case: entire list scanned.

---

## 🔹 2. **Sets / Dictionaries**

- `x in some_set` or `key in some_dict` → **O(1)** average time complexity
- Because they use **hash tables** internally.
- But worst case (rare, hash collisions): **O(n)**.

Example:

```python
s = {1, 2, 3, 4, 5}
print(3 in s)  # True, hash lookup → average O(1)
```

---

## 🔹 3. **Other Iterables (Generators, custom iterators, etc.)**

- `in` operator works by **iterating element by element**, so it’s **O(n)**.

Example:

```python
gen = (i for i in range(10))
print(5 in gen)  # True, but checked sequentially → O(n)
```

---

## ✅ Summary Table

| Iterable Type         | `in` Lookup Complexity   |
| --------------------- | ------------------------ |
| List / Tuple / String | O(n)                     |
| Set / Dict (keys)     | O(1) average, O(n) worst |
| Generator / Iterator  | O(n)                     |

---

👉 So the answer:

- **O(n)** for lists, tuples, strings, generators
- **O(1) average** for sets and dicts (hash-based lookup)

---
