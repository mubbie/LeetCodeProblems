# Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Leetcode HARD

# runtime should be O(log (m+n))

# thoughts
# merge sort from CS1?

# resource: http://projectpython.net/chapter13/

# I am not certain how to do it in O(log (m+n)) time as of now
# I believe that will involve some sort of "divide and conquer"
# but I am able to implement it using the merge part of the merge sort algorithm
# since both lists are sorted, I can merge then and the easily find the median
# that solution will involve using extra memory by creating another list though

class Solution:
    @staticmethod
    def computeMedian(nums: list[int]) -> float:
        size = len(nums)
        if size % 2 == 0:
            return (nums[size // 2 - 1] + nums[size // 2]) / 2
        else:
            return nums[size // 2]

    @staticmethod
    def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        """

        :param nums1:
        :param nums2:
        :return:

        TIME COMPLEXITY: O(m+n)
            - iterating through both lists
        """
        # EDGE CASE
        # if any of the lists are empty
        if not nums1:
            return Solution.computeMedian(nums2)
        elif not nums2:
            return Solution.computeMedian(nums1)

        # merge the lists
        merge = list()
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merge.append(nums1[i])
                i += 1
            else:
                merge.append(nums2[j])
                j += 1

        # add any remainders
        if i < len(nums1):
            merge.extend(nums1[i:])
        if j < len(nums2):
            merge.extend(nums2[j:])

        # compute the median
        return Solution.computeMedian(merge)

    @staticmethod
    def findMedianSortedArrays2(nums1: list[int], nums2: list[int]) -> float:
        """
        :param nums1:
        :param nums2:
        :return:

        THINKING:
            Using the concept of binary search or "divide and conquer"
            List: nums1, size n; nums2, size m
            The median will be the middle of the sorted list (odd sized)
            or the average of the two items in the middle of the sorted list (even sized)
            As such, if we can build out the left half of the sorted list
            we can compute the median of the lists
            The size of the left half will (m + n)/2
            So how can we figure out what that left half will be in log(m+n) time

            If we isolate one of the lists and compute the min and max that
            it can contribute to the left half of the merged list

            EXAMPLE 1:
                nums1 = [4, 20, 32, 59, 55, 61]
                nums2 = [1, 15, 22, 30, 70]

                sum of lengths = 11

            EXAMPLE 2:
                nums1 = [1, 15, 22]
                nums2 = [4, 30, 32, 59, 55]

                sum of lengths = 8
            - handle edge case where either list is empty
                - call a function that computes the median
            - compute the length of the left half of the list
                - that is: len//2 + 1
                    ex. 1: 11 -> 6
                    ex. 2: 8 -> 5
            - use one list and compute how much from that list could
            - could be in the left half of the sorted list
                - takings nums1
                    ex. 1: min: 0, max = 6
                    ex. 2: min: 0, max = 3
                - how to compute
                    using nums1
                    compute left half len
                    min = 0
                    if len(nums1) => left_half_len:
                        max = left_half_len
                    else:
                        max = left_half_len - len(nums1) + 1
            - while min < max:
                - estimate how much could be contributed from the range
                - i.e. the expected value
                countNums1 = (min + max)/2
                - thus, the number contributed from the other list
                countNums = left_half_len - countNums1

                - compute the last




        """


print(Solution.findMedianSortedArrays([1, 2], [3,4]))

# TODO: attempt to solve it O(log(m+n)) time


