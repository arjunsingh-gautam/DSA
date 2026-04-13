# **<span style="color:#ff6b6b">Problem: Container With Most Water</span>**

You are given an array `heights` where each element represents a vertical line.

Two lines form a **container**, and the container can hold water equal to:

```text
width × minimum height
```

Example:

```text
heights = [1,8,6,2,5,4,8,3,7]
```

The maximum area formed is:

```text
49
```

---

# **<span style="color:#4ecdc4">Your Solution</span>**

```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        largest=0
        while left<right:
            l=right-left
            h=min(heights[left],heights[right])
            if l*h>largest:
                largest=l*h
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return largest
```

Your approach uses the **Two Pointer Technique**, which is the **optimal solution**.

---

# **<span style="color:#ffd166">Approach Used</span>**

The area of water between two lines is:

```text
area = width × min(height_left, height_right)
```

Where:

```text
width = right - left
```

You start with:

```text
left pointer → beginning
right pointer → end
```

This gives the **maximum possible width initially**.

Then you move pointers strategically to search for a larger area.

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
left = 0
right = n - 1
max_area = 0

while left < right:

    width = right - left
    height = min(height[left], height[right])

    area = width * height

    update max_area

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

return max_area
```

---

# **<span style="color:#00d2d3">Concept Used</span>**

## **Two Pointer Optimization**

Brute force would check **every pair of lines**.

```text
for i in range(n):
    for j in range(i+1,n):
```

Total pairs:

```text
n(n-1)/2
```

Complexity:

```text
O(n²)
```

But the **two pointer trick reduces the search space**.

---

# **<span style="color:#feca57">Key Insight of the Algorithm</span>**

The area depends on:

```text
1. Width
2. Smaller height
```

Example:

```
height_left = 2
height_right = 8
width = 10
```

Area:

```
2 × 10 = 20
```

Even if the right height is very large, the **shorter line limits the container**.

Therefore:

```text
min(height_left, height_right)
```

controls the area.

---

# **<span style="color:#ff9f43">Why We Move the Smaller Pointer</span>**

Suppose:

```
height[left] < height[right]
```

Then:

```
area = width × height[left]
```

Moving the **right pointer inward** would reduce width but keep the same limiting height.

Area would only decrease.

So the only chance to improve the area is:

```text
increase the smaller height
```

Thus we move:

```
left pointer
```

---

# **<span style="color:#48dbfb">Dry Run Example</span>**

```
heights = [1,8,6,2,5,4,8,3,7]
```

Initial:

```
left = 0
right = 8
```

Area:

```
width = 8
height = min(1,7) = 1
area = 8
```

Move left.

---

Next:

```
left = 1
right = 8
```

Area:

```
width = 7
height = min(8,7) = 7
area = 49
```

Largest so far:

```
49
```

Continue moving pointers until they meet.

---

# **<span style="color:#1dd1a1">Time Complexity</span>**

Each pointer moves **at most n times**.

So total operations:

```
O(n)
```

This is optimal.

---

# **<span style="color:#ff6b6b">Space Complexity</span>**

Only a few variables are used.

```
O(1)
```

Constant extra space.

---

# **<span style="color:#54a0ff">Rating Your Solution</span>**

| Category            | Rating     |
| ------------------- | ---------- |
| Correctness         | ⭐⭐⭐⭐⭐ |
| Optimality          | ⭐⭐⭐⭐⭐ |
| Pattern recognition | ⭐⭐⭐⭐⭐ |
| Code clarity        | ⭐⭐⭐⭐   |

Overall:

```
9.5 / 10
```

This is **exactly the expected interview solution**.

---

# **<span style="color:#f368e0">Other Approaches</span>**

## **Brute Force**

Check every pair of lines.

```
for i in range(n):
    for j in range(i+1,n):
        area = (j-i)*min(height[i],height[j])
```

Time complexity:

```
O(n²)
```

Too slow for large input.

---

# **<span style="color:#ff9ff3">LeetCode Problems With Similar Pattern</span>**

Two-pointer pattern appears in many problems:

1. Container With Most Water
2. Two Sum II (Sorted array)
3. 3Sum
4. Remove Duplicates from Sorted Array
5. Valid Palindrome
6. Trapping Rain Water
7. Move Zeroes

---

# **<span style="color:#00d2d3">Practice Questions With Same Pattern</span>**

These problems use **similar pointer movement logic**.

### Question 1

Find **two numbers in a sorted array whose sum equals target**.

---

### Question 2

Remove duplicates from a sorted array **in-place**.

---

### Question 3

Find **three numbers whose sum equals zero**.

---

### Question 4

Check if a string is a **valid palindrome using two pointers**.

---

### Question 5

Compute trapped rainwater between bars.

---

# **<span style="color:#a29bfe">Key Pattern Recognition</span>**

Whenever you see problems with:

```
array
two elements forming some value
sorted structure
max/min pair optimization
```

Think:

```
Two Pointer Technique
```

This pattern reduces **O(n²) brute force problems to O(n)**.

---

If you'd like, I can also show you something extremely useful:

**How to instantly recognize when a problem can be solved with two pointers instead of nested loops.**
**<span style="color:#ff6b6b">Problem: Container With Most Water</span>**

You are given an array `heights` where each element represents a vertical line.

Two lines form a **container**, and the container can hold water equal to:

```text
width × minimum height
```

Example:

```text
heights = [1,8,6,2,5,4,8,3,7]
```

The maximum area formed is:

```text
49
```

---

# **<span style="color:#4ecdc4">Your Solution</span>**

```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        largest=0
        while left<right:
            l=right-left
            h=min(heights[left],heights[right])
            if l*h>largest:
                largest=l*h
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return largest
```

Your approach uses the **Two Pointer Technique**, which is the **optimal solution**.

---

# **<span style="color:#ffd166">Approach Used</span>**

The area of water between two lines is:

```text
area = width × min(height_left, height_right)
```

Where:

```text
width = right - left
```

You start with:

```text
left pointer → beginning
right pointer → end
```

This gives the **maximum possible width initially**.

Then you move pointers strategically to search for a larger area.

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
left = 0
right = n - 1
max_area = 0

while left < right:

    width = right - left
    height = min(height[left], height[right])

    area = width * height

    update max_area

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

return max_area
```

