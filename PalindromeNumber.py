# Problem: https://leetcode.com/problems/palindrome-number/
# Leetcode EASY

# Given an integer x,
# return true if x is a palindrome,
# and false otherwise.

# THINKING:
# BRUTE FORCE SOLUTION:
# convert the number to a string
# have two pointers, one from each end of the string
# at each step the characters should be equal
# if not, return false
# loop should stop when pointers are at the same location or next to each other

# CHALLENGE:
# solve the problem without converting the integer to a string
# reverse the integer
# if it is equal to the original, then it is a palindrome

class Solution:
    @staticmethod
    def isPalindrome(x: int) -> bool:
        x_str = str(x)

        # edge cases
        if len(x_str) == 1:
            return True
        elif len(x_str) == 2:
            if x_str[0] == x_str[-1]:
                return True
            # otherwise
            return False

        if x < 0:
            # negative numbers cannot be Palindromes
            return False

        # create pointers
        start = 0
        end = len(x_str) - 1
        while start != end and start != end-1:
            if x_str[start] != x_str[end]:
                return False
            start += 1
            end -= 1
        # after all tests
        if start == end-1:
            return x_str[start] == x_str[end]
        return True

    @staticmethod
    def isPalindrome2(x: int) -> bool:
        # edge case
        if x < 0:
            # negative numbers cannot be palindromes
            return False

        # reverse the integer
        # if it is equal to the original, then it is a palindrome
        reverse = 0
        n = x
        while n > 0:
            rem = n % 10
            reverse = reverse*10 + rem
            n = n // 10
        return reverse == x


# testing brute force
# 121, -121, 10, 11
x1 = 121
x2 = -121
x3 = 10
x4 = 11
x5 = 1000030001
x6 = 1001

print(Solution.isPalindrome2(x1))
print(Solution.isPalindrome2(x2))
print(Solution.isPalindrome2(x3))
print(Solution.isPalindrome2(x4))
print(Solution.isPalindrome2(x6))

