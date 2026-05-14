'''
Count vowels in a string
Write code to:

traverse a string
check if character is vowel
count total vowels

Hints 😏:

use loop
use:
if ch in "aeiou"
'''
s=input('enter a string: ')
vowels=0
for ch in s:
    if ch in "aeiou":
        vowels+=1
print("no of vowels in the given string is: ",vowels)