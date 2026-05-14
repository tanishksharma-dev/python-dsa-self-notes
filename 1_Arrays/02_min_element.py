#trying to write the code myself 

'''l=[4, 2, 9, 1, 7]

min=l[0]
for i in l:
    if l[i]<min:
        min=l[i]

print(l[min])'''

#correct code:
l = [4, 2, 9, 1, 7]

mn = l[0]

for i in l:
    if i < mn:
        mn = i

print(mn)
