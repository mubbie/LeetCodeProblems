# Question

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

## Solution

The ideas here is to target O(n) time and space complexity.

Iterate over the list and keep track of the elements we've seen so far using a dictionary.

The iteration is O(n) in the worst case. The space complexity is also O(n) in the worst case, as we may end up storing all elements in the dictionary.

Once we find an item in the list that is already a key in the dictionary, we can immediately return True, indicating that a duplicate exists. If we finish iterating through the list without finding any duplicates, we return False.

### Python

Here we can use a regular [python dict](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### Java

Here we can use a HashSet or a HashMap to keep track of duplicates: [Difference between HashMap and HashSet](https://www.geeksforgeeks.org/java/difference-between-hashmap-and-hashset/), [Java Util HashMap Examples](https://www.geeksforgeeks.org/java/java-util-hashmap-in-java-with-examples/), [HashSet in Java](https://www.geeksforgeeks.org/java/hashset-in-java/)
