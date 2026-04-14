# **<span style="color:#ff6b6b">Problem: 3Sum</span>**

Given an integer array `nums`, return **all unique triplets** such that:

```text
nums[i] + nums[j] + nums[k] = 0
```

Conditions:

- `i ≠ j ≠ k`
- No duplicate triplets in the result

Example:

```
nums = [-1,0,1,2,-1,-4]

Output:
[[-1,-1,2],[-1,0,1]]
```

---

# **<span style="color:#4ecdc4">Your Solution</span>**

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        answers=[]

        for i in range(n):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            low=i+1
            high=n-1
            while low<high:
                sum=nums[i]+nums[low]+nums[high]
                if (sum==0):
                    answers.append([nums[i],nums[low],nums[high]])
                    low+=1
                    high-=1
                    while low<high and nums[low]==nums[low-1]:
                        low+=1
                    while low<high and nums[high]==nums[high+1]:
                        high-=1
                elif sum<0:
                    low+=1
                else:
                    high-=1
        return answers
```

This is the **optimal solution** using:

```
Sorting + Two Pointer Pattern
```

---

# **<span style="color:#ffd166">High-Level Approach</span>**

We convert the **3Sum problem into multiple 2Sum problems**.

Steps:

1. **Sort the array**
2. Fix one number (`nums[i]`)
3. Use **two pointers** to find the remaining two numbers.

So we solve:

```
nums[i] + nums[low] + nums[high] = 0
```

Which becomes:

```
nums[low] + nums[high] = -nums[i]
```

---

# **<span style="color:#a29bfe">Step-by-Step Algorithm</span>**

### **Step 1 — Sort the array**

```
nums.sort()
```

Example:

```
[-1,0,1,2,-1,-4]
```

becomes

```
[-4,-1,-1,0,1,2]
```

Sorting allows **two pointer logic to work**.

---

### **Step 2 — Fix the first element**

Loop through the array.

```
for i in range(n)
```

This element acts as the **first number of the triplet**.

Example:

```
nums[i] = -1
```

Now we search for two numbers that sum to:

```
target = -nums[i]
```

---

### **Step 3 — Use Two Pointers**

Initialize:

```
low = i + 1
high = n - 1
```

These pointers search for the remaining pair.

---

# **<span style="color:#00d2d3">Pointer Moving Logic</span>**

At each step:

```
sum = nums[i] + nums[low] + nums[high]
```

Now we compare the sum.

---

## **Case 1: sum == 0**

Triplet found.

```
answers.append(...)
```

Move both pointers inward:

```
low++
high--
```

Why?

Because this pair has been processed already.

---

## **Case 2: sum < 0**

The sum is too small.

Example:

```
-1 + -1 + 1 = -1
```

To increase the sum:

```
move low pointer right
```

Because numbers increase in a sorted array.

```
low++
```

---

## **Case 3: sum > 0**

The sum is too large.

Example:

```
-1 + 1 + 2 = 2
```

To decrease the sum:

```
move high pointer left
```

```
high--
```

---

# **<span style="color:#feca57">Simple Analogy</span>**

Imagine you want **three numbers whose sum is zero**.

Fix one number.

Then look for two numbers whose sum equals:

```
target = -fixed_number
```

Now use two pointers like **balancing a scale**.

```
sum too small → move low pointer
sum too large → move high pointer
```

You are **adjusting the sum toward zero**.

---

# **<span style="color:#ff9f43">Example Dry Run</span>**

Sorted array:

```
[-4,-1,-1,0,1,2]
```

---

### i = 1 → nums[i] = -1

Pointers:

```
low = 2
high = 5
```

Check:

```
-1 + -1 + 2 = 0
```

Triplet found.

```
[-1,-1,2]
```

Move pointers.

---

Next:

```
low = 3
high = 4
```

Check:

```
-1 + 0 + 1 = 0
```

Triplet found.

```
[-1,0,1]
```

---

# **<span style="color:#48dbfb">Duplicate Handling</span>**

You skip duplicates using:

```
if nums[i] == nums[i-1]
```

And also skip duplicates inside the pointer loop.

Why?

Because the problem requires **unique triplets**.

Example:

```
[-1,-1,2]
```

Should appear only once.

---

# **<span style="color:#1dd1a1">Why This Works</span>**

Sorting gives us:

```
nums[low] ≤ nums[high]
```

So adjusting pointers **monotonically moves toward the target**.

This eliminates the need for brute-force triple loops.

---

# **<span style="color:#ff6b6b">Time Complexity</span>**

Sorting:

```
O(n log n)
```

Outer loop:

```
O(n)
```

Two-pointer search:

```
O(n)
```

Total:

```
O(n²)
```

This is **optimal for 3Sum**.

---

# **<span style="color:#54a0ff">Space Complexity</span>**

Ignoring output storage:

```
O(1)
```

---

# **<span style="color:#f368e0">Pattern Used</span>**

This problem uses:

```
Sorting + Two Pointer + Duplicate Skipping
```

This is a **very common interview pattern**.

---

# **<span style="color:#00d2d3">Related LeetCode Problems</span>**

Similar patterns appear in:

1. **Two Sum II**
2. **3Sum Closest**
3. **4Sum**
4. **Container With Most Water**
5. **Trapping Rain Water**

---

# **<span style="color:#a29bfe">Key Insight to Remember</span>**

The trick is:

```
3Sum → reduce to multiple 2Sum problems
```

Then solve each **2Sum using two pointers**.

---

If you'd like, I can also show you something **very powerful for interviews**:

**A geometric intuition for why the two-pointer search always finds all pairs without missing any combinations.**
