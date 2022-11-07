# Problem: https://leetcode.com/problems/two-sum/
# Leetcode Easy

# thinking:
# input -> array of integers, integer (target)
# output -> indices of integers in the array that sum to the target

# example:
# nums = [2, 7, 11, 15]
# target = 9
# output = [0, 1]
# why: 0: 2; 1: 7; sum to 1

# brute force
# iterate through the array
# for each item, iterate through the array again
# when a sum is found, return it
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        BRUTE FORCE SOLUTION
        :param nums: array of integer
        :param target: integer
        :return: the indices of integers in the array that sum to the target

        TIME COMPLEXITY:
            Worst case: O(n^2) as we need to iterate through the list twice
        """
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# follow up: more efficient solution
# can you come up with an algorithm that is less than O(n^2)?

# thinking:
    # have a dictionary
    # iterate through the list
        # compute the required difference
        # if the difference is in the dictionary
        # return the indices

class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
            BRUTE FORCE SOLUTION
            :param nums: array of integer
            :param target: integer
            :return: the indices of integers in the array that sum to the target

            TIME COMPLEXITY (https://wiki.python.org/moin/TimeComplexity):
                - Loop (O(n))
                - item in dict: for `in` operators on dict and set in python complexity is O(1) on average
                Thus, we can estimate that the worst case here is O(n)
        """
        items = dict()  # dict: mapping `items in nums` to their corresponding index

        for i in range(0, len(nums)):  # iterate through the list
            diff = target - nums[i]  # difference between current item and target
            if diff in items:
                # if the difference is in the map, then we have found the other
                # candidate for the two sum
                return [i, items[diff]]
            else:
                # if not, we add the item we just saw to the map
                # mapping: item -> it's index
                items[nums[i]] = i


"""
    LEARNING:
    enumerate in python
    for instance, see below
"""

testList = [1, 2, 3, 4, 5]  # test list

for a, b in enumerate(testList):
    # expect indices vs items
    print("Index:", a, "; Value,", b)

    """
        OUTPUT:
        Index: 0 ; Value, 1
        Index: 1 ; Value, 2
        Index: 2 ; Value, 3
        Index: 3 ; Value, 4
        Index: 4 ; Value, 5
    """

"""
    Learning:
        - the second solution should theoretically be faster 
        
        - but here are the results of running it on LeetCode
        - taking a sample of 5 on the input:
            - num = [2, 7, 11, 15]
            - target = 9
        
        Solution 1 (Time to Run): 55 ms, 60 ms, 69 ms, 68 ms, 51 ms
        Solution 2 (Time to Run): 71 ms, 57 ms, 58 ms, 46 ms, 70 ms
"""