'''Count frequency of each character in a string.

Input: "hello"
Example:
Output:
h -> 1
e -> 1
l -> 2
o -> 1
'''
s = input("Enter string: ")

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)