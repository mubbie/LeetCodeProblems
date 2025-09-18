# Question

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.

## Solution

### Questions

Input: Array of strings `strs`
Output: List of lists of strings, where each sublist contains anagrams

- Can the list be empty?
  - If yes, return an empty list of list
- Can the list have one element?
  - If yes, return a list with one sublist containing that element
- Are we considering case sensitivity?
  - If yes, "Eat" and "tea" are not anagrams
  - If no, convert all strings to lower case before processing
- Can the strings contain non-alphabetic characters?
  - If yes, consider them as part of the string when determining anagrams
  - If no, filter out non-alphabetic characters before processing (or assume input is already clean)
- What is the size of the input?
  - strs.length >= 1 (can't be empyt) and <= 1000
  - strs[i].length >= 1 and <= 100
  - strs[i] consists of lowercase English letters (no special characters or uppercase letters - this means the input is already clean)
- Can the list have duplicate strings?

### Implementation

#### Naive Solution

We can sort each string in the list and use the sorted string as a key in a dictionary.

- Create a dictionary to store the sorted string as the key and a list of anagrams as the value
- Iterate through the list of strings
- For each string, sort the characters in the string to create a new sorted string
- Check if the sorted string is already a key in the dictionary
  - If it is, append the original string to the list of anagrams for that key
  - If it is not, create a new key in the dictionary with the sorted string and set the value to a list containing the original string
- Finally, return the values of the dictionary as a list of lists
- The time complexity is O(n * m log m), where n is the number of strings in the list and m is the maximum length of a string in the list (because sorting each string takes O(m log m) time)

#### Better Solution

- We know that all the characters are lowercase English letters (a-z)
- We also know that valid anagrams will have the same character frequency for each character
- Hence, if we want to group anagrams, we can use the frequency of each character as the key in a dictionary

Thus, the solution would be list:

- Create dictionary mapping character frequency to a list of anagrams (In python, the key is a tuple of size 26, and we can create a `defaultdict` of lists to store the anagrams)
- Iterate through the list of strings
- For each string, create a frequency character array of size 26 initialized to zero
- For each character in the string, increment the corresponding index in the frequency array (index = `ord(char) - ord('a')`)
- Convert the frequency array to a tuple (to make it hashable) and use it as a key in the dictionary
- Check if the frequency tuple is already a key in the dictionary
  - If it is, append the original string to the list of anagrams for that key
  - If it is not, create a new key (Using `defaultdict`, this step is not necessary) in the dictionary with the frequency tuple and set the value to a list containing the original string
- Finally, return the values of the dictionary as a list of lists
