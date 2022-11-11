# Problem: https://leetcode.com/problems/add-two-numbers/
# Leetcode MEDIUM

# given two non-empty linked lists representing two non-negative integers
# the digits are stored in reverse order
# each node contains are single digit
# add the two numbers and return the sum of as a linked list

######## THINKING:
"""
    When adding numbers, we compute like so:
    Adding 99999 and 999
            last
            digit
            |
    first   |
    digit   |
        |   |
        99999 -> size 5
          999 -> size 3
        1111
        -----
       100998
    We expect the length of the sum to be at least the length
    of the larger number. In this case, 5
    We start adding from the last digit, and keep carrying
    until the first digit

    If we adopt this example to a linked lists,
    say to add 342 and 78

    we will have lists like so:
    a = [2,4,3] and b = [8,7]

    the longest list is [2,4,3], size 3
    so the sum is at least 3 digits long
    thus, the output is at least of size 3

    see the code below for the rest of the computation
"""

# ListNodeDefinition
# from LeetCode:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        """
        Class to hold one list node
        :param val: value of the list node
        :param next: ListNode that the current node points to
        """
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def addNumbers(num1: int, num2: int) -> tuple:
        """
        Compute the sum of two numbers that do not add to more than a 2-digit result
        :param num1: the first number
        :param num2: the second number
        :return: a tuple consisting of:
            the first digit of the result,
            the second digit of the result,
            the sum of num1 and num2
        """
        sumDigs = num1 + num2
        if sumDigs <= 9:
            return 0, sumDigs
        else:
            return sumDigs//10, sumDigs%10

    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        """
        Given two non-empty linked lists representing two negative numbers
        The digits are stored in reverse order and each node contains a single digit
        Adds the two numbers and returns the sum as a linked list
        :param l1: the first linked list
        :param l2: the second linked list
        :return: the sum of the two linked lists

        TIME COMPLEXITY:
        Let n be the size of the larger list
        Let m be the size of the smaller list
        If both lists are the same size use m
            - first loop: O(m)
            - second loop (only one of the two defined loops runs): O(n-m)
                - does not run if the lists are the same size
            - last loop: O(n)
                - with the possibility of O(n+1) if there is any carry
        """
        # modifiable pointers for the ListNodes
        temp1, temp2 = l1, l2

        # first part of the sum
        # that is, starting from the back of the two numbers
        # the sum of each corresponding digit
        # for instance, if the numbers are 53789 and 426
        # this will compute the sum of 9 and 6, 8 and 2,
        size, carryOver = 0, 0
        output = list()
        while temp1.next is not None and temp2.next is not None:
            carryOver, sumDig2 = Solution.addNumbers(temp1.val, temp2.val + carryOver)
            output.append(sumDig2)
            temp1 = temp1.next
            temp2 = temp2.next
            size += 1

        # add the last digits from both lists
        # this will add the current digits in stored in temp1 and temp2
        # for the example above, this will be 7 and 4
        carryOver, endDig = Solution.addNumbers(temp1.val, temp2.val + carryOver)
        output.append(endDig)
        if carryOver > 0 and temp1.next is None and temp2.next is None:
            output.append(carryOver)

        # compute the final part of the sum i.e. if there are any extra digits
        # if any of the inputs has extra digits this will add them to the sum
        # for the example above, this will be 5, 3 and any carried over remainders
        while temp1.next is not None:
            carryOver, sumDig2 = Solution.addNumbers(temp1.next.val, carryOver)
            output.append(sumDig2)
            temp1 = temp1.next
        while temp2.next is not None:
            carryOver, sumDig2 = Solution.addNumbers(temp2.next.val, carryOver)
            output.append(sumDig2)
            temp2 = temp2.next

        # add the final carryOver (if any)
        # this will be any additional digit that should increase the width
        # of the output sum beyond the length of the longest input
        if carryOver > 0:
            output.append(carryOver)

        # build the output
        # from the list where the output has been accumulated
        # construct a new linked list
        sumOutput = ListNode(output[0])
        temp3 = sumOutput
        for i in range(1, len(output)):
            temp3.next = ListNode(output[i])
            temp3 = temp3.next
        return sumOutput


# tests
# build lists
ll1 = ListNode(2, ListNode(4, ListNode(3)))
ll2 = ListNode(8, ListNode(7))

ll3 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))
ll4 = ListNode(9, ListNode(9, ListNode(9)))

ll5 = ListNode(0)
ll6 = ListNode(0)

# build output
out = Solution.addTwoNumbers(ll4, ll3)

# print out values
while out.next is not None:
    print(out.val)
    out = out.next
print(out.val)
