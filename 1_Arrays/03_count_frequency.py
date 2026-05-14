#Given a list of integers and a number x, 
#count how many times x appears in the list.
arr = [1, 2, 3, 2, 4, 2, 5]
x=2
#output = 3
counter=0
for i in arr:
    if i==x:
        counter+=1
print(counter)

#yup ur code is 100% correct 😭 w

'''
Does this code work for 1 lakh elements?
Answer: YES
Time taken grows linearly with 
size → this is called O(n)

Is sorting needed for frequency count?
No
Counting directly is smarter + faster.
'''
