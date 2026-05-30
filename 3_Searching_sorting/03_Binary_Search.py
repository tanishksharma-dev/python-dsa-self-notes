'''
Binary Search ONLY works on:
sorted arrays
Instead of checking one-by-one:
👉go to MIDDLE element first.
Then:
eliminate HALF the array instantly.
That’s why complexity becomes:
O(log n), it was O(n) in linear search

in the code:
low means:
starting index of current search range.
'''
arr = list(map(int, input("Enter array: ").split()))

# arr.sort() [not needed, given array is already sorted ]

target = int(input("Enter the target: "))

low = 0
high = len(arr)-1

found = False

while low <= high:

    mid = (low + high)//2

    if arr[mid] == target:
        found = True
        break

    elif target > arr[mid]:
        low = mid + 1

    else:
        high = mid - 1

if found:
    print("Element found")

else:
    print("Element not found")
