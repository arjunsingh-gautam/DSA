# <span style="color:yellow">**What is an Algorithm?**</span>

At its simplest:
👉 An **algorithm** is a **finite, step-by-step procedure** to solve a problem or accomplish a task.

Think of it like a **recipe**:

- Input: raw ingredients
- Procedure: mixing, heating, timing, stirring
- Output: final dish

Not every block of code is an algorithm — some are just _statements without structure_.

---

## **Properties of a True Algorithm**

For a block of instructions to be considered an algorithm, it must have these properties:

1. **Input** – It should accept 0 or more inputs.
2. **Output** – It should produce at least 1 output/result.
3. **Finiteness** – Must terminate after a finite number of steps.
   (e.g., “keep doing forever” is _not_ an algorithm).
4. **Definiteness** – Each step should be _clear, unambiguous, precise_.
   (no vague instructions like “do something smart”).
5. **Effectiveness** – Every step should be basic enough that it can be carried out with available resources.

---

## **Example: Algorithm for “Find Maximum in Array”**

### Problem:

Given an array of `n` integers, find the maximum element.

### Steps (Algorithm design):

1. Start with the first element as `max`.
2. For each element in the array:

   - If the element > `max`, update `max`.

3. After scanning all elements, output `max`.

👉 Properties check:

- Input: an array of integers
- Output: one integer (maximum)
- Finiteness: loop ends after n steps
- Definiteness: each step is clear
- Effectiveness: easy to execute

---

## **Methodology to Design an Algorithm (Step-by-Step)**

Whenever you face a new task:

1. **Understand the Problem Clearly**

   - What are inputs?
   - What is required output?
   - Constraints (size, limits, time)?

2. **Break it Down into Steps**

   - Think logically in plain language or pseudocode.
   - Avoid jumping into code immediately.

3. **Choose a Strategy**

   - Brute force? Greedy? Divide & conquer? Dynamic programming?

4. **Analyze Complexity**

   - Time & space cost (Big-O).
   - Is it efficient enough?

5. **Test on Edge Cases**

   - Empty input, large input, negatives, duplicates.

6. **Convert to Code**

   - Write clean, modular Python.

7. **Debug & Optimize**

   - Fix mistakes, look for faster approaches.

---

## **What is _NOT_ an Algorithm?**

- A single code snippet like:

  ```python
  x = x + 1
  ```

  (This doesn’t solve a complete problem.)

- Infinite loops without termination.

- Vague instructions like:
  “Sort this somehow” or “find the biggest cleverly”

- Code without clear input/output relation.

---

## **Best Practices for Algorithms**

- **Clarity first, code later** → Write steps in pseudocode before coding.
- **Modular design** → Break tasks into smaller helper algorithms.
- **Check correctness before optimization**.
- **Think edge cases early**.
- **Consistency in notation** (variables, pseudocode format).
- **Iterate & improve** → first brute force, then optimize.

---

## Quick Example (Design Together)

Task: **Check if a string is a palindrome**

👉 Let’s outline an algorithm (without coding yet):

1. Take the string `s`.
2. Set two pointers: `left = 0`, `right = len(s) - 1`.
3. While `left < right`:

   - If `s[left] != s[right]` → return False.
   - Else, move inward (`left++`, `right--`).

4. If loop finishes, return True.

✅ Has input, output, finite steps, precise, effective.
Now we can code it.

---
