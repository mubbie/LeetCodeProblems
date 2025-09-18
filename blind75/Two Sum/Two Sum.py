class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ### naive solution (brute force) - Time complexity is O(n^2)
        # indices = list(range(len(nums)))
        # for index1 in indices:
        #     for index2 in indices:
        #         if index1 == index2:
        #             continue
        #         elif nums[index1] + nums[index2] == target:
        #             output = [index1, index2]
        #             print(output)
        #             return sorted(output)
        # return []
        
        ### better solution
        tracking = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in tracking:
                return [tracking[complement], i]
            else:
                tracking[nums[i]] = i
        return []