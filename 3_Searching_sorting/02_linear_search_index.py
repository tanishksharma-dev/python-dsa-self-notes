#my try(CORRECT )
arr=list(map(int,input("enter array: ").split()))

target=int(input("Enter the target: "))

found=False

for i in range(0,len(arr)):
    if arr[i] == target:
        found=True
        break 

if found:
    print('yes, the array contain the target element at index ',i)

else:
    print('No, the array doesn\'t contain the target element')

'''you don’t even need:

found=True

You could directly:

print(...)
break

Time Complexity?

Worst case:
👉 O(n)

Still checking array linearly.
'''
