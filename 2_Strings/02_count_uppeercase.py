'''
Count uppercase letters
Hint:
Python has:
ch.isupper()
'''
#my try:
s='heLlO'
upper=0
for ch in s:
    if ch.isupper()==True:
        upper+=1
print(upper)
#correct but i dont't need == True bcz ch.isupper
#already returns True/False 