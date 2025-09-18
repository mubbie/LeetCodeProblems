# Question

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Example 1:
Input:
[3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000

## Solution

### Questions

1. Are we guaranteed to always have a solution for the list?
   - If no,
     - Then we can have empty array inputs
   - If yes,
     - Then if the array size is less than 2, return empty array
  
### Python

The naive solution (brute force) would be the iterate over the array with two nested loops, and checking if the sum of the two numbers is equal to the target. If it is, return the indices of the two numbers. This would be O(n^2) time complexity.

A better solution would be to:

- Create a dictionary to store the numbers we have seen so far and their indices (Use dictionary because lookup is O(1))
- Iterate through the array, and think of the solution in terms of the equation `nums[i] + nums[j] = target`, which rearranged becomes `nums[j] = target = nums[i]`
- For each number, calculate the complement (i.e., `target - nums[i]`)
- Check if the complement is in the dictionary
- If it is, return the indices of the current number and the complement
- If it is not, add the current number and its index to the dictionary

#### Analysis

- Time complexity: O(n) because we iterate over the array
- Space complexity: O(n) because we store the number in a dictionary (worst case, we store all the numbers in the array)
