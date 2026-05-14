'''
Write code to check if a string is palindrome.
Option 1:
 reverse string
 compare with original
Option 2 (advanced thinking):
 compare left and right characters
'''

s=input('Enter the string: ')
s = s.lower()   # normalize case
rev=''
for ch in s:
    rev=ch+rev

if rev==s:
    print('Yes,given string is a palindrome ')
else:
    print('No,given string is not a palindrome ')

'''
Doubt: how s = s.lower() works even when strings 
are immutable 
solution:
Note:
Strings are immutable in Python.
s = s.lower() does NOT modify the original string.
It creates a NEW string and assigns it back to s.

'''