---

# **<span style="color:#00d2d3">Concept Used</span>**

## **Two Pointer Optimization**

Brute force would check **every pair of lines**.

```text
for i in range(n):
    for j in range(i+1,n):
```

Total pairs:

```text
n(n-1)/2
```

Complexity:

```text
O(n²)
```

But the **two pointer trick reduces the search space**.

---

# **<span style="color:#feca57">Key Insight of the Algorithm</span>**

The area depends on:

```text
1. Width
2. Smaller height
```

Example:

```
height_left = 2
height_right = 8
width = 10
```

Area:

```
2 × 10 = 20
```

Even if the right height is very large, the **shorter line limits the container**.

Therefore:

```text
min(height_left, height_right)
```

controls the area.

---

# **<span style="color:#ff9f43">Why We Move the Smaller Pointer</span>**

Suppose:

```
height[left] < height[right]
```

Then:

```
area = width × height[left]
```

Moving the **right pointer inward** would reduce width but keep the same limiting height.

Area would only decrease.

So the only chance to improve the area is:

```text
increase the smaller height
```

Thus we move:

```
left pointer
```

---

# **<span style="color:#48dbfb">Dry Run Example</span>**

```
heights = [1,8,6,2,5,4,8,3,7]
```

Initial:

```
left = 0
right = 8
```

Area:

```
width = 8
height = min(1,7) = 1
area = 8
```

Move left.

---

Next:

```
left = 1
right = 8
```

Area:

```
width = 7
height = min(8,7) = 7
area = 49
```

Largest so far:

```
49
```

Continue moving pointers until they meet.

---

# **<span style="color:#1dd1a1">Time Complexity</span>**

Each pointer moves **at most n times**.

So total operations:

```
O(n)
```

This is optimal.

---

# **<span style="color:#ff6b6b">Space Complexity</span>**

Only a few variables are used.

```
O(1)
```

Constant extra space.

---

# **<span style="color:#54a0ff">Rating Your Solution</span>**

| Category            | Rating     |
| ------------------- | ---------- |
| Correctness         | ⭐⭐⭐⭐⭐ |
| Optimality          | ⭐⭐⭐⭐⭐ |
| Pattern recognition | ⭐⭐⭐⭐⭐ |
| Code clarity        | ⭐⭐⭐⭐   |

Overall:

```
9.5 / 10
```

This is **exactly the expected interview solution**.

---

# **<span style="color:#f368e0">Other Approaches</span>**

## **Brute Force**

Check every pair of lines.

```
for i in range(n):
    for j in range(i+1,n):
        area = (j-i)*min(height[i],height[j])
```

Time complexity:

```
O(n²)
```

Too slow for large input.

---

# **<span style="color:#ff9ff3">LeetCode Problems With Similar Pattern</span>**

Two-pointer pattern appears in many problems:

1. Container With Most Water
2. Two Sum II (Sorted array)
3. 3Sum
4. Remove Duplicates from Sorted Array
5. Valid Palindrome
6. Trapping Rain Water
7. Move Zeroes

---

# **<span style="color:#00d2d3">Practice Questions With Same Pattern</span>**

These problems use **similar pointer movement logic**.

### Question 1

Find **two numbers in a sorted array whose sum equals target**.

---

### Question 2

Remove duplicates from a sorted array **in-place**.

---

### Question 3

Find **three numbers whose sum equals zero**.

---

### Question 4

Check if a string is a **valid palindrome using two pointers**.

---

### Question 5

Compute trapped rainwater between bars.

---

# **<span style="color:#a29bfe">Key Pattern Recognition</span>**

Whenever you see problems with:

```
array
two elements forming some value
sorted structure
max/min pair optimization
```

Think:

```
Two Pointer Technique
```

This pattern reduces **O(n²) brute force problems to O(n)**.

---

If you'd like, I can also show you something extremely useful:

**How to instantly recognize when a problem can be solved with two pointers instead of nested loops.**
**<span style="color:#ff6b6b">Problem: Container With Most Water</span>**

