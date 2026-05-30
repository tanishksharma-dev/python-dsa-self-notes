arr=list(map(int,input("enter array: ").split()))
target=int(input("Enter the target: "))
found=False

for num in arr:
    if num == target:
        found=True
        break 

if found:
    print('yes, the array contain the target element')

else:
    print('No, the array doesn\'t contain the target element')
    