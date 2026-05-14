# Strings

## What is a String?
A string is a sequence of characters.

Example:
s = "hello"

Characters have indices:
h e l l o
0 1 2 3 4

## Important Difference
- Lists are mutable
- Strings are immutable

s[0] = "H"   ❌ ERROR (can't change characters directly)

## Count Vowels in a String

Logic:
- Traverse string character by character
- Check if character is vowel
- Increase counter

Code pattern:
if ch in "aeiou"

Time Complexity: O(n)
Space Complexity: O(1)

## Count Uppercase Letters

Logic:
- Traverse string
- Check each character using isupper()
- Increase counter

Useful function:
ch.isupper()

Time Complexity: O(n)
Space Complexity: O(1)

## Palindrome String

A string is palindrome if:
original == reverse

Logic:
- Reverse string manually
- Compare with original

Important:
Normalize case using .lower() for accurate comparison

## Palindrome (Two Pointer Method)

Logic:
- Use left and right pointers
- Compare characters
- Move inward

Benefit:
- No extra space used
- More efficient than reversing string

## Character Frequency using Dictionary

Dictionary stores:
key -> value

For frequency:
character -> count

Logic:
- If character already exists, increase count
- Otherwise add with count 1

freq[ch] += 1

means:

freq[ch] = freq[ch] + 1

freq[ch] = 1

If key does not exist:
- dictionary creates new key
- assigns value

Dictionaries are dynamic.

## Character with Maximum Frequency

### Logic

Step 1:
Create frequency dictionary.

Example:
hello

{
'h':1,
'e':1,
'l':2,
'o':1
}

Step 2:
Traverse dictionary and find maximum count.

### Important Concepts

Dictionary stores:
key -> value

For frequency problems:
character -> count

### Important Syntax

Create empty dictionary:
freq = {}

Check key exists:
if ch in freq

Increase value:
freq[ch] += 1

Create new key:
freq[ch] = 1

Traverse dictionary:
for key in freq

Access value using key:
freq[key]

### Logic for Maximum

Store:
max_char
max_count

Compare:
if freq[key] > max_count

Update both:
max_count = freq[key]
max_char = key

### Time Complexity
O(n)

### Space Complexity
O(n)

## Anagram Strings

Two strings are anagrams if:
- same characters
- same frequencies

Logic:
- Create frequency dictionaries for both strings
- Compare dictionaries

Important:
Dictionary comparison checks both keys and values.

Optimization:
If lengths are different,
strings cannot be anagrams.

Length check optimization improves best-case performance,
but worst-case time complexity still remains O(n).