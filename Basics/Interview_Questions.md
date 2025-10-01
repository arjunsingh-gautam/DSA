# 🔹 **A Priori Analysis (theory-based algorithm analysis)**

📌 _Definition Reminder:_
A priori analysis = analyzing an algorithm’s efficiency **before implementation** (mathematical model, independent of machine).

---

### ✅ Common Interview Questions

1. **What is a priori analysis? How is it different from a posteriori analysis?**

   - Expected answer: _A priori analysis studies the efficiency of algorithms theoretically (before coding), while a posteriori analysis measures actual performance after implementation._

2. **Why do we need a priori analysis?**

   - Possible talking points:

     - To predict algorithm performance without relying on machine or compiler.
     - To compare algorithms on growth rate, not hardware factors.

3. **What parameters are considered in a priori analysis?**

   - Time complexity, space complexity, input size, data structure usage.

4. **Give an example of a priori analysis for a simple algorithm.**

   - Eg: For loop from `1 to n` → runtime grows linearly → O(n).

5. **What are the limitations of a priori analysis?**

   - Doesn’t capture cache effects, memory hierarchy, or compiler optimizations.
   - May differ from real-world execution (a posteriori).

6. **In interviews:**

   - They might ask you to analyze a new algorithm using a priori approach (derive time complexity step by step, not by running code).

---

# 🔹 **Asymptotic Notations (Big O, Ω, Θ)**

📌 _Definition Reminder:_
They describe how runtime/space grows as input size `n → ∞`.

---

### ✅ Common Interview Questions

1. **Define Big O, Omega, and Theta notations.**

   - Be ready with _formal definitions + intuitive explanation + example._

2. **Why do we need asymptotic notations instead of actual execution time?**

   - Hardware/implementation differs → asymptotic gives machine-independent measure.

3. **Give an example where Big O and Omega are different.**

   - Linear search: O(n), Ω(1).

4. **When do we say an algorithm is Θ(f(n))?**

   - When both upper and lower bounds are the same.

5. **Explain the importance of asymptotic analysis in algorithm design.**

   - Helps compare efficiency in long run, avoids dependence on constants.

6. **Why do we ignore constants and lower-order terms in Big O?**

   - Because as n grows large, higher-order terms dominate growth rate.

7. **What are some common complexity classes and their meanings?**

   - O(1), O(log n), O(n), O(n log n), O(n²), O(2ⁿ), O(n!).

8. **How do you calculate time complexity of a nested loop?**

   - Multiply iterations: e.g., two nested loops from 1 to n → O(n²).

9. **What is the difference between worst-case, average-case, and best-case complexities?**

   - Worst → O, Best → Ω, Average → Expected analysis.

10. **Trick Interview Q:**

- _If an algorithm has best case Ω(n), worst case O(n²), can we say it’s Θ(n)?_
- Answer: No. Θ exists only if both bounds match.

---

# 🔹 **How to Prepare for These in Interviews**

- Be ready to **explain definitions simply** (not just formulas).
- Always provide a **real example** (like linear search, binary search, merge sort).
- Interviewers often push: “Why?” — so be ready with **intuition** (e.g., why constants don’t matter).
- Practice writing runtime bounds for small code snippets.

---
