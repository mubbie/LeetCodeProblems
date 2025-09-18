# Question

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.

## Solution

### Questions

1. Can we assume the strings are exactly the same length?
    - If they're not equal length, we can immediately return False as they cannot be anagrams.
2. What character set are we dealing with? ASCII, Unicode, etc.?
    - If ASCII, we can use a fixed-size array of length 26 to keep track of character counts. A good solution is to create an array of size 26 initialized to zero, then iterate over the first string and increment the counter for each character (increment at index `ord(char) - ord('a')` - that is the ASCII value of the character less the ASCII value of `a`). Finally, iterate over the second string and decrement the counter for each character in the string from the array. If before decrementing, the counter is already zero, we can return False. If we finish iterating through both strings and all counters are zero, we can return True.
    - If Unicode, we may need to use a dictionary or hashmap to count character occurrences. In this case, we can use a more general solution.
3. Are the strings case-sensitive?
    - If not, we should convert both strings to the same case (either upper or lower) before processing.
    - To do this in python, we can use the `lower()` or `upper()` string methods.
4. Can the strings contain spaces or special characters?
    - If yes, should we consider them in our character count.

### Python

Python has a data structure to keep track of frequencies, [Counter](https://docs.python.org/3/library/collections.html#collections.Counter).

The time complexity, would be:

- O(n) to create the frequency count for the first string.
- O(m) to create the frequency count for the second string.
- O(k) to compare the two frequency counts, where k is the number of unique characters (Python compares the lengths of the two Counters first, which is O(1) if they are not equal. If they are equal, it iterates over each key/value in the first counter to see if they are in the second counter).
- O(1) for the space complexity, as we are using a fixed-size data structure (the Counter) that does not grow with the input size.
- Overall, the time complexity is O(n + m + k), which simplifies to O(n + m) in the worst case where all characters are unique. The space complexity is O(1) since the size of the Counter is bounded by the character set (e.g., 26 for lowercase English letters).

An better solution:

- Iterate through the items in the first string and create a frequency count using a dictionary.
- Iterate through the items in the second string and decrement the frequency count in the dictionary.
- If we find a character in the second string where the count in the dictionary is already zero or the character does not exist in the dictionary, we can return False.
- Finally, if we finish iterating through both strings and all counts in the dictionary are zero, we can return True.

The time/space complexity will be:

- O(n) to create the frequency count for the first string.
- O(m) to decrement the frequency count for the second string.
- O(1) for the space complexity, as we are using a fixed-size data structure (the dictionary) that does not grow with the input size.
- Overall, the time complexity is O(n + m), and the space complexity is O(1) since the size of the dictionary is bounded by the character set (e.g., 26 for lowercase English letters).