You are given an array `heights` where each element represents a vertical line.

Two lines form a **container**, and the container can hold water equal to:

```text
width × minimum height
```

Example:

```text
heights = [1,8,6,2,5,4,8,3,7]
```

The maximum area formed is:

```text
49
```

---

# **<span style="color:#4ecdc4">Your Solution</span>**

```python
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        largest=0
        while left<right:
            l=right-left
            h=min(heights[left],heights[right])
            if l*h>largest:
                largest=l*h
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return largest
```

Your approach uses the **Two Pointer Technique**, which is the **optimal solution**.

---

# **<span style="color:#ffd166">Approach Used</span>**

The area of water between two lines is:

```text
area = width × min(height_left, height_right)
```

Where:

```text
width = right - left
```

You start with:

```text
left pointer → beginning
right pointer → end
```

This gives the **maximum possible width initially**.

Then you move pointers strategically to search for a larger area.

---

# **<span style="color:#a29bfe">Pseudocode</span>**

```
left = 0
right = n - 1
max_area = 0

while left < right:

    width = right - left
    height = min(height[left], height[right])

    area = width * height

    update max_area

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

return max_area
```

---

# **<span style="color:#00d2d3">Concept Used</span>**

## **Two Pointer Optimization**

Brute force would check **every pair of lines**.

```text
for i in range(n):
    for j in range(i+1,n):
```

Total pairs:

```text
n(n-1)/2
```

Complexity:

```text
O(n²)
```

But the **two pointer trick reduces the search space**.

---

# **<span style="color:#feca57">Key Insight of the Algorithm</span>**

The area depends on:

```text
1. Width
2. Smaller height
```

Example:

```
height_left = 2
height_right = 8
width = 10
```

Area:

```
2 × 10 = 20
```

Even if the right height is very large, the **shorter line limits the container**.

Therefore:

```text
min(height_left, height_right)
```

controls the area.

---

# **<span style="color:#ff9f43">Why We Move the Smaller Pointer</span>**

Suppose:

```
height[left] < height[right]
```

Then:

```
area = width × height[left]
```

Moving the **right pointer inward** would reduce width but keep the same limiting height.

Area would only decrease.

So the only chance to improve the area is:

```text
increase the smaller height
```

Thus we move:

```
left pointer
```

---

# **<span style="color:#48dbfb">Dry Run Example</span>**

```
heights = [1,8,6,2,5,4,8,3,7]
```

Initial:

```
left = 0
right = 8
```

Area:

```
width = 8
height = min(1,7) = 1
area = 8
```

Move left.

---

Next:

```
left = 1
right = 8
```

Area:

```
width = 7
height = min(8,7) = 7
area = 49
```

Largest so far:

```
49
```

Continue moving pointers until they meet.

---

# **<span style="color:#1dd1a1">Time Complexity</span>**

Each pointer moves **at most n times**.

So total operations:

```
O(n)
```

This is optimal.

---

# **<span style="color:#ff6b6b">Space Complexity</span>**

Only a few variables are used.

```
O(1)
```

Constant extra space.

---

# **<span style="color:#54a0ff">Rating Your Solution</span>**

| Category            | Rating     |
| ------------------- | ---------- |
| Correctness         | ⭐⭐⭐⭐⭐ |
| Optimality          | ⭐⭐⭐⭐⭐ |
| Pattern recognition | ⭐⭐⭐⭐⭐ |
| Code clarity        | ⭐⭐⭐⭐   |

Overall:

```
9.5 / 10
```

This is **exactly the expected interview solution**.

---

# **<span style="color:#f368e0">Other Approaches</span>**

## **Brute Force**

Check every pair of lines.

```
for i in range(n):
    for j in range(i+1,n):
        area = (j-i)*min(height[i],height[j])
```

Time complexity:

```
O(n²)
```

Too slow for large input.

---

# **<span style="color:#ff9ff3">LeetCode Problems With Similar Pattern</span>**

Two-pointer pattern appears in many problems:

1. Container With Most Water
2. Two Sum II (Sorted array)
3. 3Sum
4. Remove Duplicates from Sorted Array
5. Valid Palindrome
6. Trapping Rain Water
7. Move Zeroes

---

# **<span style="color:#00d2d3">Practice Questions With Same Pattern</span>**

These problems use **similar pointer movement logic**.

### Question 1

Find **two numbers in a sorted array whose sum equals target**.

---

### Question 2

Remove duplicates from a sorted array **in-place**.

---

### Question 3

Find **three numbers whose sum equals zero**.

---

### Question 4

Check if a string is a **valid palindrome using two pointers**.

---

### Question 5

Compute trapped rainwater between bars.

---

# **<span style="color:#a29bfe">Key Pattern Recognition</span>**

Whenever you see problems with:

```
array
two elements forming some value
sorted structure
max/min pair optimization
```

Think:

```
Two Pointer Technique
```

This pattern reduces **O(n²) brute force problems to O(n)**.

---

If you'd like, I can also show you something extremely useful:

**How to instantly recognize when a problem can be solved with two pointers instead of nested loops.**
