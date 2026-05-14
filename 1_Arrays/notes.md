# Arrays (Python Lists)

## Basics
- Arrays store multiple elements of same type
- Python uses lists for arrays

## Common Patterns

### 1. Finding Maximum / Minimum
Logic:
- Assume first element
- Traverse list
- Compare and update

Time Complexity: O(n)
Space Complexity: O(1)

### 2. Looping styles(i did this mistake in min_element.py)
- for i in arr → value
- for i in range(len(arr)) → index  

### Counting Frequency
- Initialize counter = 0
- Traverse array
- If element matches target, increment counter

Time Complexity: O(n)
Space Complexity: O(1)

### Reversing an Array (Using Extra List)
Logic:
- Create empty list
- Traverse original list from last index to first
- Append each element to new list

Time Complexity: O(n)
Space Complexity: O(n)

Note:
- Extra list approach is easier to understand
- In-place reverse saves memory but is trickier

### Check if Array is Sorted
Logic:
- Traverse array using indices
- Compare current element with next
- If any element > next → not sorted

Time Complexity: O(n)
Space Complexity: O(1)

- Trick:
for x in arr → use when you don’t need neighbors
for i in range(len(arr)) → use when index matters

