# Searching

Searching means finding an element in a collection.

---

## Linear Search

Checks elements one by one.

Works on:
- sorted arrays
- unsorted arrays

---

### Steps

1. Traverse array
2. Compare each element with target
3. If found:
   return/index/print
4. Else:
   element not found

---

### Time Complexity

Best Case:
O(1)
(target found at first position)

Worst Case:
O(n)
(target at end or absent)

---

### Space Complexity

O(1)

---

### Important Concepts Used

- loop traversal
- condition checking
- break
- boolean flag

### Input syntax

arr = list(map(int, input().split()))

## Linear Search using Index

Instead of traversing elements directly,
we traverse indexes.

Example:
for i in range(len(arr))

'''2 types of traversing
1. direct:
   for num in arr:
      (Gets values directly.)
2. Index traversal:
   for i in range(len(arr)):
      (Gets positions/indexes.)
'''

## Binary Search

Binary Search works only on sorted arrays.

Instead of checking elements one-by-one,
it checks middle element and eliminates half of the search space.

---
### 🧠 Small important note

i used:

arr.sort()
BUT in interviews/questions:
usually they say:

given sorted array

because sorting itself costs:

O(n log n)
---

### Important Variables

low → starting index

high → ending index

mid → middle index

Formula:
mid = (low + high)//2

*Conditions*

If target > arr[mid]:
search right half

low = mid + 1

If target < arr[mid]:
search left half

high = mid - 1

*Complexity*

Time Complexity:
O(log n)

Space Complexity:
O(1)

## Binary Search using Index

If target is found:
`mid` stores the index position.

Example:
```python
print(mid)
