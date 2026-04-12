
# **<span style="color:#ff6b6b">Problem: Product of Array Except Self</span>**

Given an integer array `nums`, return an array `result` such that:

```text
result[i] = product of all elements of nums except nums[i]
```

Constraints:

* **Division is not allowed**
* Must run in **O(n)** time

Example:

```text
nums = [1,2,3,4]

result = [24,12,8,6]
```

Explanation:

```
result[0] = 2×3×4 = 24
result[1] = 1×3×4 = 12
result[2] = 1×2×4 = 8
result[3] = 1×2×3 = 6
```

---

# **<span style="color:#4ecdc4">Analysis of Your Brute Force Solution</span>**

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]

            result.append(product)

        return result
```

### **Idea**

For each index:

```
Multiply all other elements except itself
```

Example:

```
nums = [1,2,3,4]

i = 0
product = 2×3×4 = 24

i = 1
product = 1×3×4 = 12
```

---

# **<span style="color:#ffd166">Pseudocode (Brute Force)</span>**

```
function productExceptSelf(nums):

    result = []

    for i from 0 to n-1:
        product = 1

        for j from 0 to n-1:
            if i != j:
                product *= nums[j]

        append product to result

    return result
```

---

# **<span style="color:#a29bfe">Concept Used</span>**

### **Nested Iteration / Pairwise Multiplication**

For every element:

```
scan entire array again
```

Structure:

```
outer loop → element to exclude
inner loop → multiply remaining elements
```

---

# **<span style="color:#ff9f43">Time Complexity</span>**

Outer loop:

```
n
```

Inner loop:

```
n
```

Total:

```
O(n²)
```

---

# **<span style="color:#48dbfb">Space Complexity</span>**

Only result array used.

```
O(n)
```

---

# **<span style="color:#4ecdc4">Analysis of Your Optimized Solution</span>**

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult=1
        r_mult=1
        n=len(nums)
        l_arr=[0]*n
        r_arr=[0]*n

        for i in range(n):
            j=-i-1
            l_arr[i]=l_mult
            r_arr[j]=r_mult
            l_mult*=nums[i]
            r_mult*=nums[j]

        return [l*r for l,r in zip(l_arr,r_arr)]
```

Your approach uses **prefix product + suffix product**.

This is the **standard optimal pattern**.

---

# **<span style="color:#ffd166">Approach Used</span>**

The product except self can be written as:

```
product_left × product_right
```

For index `i`:

```
result[i] = (product of elements left of i) × (product of elements right of i)
```

Example:

```
nums = [1,2,3,4]
```

Left products:

```
[1,1,2,6]
```

Right products:

```
[24,12,4,1]
```

Multiply:

```
[24,12,8,6]
```

---

# **<span style="color:#a29bfe">Pseudocode (Optimized)</span>**

```
function productExceptSelf(nums):

    n = length(nums)

    create left array
    create right array

    left_product = 1
    right_product = 1

    for i from 0 to n-1:

        left[i] = left_product
        left_product *= nums[i]

        j = n-1-i
        right[j] = right_product
        right_product *= nums[j]

    result = []

    for each index:
        result[i] = left[i] * right[i]

    return result
```

---

# **<span style="color:#00d2d3">Concept Used</span>**

### **Prefix-Suffix Product Pattern**

Idea:

```
result[i] =
product of elements before i
×
product of elements after i
```

This avoids:

```
recomputing products repeatedly
```

---

# **<span style="color:#feca57">Pattern Used</span>**

### **Prefix Computation Pattern**

General structure:

```
prefix[i] = prefix[i-1] * nums[i-1]
suffix[i] = suffix[i+1] * nums[i+1]
```

Then combine.

Used in many problems.

---

# **<span style="color:#ff9f43">Time Complexity</span>**

Loop runs once:

```
O(n)
```

Final multiplication:

```
O(n)
```

Total:

```
O(n)
```

Optimal.

---

# **<span style="color:#48dbfb">Space Complexity</span>**

You created:

```
left array → O(n)
right array → O(n)
result → O(n)
```

Total:

```
O(n)
```

---

# **<span style="color:#ff6b6b">Rating Your Approach</span>**

| Category            | Rating |
| ------------------- | ------ |
| Correctness         | ⭐⭐⭐⭐⭐  |
| Pattern recognition | ⭐⭐⭐⭐⭐  |
| Optimization        | ⭐⭐⭐⭐   |
| Code clarity        | ⭐⭐⭐⭐   |

Overall:

```
9 / 10
```

Excellent understanding.

Only improvement:

```
We can reduce space to O(1)
```

---

# **<span style="color:#54a0ff">More Optimal Approach (O(1) Extra Space)</span>**

Instead of two arrays:

Use result array for prefix.

Then multiply suffix.

Example:

```python
result=[1]*n

prefix=1
for i in range(n):
    result[i]=prefix
    prefix*=nums[i]

suffix=1
for i in reversed(range(n)):
    result[i]*=suffix
    suffix*=nums[i]
```

### Complexity

```
Time = O(n)
Space = O(1) extra
```

This is the **best LeetCode solution**.

---

# **<span style="color:#f368e0">LeetCode Problems With Same Pattern</span>**

These use **prefix / suffix computations**.

1. **Product of Array Except Self**

2. **Maximum Product Subarray**

3. **Trapping Rain Water**

4. **Pivot Index**

5. **Find Pivot Index**

6. **Range Sum Query**

7. **Subarray Sum Equals K**

---

# **<span style="color:#00d2d3">Practice Questions With Similar Pattern</span>**

### **Question 1**

Return array where:

```
result[i] = sum of all elements except nums[i]
```

---

### **Question 2**

Compute **prefix product array**.

---

### **Question 3**

Find index where:

```
sum left = sum right
```

(Pivot index problem)

---

### **Question 4**

Find maximum subarray product.

---

### **Question 5**

Given heights array compute trapped rain water.

---

# **<span style="color:#a29bfe">Important Pattern Recognition Tip</span>**

Whenever you see problems involving:

```
"all elements except current"
```

Think immediately:

```
prefix product
suffix product
```

Because brute force will be:

```
O(n²)
```

Prefix-suffix reduces it to:

```
O(n)
```

This pattern appears in **many array problems in interviews**.
