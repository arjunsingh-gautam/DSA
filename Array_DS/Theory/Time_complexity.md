- `n` = number of elements currently stored in the array
- `capacity` = total allocated size of the underlying memory block

---

### 1. **Initialization (`__init__`)**

```python
def __init__(self):
    self._capacity = 1
    self._size = 0
    self._array = self._make_array(self._capacity)
```

- Just assigning values, no loops.
  ✅ **Time Complexity:** **O(1)**

---

### 2. **Get item (`__getitem__`)**

```python
def __getitem__(self, index):
    if 0 <= index < self._size:
        return self._array[index]
```

- Direct access via index (same as C array or Python list).
  ✅ **Time Complexity:** **O(1)**

---

### 3. **Set item (`__setitem__`)**

```python
def __setitem__(self, index, value):
    if 0 <= index < self._size:
        self._array[index] = value
```

- Again, direct access via index.
  ✅ **Time Complexity:** **O(1)**

---

### 4. **Append**

```python
def append(self, item):
    if self._size == self._capacity:
        self._resize(2 * self._capacity)
    self._array[self._size] = item
    self._size += 1
```

- If there’s space: just insertion → **O(1)**.
- If resizing is required: copying takes **O(n)**.
- But resizing happens rarely (doubling strategy).
  ✅ **Amortized Complexity:** **O(1)**
  ❌ **Worst Case:** **O(n)**

---

### 5. **Resize (Helper)**

```python
def _resize(self, new_capacity):
    new_array = self._make_array(new_capacity)
    for i in range(self._size):
        new_array[i] = self._array[i]
    self._array = new_array
    self._capacity = new_capacity
```

- Copies all elements → **O(n)**

---

### 6. **Delete (pop last)**

```python
def delete(self):
    if self._size > 0:
        self._size -= 1
        self._array[self._size] = 0  # optional
```

- Just reducing size → **O(1)**

---

### 7. **Insert at index**

```python
def insert(self, index, value):
    if self._size == self._capacity:
        self._resize(2 * self._capacity)
    for i in range(self._size, index, -1):
        self._array[i] = self._array[i - 1]
    self._array[index] = value
    self._size += 1
```

- Shifting elements → **O(n)** in worst case (insert at start).
  ✅ **Best Case:** **O(1)** (insert at end).
  ❌ **Worst Case:** **O(n)**

---

### 8. **Delete at index**

```python
def delete_at(self, index):
    for i in range(index, self._size - 1):
        self._array[i] = self._array[i + 1]
    self._size -= 1
```

- Shifting elements after index → **O(n)**

---

### 📊 **Summary of Time Complexities**

| Operation       | Time Complexity            |
| --------------- | -------------------------- |
| Initialization  | O(1)                       |
| Get item        | O(1)                       |
| Set item        | O(1)                       |
| Append          | Amortized O(1), Worst O(n) |
| Resize          | O(n)                       |
| Delete (pop)    | O(1)                       |
| Insert at index | O(n)                       |
| Delete at index | O(n)                       |

---
