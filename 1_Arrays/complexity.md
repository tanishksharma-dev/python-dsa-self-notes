# Time Complexity

## Meaning
Time Complexity tells how running time grows with input size.

Input size = n

---

## Common Complexities

O(1) → constant
O(n) → linear
O(n²) → nested loops
O(log n) → input halves each step

---

## Rules

1. One loop → O(n)

2. Nested loops → O(n²)

3. Separate loops:
O(n)+O(n)=O(n)

4. Ignore constants:
O(2n)=O(n)

5. Keep highest growing term:
O(n²+n)=O(n²)

---

## Examples

Single loop:
O(n)

Nested loop:
O(n²)

Binary search:
O(log n)

---

## Space Complexity

Extra memory used by program.

Extra array/string:
O(n)

No extra structure:
O(1)