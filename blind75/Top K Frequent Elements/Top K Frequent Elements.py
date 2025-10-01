class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ##### NAIVE SOLUTION - O(n log n) time complexity
        # # the list has only one element
        # if len(nums) == 1 and k == 1:
        #     return nums

        # # create a counter for the elements in the list
        # counter_dict = {}

        # for item in nums: # O(n) operation
        #     counter_dict[item] = counter_dict.get(item, 0) + 1

        # # sort by values - Iteration to create a list of item is O(N) and then sorting the item O(N log N)
        # sorted_dict = dict(sorted(counter_dict.items(), key=lambda x: x[1]))

        # # build a list with the top keys
        # return list(sorted_dict.keys())[k-1:]

        ##### BETTER SOLUTION
        count = {} # store the frequency of each number (O(n) time complexity)
        freq = [[] for i in range(len(nums) + 1)] # array same size as `nums`, where the index represents the frequency of elements in `nums` and the value would be the list of values with that frequency
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # because the max frequency of any number in nums can be len(nums)
        # the time complexity of this loop is O(n)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1): 
            # iterate from the back of the freq array
            # we stop before 0 because 0 frequency means the number is not in the list
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        