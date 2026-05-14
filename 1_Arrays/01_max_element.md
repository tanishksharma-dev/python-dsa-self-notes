# Topic: Finding Maximum in a List (Basic DSA)

Given a list of integers, find the maximum element without using built-in functions like max() or sort().

## Idea / Logic (MOST IMPORTANT PART)

- Assume first element is the largest
- Traverse the list one by one
- Compare each element with current maximum
- Update maximum if a larger value is found
- (These bullet points matter more than code.)

- CODE:
```python
arr = [4, 2, 9, 1, 7]

mx = arr[0]

for i in arr:
    if i > mx:
        mx = i

print(mx)
```
- Time & Space Complexity (NOTE THIS)

Time Complexity: O(n)
Space Complexity: O(1)
I’ll explain these slowly later, but start noting them from day 1. Future you will thank me.

