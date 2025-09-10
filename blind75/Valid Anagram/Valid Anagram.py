class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # strings must be equal length
        if len(s) != len(t):
            return False

        ## Brute Force
        # if sorted(s) != sorted(t): #O(nlogn + mlogm)
        #     return False

        # return True

        ## Optimal Solution
        counter = dict()

        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            else:
                counter[char] = counter.get(char) - 1

        return True
        