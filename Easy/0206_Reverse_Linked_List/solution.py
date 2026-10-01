# Problem: 206. Reverse Linked List
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/reverse-linked-list/
# Video Explanation (Telugu): https://youtu.be/TXMG-DX8Hz4
#
# Time Complexity: O(N) - traversing each node of the linked list once
# Space Complexity: O(1) - using only a constant amount of extra pointer space


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# Example test run:
if __name__ == "__main__":
    # Helper to create linked list from list
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    # Helper to convert linked list to list
    def linked_list_to_list(head):
        res = []
        curr = head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

    sol = Solution()
    
    # Test 1: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print(linked_list_to_list(sol.reverseList(head1)))  # Output: [5, 4, 3, 2, 1]

    # Test 2: [1, 2] -> [2, 1]
    head2 = create_linked_list([1, 2])
    print(linked_list_to_list(sol.reverseList(head2)))  # Output: [2, 1]

    # Test 3: [] -> []
    head3 = create_linked_list([])
    print(linked_list_to_list(sol.reverseList(head3)))  # Output: []
