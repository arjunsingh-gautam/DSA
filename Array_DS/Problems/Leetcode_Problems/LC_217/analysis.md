# **<span style="color:#ff6b6b">Problem: Contains Duplicate</span>**

Given an integer array `nums`, return **True** if any value appears **at least twice**, otherwise return **False**.

Example:

```text
nums = [1,2,3,1]
Output: True
```

Because **1 appears twice**.

Another example:

```text
nums = [1,2,3,4]
Output: False
```

No duplicates exist.

---

# **<span style="color:#4ecdc4">Analysis of Your Approaches</span>**

You described **three approaches**:

1. **Brute Force — Pair Comparison**
2. **HashSet (Set Conversion)**
3. **Sorting + Adjacent Comparison**

These represent the **standard progression of solutions in interviews**.

---

# **<span style="color:#ffd166">Approach-1: Brute Force (Pair Checking)</span>**

## **Idea**

Check **every pair of elements** and see if two numbers are equal.

Example:

```text
nums = [1,2,3,3]

Pairs checked:
(1,2)
(1,3)
(1,3)
(2,3)
(2,3)
(3,3) → duplicate found
```

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
function containsDuplicate(nums):

    for i from 0 to n-1:
        for j from i+1 to n-1:
            if nums[i] == nums[j]:
                return True

    return False
```

---

# **<span style="color:#00d2d3">Concept Used</span>**

### **Pair Enumeration**

You compare every pair:

```
nums[i] == nums[j]
```

Total comparisons:

```
n(n-1)/2
```

This leads to **quadratic time complexity**.

---

# **<span style="color:#ff9f43">Complexity Analysis</span>**

### Time Complexity

```
O(n²)
```

Because of **nested loops**.

### Space Complexity

```
O(1)
```

No extra memory used.

---

# **<span style="color:#48dbfb">Approach-2: Using Set (HashSet Pattern)</span>**

Your main idea:

```
convert list → set
```

Because:

```
set automatically removes duplicates
```

So if duplicates exist:

```
len(nums) != len(set(nums))
```

---

# **<span style="color:#feca57">Pseudocode</span>**

```
function containsDuplicate(nums):

    unique_set = convert nums into set

    if size of unique_set != size of nums:
        return True
    else:
        return False
```

---

# **<span style="color:#1dd1a1">Concept Used</span>**

## **Hashing / Set Membership**

A **set** uses hashing internally.

Properties:

```
unique elements only
O(1) insertion
O(1) lookup
```

So duplicates automatically disappear.

Example:

```
nums = [1,2,3,3]

set(nums) → {1,2,3}
```

Size changed:

```
4 → 3
```

So duplicates exist.

---

# **<span style="color:#ff9f43">Time Complexity</span>**

Building set requires scanning array.

```
O(n)
```

---

# **<span style="color:#48dbfb">Space Complexity</span>**

Set stores elements.

```
O(n)
```

---

# **<span style="color:#54a0ff">Approach-3: Sorting + Adjacent Comparison</span>**

Idea:

```
Sort array
```

Then duplicates will become **adjacent**.

Example:

```
nums = [3,1,2,3]
sorted → [1,2,3,3]
```

Now compare neighbors.

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
function containsDuplicate(nums):

    sort nums

    for i from 1 to n-1:
        if nums[i] == nums[i-1]:
            return True

    return False
```

---

# **<span style="color:#00d2d3">Concept Used</span>**

### **Sorting + Neighbor Comparison**

Sorting groups identical values together.

Pattern:

```
sort → compare adjacent elements
```

Used frequently in:

```
duplicate detection
interval merging
two pointer problems
```

---

# **<span style="color:#ff9f43">Time Complexity</span>**

Sorting:

```
O(n log n)
```

Scanning:

```
O(n)
```

Total:

```
O(n log n)
```

---

# **<span style="color:#48dbfb">Space Complexity</span>**

Depends on sorting algorithm.

Typically:

```
O(1) to O(n)
```

---

# **<span style="color:#ff6b6b">Rating Your Approaches</span>**

| Approach    | Rating     | Reason                  |
| ----------- | ---------- | ----------------------- |
| Brute Force | ⭐⭐⭐     | Correct but inefficient |
| Sorting     | ⭐⭐⭐⭐   | Good but slower         |
| HashSet     | ⭐⭐⭐⭐⭐ | Optimal                 |

### **Overall**

```
9 / 10
```

Your thinking shows **correct algorithm progression**.

---

# **<span style="color:#f368e0">Other Possible Approaches</span>**

## **Approach-4: HashMap Frequency Counting**

Store frequency of numbers.

```
map[number] += 1
```

If frequency > 1 → duplicate.

Complexity:

```
Time: O(n)
Space: O(n)
```

---

## **Approach-5: Bitset (Advanced)**

If number range is small, use bit array.

Example:

```
seen[number] = True
```

Useful in **system-level optimizations**.

---

# **<span style="color:#ff9ff3">LeetCode Problems With Same Pattern</span>**

### **Hashing / Duplicate Detection Pattern**

1. **Contains Duplicate**

2. **Contains Duplicate II**

3. **Contains Duplicate III**

4. **Find All Duplicates in an Array**

5. **First Missing Positive**

6. **Happy Number**

7. **Intersection of Two Arrays**

---

# **<span style="color:#00d2d3">Practice Questions With Similar Pattern</span>**

### **Question-1**

Find the **first duplicate element** in an array.

---

### **Question-2**

Find **all duplicates** in the array.

---

### **Question-3**

Return **count of duplicate elements**.

---

### **Question-4**

Check if array contains duplicates **within distance k**.

---

### **Question-5**

Find the **missing number from range 1..n**.

---

# **<span style="color:#a29bfe">Important Pattern Recognition</span>**

When you see problems involving:

```
duplicate detection
unique elements
frequency counting
```

Think immediately:

```
1️⃣ HashSet
2️⃣ HashMap
3️⃣ Sorting + neighbor check
```

These patterns solve **many array interview questions**.

---

If you want, I can also show you something very powerful:

**The 10 HashMap patterns that solve ~45% of LeetCode problems.**
