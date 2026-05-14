'''
reverse a string:
Example:

Input: "hello"
Output: "olleh"

RULES

❌ Don’t use:

[::-1]

❌ Don’t use:

reversed()
'''
s='hello'
rev=""
for ch in s:
    # don't do this rev=rev+ch
    rev=ch+rev
print(rev)