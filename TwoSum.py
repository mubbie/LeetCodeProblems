# Problem: https://leetcode.com/problems/two-sum/
# Leetcode Easy
import random


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
    @staticmethod
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
        
        - but this size might not be the best to test on
        - from chat with Ike: 
                Time complexity is a heuristic to determine how much the time 
                taken for the algorithm to run grows based on the input  
                
        - generate large lists (size 1000):
            a. [.., .., solution, solution]
            b. [.., solution, solution, ..]
            c. [solution, .., .., solution]
            d. [.., solution, .., solution, ..]   
"""

a = list()
b = list()
c = list()
d = list()

# add 1000 items to each list
for index in range(0, 1000):
    a.append(random.randint(10, 1000))
    b.append(random.randint(10, 1000))
    c.append(random.randint(10, 1000))
    d.append(random.randint(10, 1000))

# plant solutions are some indices
# target = 9, solution: 4, 5
a[998] = 4
a[999] = 5
b[499] = 5
b[500] = 4
c[0] = 4
c[999] = 5
d[random.randint(0, 999)] = 4
d[random.randint(0, 999)] = 5

print("\nTest Lists:")
print(a, "\n")
print(b, "\n")
print(c, "\n")
print(d, "\n")
print("Target: 9")

"""
    RESULTS: 
        Size: 1000
        
        Pattern: 
            a. [.., .., solution, solution]
            b. [.., solution, solution, ..]
            c. [solution, .., .., solution]
            d. [.., solution, .., solution, ..] 
            
        Populating lists:
            for index in range(0, 1000):
                a.append(random.randint(10, 1000))
                b.append(random.randint(10, 1000))
                c.append(random.randint(10, 1000))
                d.append(random.randint(10, 1000))
            
        Planting Solutions: 
            a[998] = 4
            a[999] = 5
            b[499] = 5
            b[500] = 4
            c[0] = 4
            c[999] = 5
            d[random.randint(0, 999)] = 4
            d[random.randint(0, 999)] = 5
            
        RUNTIME: 
            NOTE: Second Run is after refreshing the page, did not clear cache at all
            NOTE: For d., I have no clue were the results are so it is possible they 
                  were placed at the same position. In which case the test has no solution.
                  But I kept it that way to allow things stay random. If there are numbers, there was a solution.
            Solution 1 (Brute force): 
                a: 282 ms, 389 ms, 306 ms, 259 ms, 280 ms
                b: 147 ms, 192 ms, 170 ms, 157 ms, 160 ms
                c: 50 ms? (makes sense because solution at 0, 999),
                     37 ms, 66 ms, 58 ms, 60 ms
                d: 55 ms, 110 ms, 107 ms, 51 ms, 103 ms
            
            Solution 2: 
                a: 68 ms, 30 ms, 62 ms, 94 ms, 44 ms
                b: 66 ms, 67 ms, 64 ms, 43 ms, 
                    97 ms (this was after for some reason 
                    I could not run the code again and needed to sign in again)
                c: 64 ms, 73 ms, 90 ms, 65 ms, 63 ms
                d: 60 ms, 61 ms, 66 ms, 57 ms, 65 ms
                
            NOTE: For d. it turns out the solutions were at indices [236, 777]
"""