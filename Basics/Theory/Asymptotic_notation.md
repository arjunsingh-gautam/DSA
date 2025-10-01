# <span style="color:yellow">**Asymptotic Notation**</span>

## 1. Definition of Big O Notation

- **Big O notation** describes the **upper bound** (worst-case growth rate) of an algorithm’s running time (or space usage) as the input size `n` grows.
- It ignores constants and low-order terms, focusing only on the **dominant factor** that dictates growth when `n → ∞`.

👉 Formally:
If an algorithm’s running time is `f(n)`, we say
**f(n) ∈ O(g(n))**
if there exist constants `c > 0` and `n₀ > 0` such that:

[
f(n) \leq c \cdot g(n) \quad \text{for all } n \geq n₀
]

---

## 2. How to Calculate Big O Mathematically

Steps:

1. **Express running time** as a function of input size `n`.
   Example: `f(n) = 3n² + 5n + 10`
2. **Keep the dominant term** (highest growth rate).
   → Here, `n²` dominates.
3. **Drop constants**.
   → `3n²` becomes `n²`.
4. Result: **O(n²)**

---

## 3. Examples

### Example 1: Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

- In worst case, we check all `n` elements.
- Time = `O(n)`

---

### Example 2: Nested Loop

```python
def pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])
```

- Outer loop runs `n` times.
- Inner loop runs `n` times per outer loop.
- Total = `n × n = n²` → `O(n²)`

---

### Example 3: Mixed terms

```python
def func(arr):
    for i in arr:          # O(n)
        print(i)
    for i in arr:          # O(n)
        for j in arr:      # O(n²)
            print(i, j)
```

- First loop = O(n)
- Second = O(n²)
- Total = O(n² + n) → O(n²) (drop smaller terms)

---

## 4. What Info Big O Conveys

- **Rate of growth**: How quickly running time grows as input increases.
- **Scalability**: Whether algorithm is practical for large `n`.
- **Worst-case guarantee**: Ensures performance won’t exceed this bound.

---

## 5. Use Cases of Big O

- **Compare algorithms** (e.g., O(n log n) sort vs O(n²) sort).
- **Predict performance** for large datasets.
- **Interview shorthand**: When asked about complexity, you answer in Big O.
- **System design**: Helps choose between approaches depending on input size.

---

## 6. Key Takeaways

- Big O **ignores constants** (O(2n) = O(n)).
- Focuses on **worst case**, but other notations (Ω, Θ) handle best/average.
- It’s about **growth rates**, not actual time in seconds.

---

✅ **Simple analogy:**
Big O is like describing how a car _accelerates_ with more passengers, not its actual speed at a moment. It shows the **trend**, not the exact number.

---

## 1. Definition of Ω (Omega) Notation

- **Ω-notation** describes the **asymptotic lower bound** of an algorithm’s running time (or space).
- It tells us the **best-case growth rate**: the minimum time the algorithm will take for input size `n`.

👉 Formally:
If an algorithm’s runtime is `f(n)`, we say
**f(n) ∈ Ω(g(n))**
if there exist constants `c > 0` and `n₀ > 0` such that:

[
f(n) \geq c \cdot g(n) \quad \text{for all } n \geq n₀
]

---

## 2. How to Calculate Ω Mathematically

Steps:

1. Express running time `f(n)` as a function of input size.
2. Look for the **slowest growing dominant term** (best case).
3. Drop constants.
4. That gives the Ω bound.

---

## 3. Examples

### Example 1: Linear Search

```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

- **Best case**: target is at index `0` → just 1 comparison.

- So, `Ω(1)`

- **Worst case** (Big O): O(n)

---

### Example 2: Bubble Sort

```python
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

- Best case: array is already sorted → inner swap never happens, but we still check each element once → Ω(n).
- Worst case: O(n²).

---

### Example 3: Simple Function

`f(n) = 4n² + 3n + 10`

- For Ω, we take the **dominant term that always grows fastest** → `n²`.
- So, Ω(n²).

---

## 4. What Info Ω Conveys

- **Lower bound guarantee**: At least this much time is needed, no matter what.
- **Best case** scenario of performance.
- **Efficiency floor**: Tells us how “fast” the algorithm can possibly be.

---

## 5. Use Cases

- Useful to analyze whether an algorithm is **sometimes efficient**.
  (e.g., QuickSort has Ω(n log n), meaning best case is very good).
- Complements Big O:

  - Big O → worst-case ceiling
  - Ω → best-case floor

- Helps in **average-case analysis** (together with Θ).

---

## 6. Quick Comparison

- **Big O (O)** → at most this much time.
- **Omega (Ω)** → at least this much time.
- **Theta (Θ)** → tightly bounded both above and below.

✅ **Analogy:**
Think of running a marathon:

- **Ω** = minimum time you could ever finish (even if everything goes perfectly).
- **O** = maximum time (even if everything goes wrong).
- **Θ** = your realistic average range.

---

## 1. Definition of Θ (Theta) Notation

- **Θ-notation** describes the **asymptotically tight bound** of an algorithm’s running time (or space).
- It means the algorithm grows **at least as fast** as some function _and_ **at most as fast** as that same function.

👉 Formally:
If runtime is `f(n)`, we say
**f(n) ∈ Θ(g(n))**
if there exist constants `c₁, c₂ > 0` and `n₀ > 0` such that:

[
c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n) \quad \text{for all } n \geq n₀
]

So, Θ means:

- `f(n)` is **sandwiched** between two multiples of `g(n)`.

---

## 2. How to Calculate Θ Mathematically

1. Write down runtime function `f(n)`.
2. Identify **dominant term**.
3. If both Big O (upper bound) and Omega (lower bound) are the same → That’s Θ.

Example:
`f(n) = 3n² + 5n + 20`

- O(n²) (upper bound)
- Ω(n²) (lower bound)
  → So Θ(n²).

---

## 3. Examples

### Example 1: Linear Search

- Worst case: O(n)
- Best case: Ω(1)
- Since O ≠ Ω → **not Θ(n)**

---

### Example 2: Binary Search

- Worst case: O(log n)
- Best case: Ω(1)
- Since O ≠ Ω → **not Θ(log n)**

---

### Example 3: Merge Sort

- Worst case: O(n log n)
- Best case: Ω(n log n)
- Same upper & lower bounds → **Θ(n log n)**

---

## 4. What Θ Conveys

- **Tight bound**: Gives the _exact_ growth rate, ignoring constants.
- If an algorithm is Θ(n log n), it means its time will always grow on the order of `n log n`, no better, no worse.
- More precise than just Big O or Ω alone.

---

## 5. Use Cases

- When analyzing algorithms in **textbooks, research, or interviews**, Θ is often preferred because it gives a **complete performance profile**.
- Good for comparing two algorithms’ _true asymptotic efficiency_.
- Helps detect if an algorithm’s best, average, and worst cases are similar.

---

## 6. Quick Comparison

- **Big O (O)** = maximum time (ceiling).
- **Omega (Ω)** = minimum time (floor).
- **Theta (Θ)** = exact growth rate (sandwiched).

✅ **Analogy:**
Think of Θ as a **speedometer range**:
If you always drive between 50–60 km/h, we can tightly say: Θ(55 km/h).
But if sometimes 10 km/h and sometimes 100 km/h, then Θ doesn’t exist — only O and Ω separately.

---
