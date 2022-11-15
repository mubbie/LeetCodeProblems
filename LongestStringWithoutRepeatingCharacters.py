# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Leetcode MEDIUM

# thinking:
# input -> string
# output -> length of the longest substring without repeating characters

# example:
# input: "abcabcbb"
# output: 3, "abc", "abc" is the longest substring without repeating characters

# input: "bbbbb"
# output: 1, "b"

# input: "pwwkew"
# output: 3, "wke"

# approach
# have a dictionary mapping characters to their corresponding index
#       have a left pointer that forms a sliding window with the index
#           used to iterate through the list
#       have an output to store the result of the function
# iterate through the string
#   if a character has not been seen
#       update the output = max(output, i - l + 1)
#   else
#       if the character is in the current window
#           move l to 1 greater than the index of the matching index from the map
#       else
#           compute the output = max(output, i - l + 1)
# return the output

class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        # define the dictionary mapping `character` -> `index`
        seen = dict()

        # define left/right pointers for sliding window, and the output
        left = 0
        output = 0

        # iterate through the string
        
        # for i in range(0, len(s)):
        #     # character has not been seen
        #     if s[i] not in seen:
        #         output = max(output, i-left+1)
        #     # character has been seen
        #     else:
        #         if seen[s[i]] < left:
        #             # not in current window
        #             output = max(output, i - left + 1)
        #         else:
        #             # in current window
        #             left = seen[s[i]] + 1
        #     seen[s[i]] = i
            
        # alternative looping implementation
        # using enumerate
        for i, j in enumerate(s):
            # character has not been seen 
            if j not in seen:
                output = max(output, i - left + 1)
            # character has been seen
            else: 
                if seen[j] < left:
                    # not in current window
                    output = max(output, i - left + 1)
                else:
                    # in current window
                    left = seen[j] + 1
            seen[j] = i

        return output

print(Solution.lengthOfLongestSubstring("abcabcbb"))