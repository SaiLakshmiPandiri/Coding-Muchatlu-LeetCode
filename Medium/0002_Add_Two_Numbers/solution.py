# Problem: 2. Add Two Numbers
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/add-two-numbers/
# Video Explanation (Telugu): https://youtu.be/HDcJWZo6iMY
#
# Time Complexity: O(max(N, M)) - iterate through the longer of the two lists
# Space Complexity: O(max(N, M)) - length of the new created linked list


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            total = a + b + carry

            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# Helper functions for local execution
def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def print_linked_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    # 342 represented as [2, 4, 3] + 465 represented as [5, 6, 4]
    l1 = build_linked_list([2, 4, 3])
    l2 = build_linked_list([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)
    print_linked_list(result)  # Output: 7 -> 0 -> 8 (807)
