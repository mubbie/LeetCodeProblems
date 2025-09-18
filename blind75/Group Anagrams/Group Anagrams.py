class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for item in strs:
            char_freq = [0] * 26 # list of 26 zeros
            for char in item:
                char_freq[ord(char) - ord('a')] += 1
            output[tuple(char_freq)].append(item)

        return list(output.values())


####### NAIVE SOLUTION #######
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         # naive
#         # handling default inputs
#             # size 1 list
#                 # return a list of list
#         # have a set to keep track of processed string (this will have O(1) lookup)
#         # use index to keep track of sublist
#         # start at index 0 and increment
#         # for index 0
#         # iterate over the list
#             # if item has not been processed
#                 # for each item in the list
#                     # check if we have valid anagram
#                         # if so, add it at index 0
#             # before the next iteration, increment index
#         # eventually, return the lists of lists

#         # default
#         if len(strs) == 1:
#             return [[strs[0]]]

#         # other cases
#         tracker = set() 
#         output = list() 
#         process_idx = 0 

#         # Time Complexity: O(N^2) - where N is len(strs)
#         # Total time complexity O(N^2 * (len(a) * len(b)))
#         for i in range(len(strs)):
#             if i not in tracker:
#                 item = strs[i]
#                 output.insert(process_idx, list())
#                 output[process_idx].append(item)
#                 tracker.add(i)

#                 for j in range(len(strs)):
#                     item2 = strs[j]
#                     if j not in tracker:
#                         # check valid anagram
#                         isAnagram = Solution.checkValidAnagram(item, item2)
#                         if isAnagram:
#                             output[process_idx].append(item2)
#                             tracker.add(j)
#                 process_idx += 1

#         return output

#     # Time Complexity: O(len(a) * len(b))
#     def checkValidAnagram(a: str, b: str) -> bool:
#         if len(a) != len(b):
#             return False

#         counter = dict()
#         for char in a:
#             if char in counter:
#                 counter[char] += 1
#             else:
#                 counter[char] = 1

#         for char2 in b:
#             if char2 not in counter:
#                 return False
#             if counter[char2] == 0:
#                 return False
#             counter[char2] -= 1

#         return True
            