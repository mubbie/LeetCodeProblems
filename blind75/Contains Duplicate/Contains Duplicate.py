class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = dict()

        for item in nums:
            if duplicates.get(item) != None:
                return True
            else:
                duplicates[item] = 1
        return False