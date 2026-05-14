#Given a list of integers, check whether
#  it is sorted in non-decreasing (ascending) order.

'''
my solution:
arr1=[1,4,6,41,55]
for i in arr1:
    if i<=i+1:
        print('sorted') 
this is wrong bcz ur literally checking i<=i+1 
which will always be true
'''
arr1 = [1, 4, 6, 41, 55]

is_sorted = True

for i in range(len(arr1) - 1):
    if arr1[i] > arr1[i + 1]:
        is_sorted = False
        break

print(is_sorted)

#output True
