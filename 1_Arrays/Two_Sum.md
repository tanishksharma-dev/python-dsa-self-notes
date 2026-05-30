## Two Sum (HashMap)

Idea:
For each number:
1. Find the required complement = target - current_number
2. Check if complement already exists in hashmap
3. If yes, return both indexes
4. Otherwise store current number and its index

Time Complexity: O(n)
Space Complexity: O(n)

Common Mistake:
- Putting hashmap insertion inside the `if` block.
- Current number should be stored when complement is NOT found.
