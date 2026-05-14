'''
Check if Two Strings are Anagrams
Two strings are anagrams if:
👉 they contain same characters with same frequencies.
Example:
listen
silent

Both contain:

l,i,s,t,e,n
same counts.
'''
#my try(100% correct 😭)
s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

# Optimization:
# If lengths are different,
# strings cannot be anagrams
if len(s1) != len(s2):
    print("No, not anagram")

else:
    freq1 = {}
    freq2 = {}

    # Frequency dictionary for first string
    for ch1 in s1:
        if ch1 in freq1:
            freq1[ch1] += 1
        else:
            freq1[ch1] = 1

    # Frequency dictionary for second string
    for ch2 in s2:
        if ch2 in freq2:
            freq2[ch2] += 1
        else:
            freq2[ch2] = 1

    # Compare dictionaries
    if freq1 == freq2:
        print("Yes, both strings are anagram")
    else:
        print("No, not anagram")

