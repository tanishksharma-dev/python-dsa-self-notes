'''Given a list, 
reverse it without using reverse() or slicing.
2 methods:
1) create a new list and fill it 
2) reverse in place(harder , optional)

'''
#code:
arr = [1, 2, 3, 4, 5]
rev = []

for i in range(len(arr)-1, -1, -1):
    rev.append(arr[i])

print(rev)

'''
🧠 Note for range(start, stop, step)
start → starting index
stop → ending index (not included)
step → movement of index
sign (+ / -) = direction
value = jump size

👉 Example: range(4, -1, -1) = go from last
 index to 0
'''


