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
    def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
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
        size = len(merge)
        if size % 2 == 0:
            return (merge[size//2 - 1] + merge[size//2])/2
        else:
            return merge[size//2]

print(Solution.findMedianSortedArrays([1, 2], [3,4]))

# TODO: attempt to solve it O(log(m+n)) time

