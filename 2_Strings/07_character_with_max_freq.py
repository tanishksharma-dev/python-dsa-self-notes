'''
Find Character with Maximum Frequency
Example:
Input: "success"

Output:
s -> 3

bcz s appears maximum times
'''
#my try 

'''s="hello"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1


for key in freq:
    if key'''

s = input("Enter a string: ")

freq = {}

# Creating frequency dictionary
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

max_char = ""
max_count = 0

# Finding character with maximum frequency
for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        max_char = key

print("Character with maximum frequency is:", max_char)
print("Frequency is:", max_count)