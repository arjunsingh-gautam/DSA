# **<span style="color:#ff6b6b">Problem: Find All Numbers Disappeared in an Array</span>**

LeetCode: **Find All Numbers Disappeared in an Array**

Input constraints:

- `nums` size = `n`
- values range from **1 → n**

Example:

```
Input:
nums = [4,3,2,7,8,2,3,1]

Output:
[5,6]
```

Meaning:

Numbers **1..n should exist**, but some numbers are missing.

---

# **<span style="color:#4ecdc4">Your Solution</span>**

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result=[]
        mapping=[0]*len(nums)

        for i in nums:
            index=i-1
            mapping[index]+=1

        for j in range(len(nums)):
            if mapping[j]==0:
                result.append(j+1)

        return result
```

Your idea:

> **Index represents the number**
>
> **Value represents frequency**

This is what you called **hashlist**.

Correct concept.

---

# **<span style="color:#ffd166">Approach Used in Your Solution</span>**

You created a **frequency array** where:

```
index = number - 1
value = frequency of that number
```

Example:

```
nums = [4,3,2,7,8,2,3,1]
n = 8
```

Initial mapping:

```
[0,0,0,0,0,0,0,0]
```

After counting:

```
[1,2,2,1,0,0,1,1]
```

Interpretation:

```
index 4 → value 0 → number 5 missing
index 5 → value 0 → number 6 missing
```

So result:

```
[5,6]
```

---

# **<span style="color:#a29bfe">Concept Used</span>**

## **Frequency Hashing (Hash List)**

Instead of using:

```
dict / hashmap
```

You used:

```
list as frequency table
```

This works because:

```
numbers range = 1..n
```

So we can map:

```
number → index
```

Mapping rule:

```
index = number - 1
```

This technique is extremely common in DSA.

---

# **<span style="color:#00d2d3">Pattern Used</span>**

### **Index Mapping Pattern**

Key idea:

```
Use index of array to represent numbers
```

General structure:

```
index = value - offset
```

Examples:

```
value range 1..n → index = value-1
value range 0..n → index = value
```

Used when:

- Numbers have **limited range**
- You want **O(1) lookup**
- You want **O(n) time**

---

# **<span style="color:#feca57">Pseudocode</span>**

```
function findDisappearedNumbers(nums):

    create result list

    create mapping array of size n filled with 0

    for each number in nums:
        index = number - 1
        mapping[index] += 1

    for index from 0 to n-1:
        if mapping[index] == 0:
            result.append(index + 1)

    return result
```

---

# **<span style="color:#ff9f43">Step-by-Step Example</span>**

Input:

```
nums = [4,3,2,7,8,2,3,1]
```

### Step 1: Count frequencies

```
mapping = [1,2,2,1,0,0,1,1]
```

### Step 2: Find missing numbers

```
index 4 → 0 → number 5
index 5 → 0 → number 6
```

Result:

```
[5,6]
```

---

# **<span style="color:#48dbfb">Time Complexity Analysis</span>**

Let:

```
n = length of nums
```

### First loop

```
for i in nums
```

Cost:

```
O(n)
```

### Second loop

```
for j in range(n)
```

Cost:

```
O(n)
```

### Total

```
Time Complexity = O(n)
```

Optimal.

---

# **<span style="color:#1dd1a1">Space Complexity Analysis</span>**

You created:

```
mapping array size = n
```

So:

```
Space Complexity = O(n)
```

Result array also worst case:

```
O(n)
```

Total:

```
O(n)
```

---

# **<span style="color:#ff6b6b">Rating Your Approach</span>**

| Criteria         | Rating     |
| ---------------- | ---------- |
| Correctness      | ⭐⭐⭐⭐⭐ |
| Simplicity       | ⭐⭐⭐⭐⭐ |
| Time Complexity  | ⭐⭐⭐⭐⭐ |
| Space Efficiency | ⭐⭐⭐     |

Overall:

```
8 / 10
```

Why not 10?

Because **LeetCode expects O(1) extra space solution**.

But your solution is **clean and very interview friendly**.

---

# **<span style="color:#54a0ff">Better Approach (Optimal)</span>**

## **In-place Marking Technique**

Key idea:

```
Use nums itself as hashmap
```

Steps:

```
value = abs(nums[i])
index = value - 1
mark nums[index] negative
```

Example:

```
nums = [4,3,2,7,8,2,3,1]
```

Mark visited numbers by **negative sign**.

Finally:

```
positive numbers → missing indexes
```

Code:

```python
for i in range(len(nums)):
    index = abs(nums[i]) - 1
    if nums[index] > 0:
        nums[index] *= -1

result = []
for i in range(len(nums)):
    if nums[i] > 0:
        result.append(i+1)
```

### Complexity

```
Time = O(n)
Space = O(1)
```

This is the **optimal LeetCode solution**.

---

# **<span style="color:#f368e0">Other Approaches</span>**

## **Approach 1 — Hash Set**

Idea:

```
store all numbers in set
```

Then check missing numbers.

```
for i in range(1,n+1):
    if i not in set:
        missing
```

Time:

```
O(n)
```

Space:

```
O(n)
```

---

## **Approach 2 — Sorting**

Sort the array and check gaps.

Time:

```
O(n log n)
```

Worse than your solution.

---

# **<span style="color:#ff9ff3">LeetCode Problems with Same Pattern</span>**

### **Index Mapping / Frequency Pattern**

1️⃣ **Find All Numbers Disappeared in an Array**

2️⃣ **Find All Duplicates in an Array**

3️⃣ **First Missing Positive**

4️⃣ **Set Mismatch**

5️⃣ **Find the Duplicate Number**

6️⃣ **Missing Number**

These problems use:

```
index = value mapping
```

---

# **<span style="color:#00d2d3">Questions That Use Similar Approach</span>**

These are **good practice questions**.

### Question 1

Given array with numbers **1..n**, find all **duplicate numbers**.

---

### Question 2

Find the **first missing positive integer**.

---

### Question 3

Find the **single missing number from 0..n**.

---

### Question 4

Find numbers appearing **twice** in array.

---

### Question 5

Given numbers **1..n**, find the **duplicate and missing number**.

---

# **<span style="color:#a29bfe">Important Interview Insight</span>**

When you see:

```
numbers range = 1..n
array size = n
```

Immediately think:

```
INDEX MAPPING
```

Techniques:

```
1️⃣ Frequency array
2️⃣ In-place marking
3️⃣ Cyclic sort
```

These are **very high-frequency interview patterns**.

---

If you want, I can also show you:

- **The 6 most important “index mapping” problems asked in FAANG**
- **Cyclic Sort pattern (EXTREMELY powerful)**
- **Mental framework to detect these problems instantly**

These will **massively improve your DSA pattern recognition.**
