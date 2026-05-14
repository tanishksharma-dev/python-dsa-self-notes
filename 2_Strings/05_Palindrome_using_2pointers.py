'''
Instead of:

making reverse string ❌

We directly compare:

left side
right side
'''
s = input("Enter string: ")
s = s.lower()

left = 0
right = len(s) - 1

is_palindrome = True

while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print("Yes, palindrome")
else:
    print("No, not palindrome")


'''
Why this is IMPORTANT
Before:
reverse string → O(n) extra space
Now:
no extra string
just comparisons
more efficient

👉 This is called:

Two Pointer Technique
'''