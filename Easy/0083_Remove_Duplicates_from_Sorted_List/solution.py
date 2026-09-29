# Problem: 83. Remove Duplicates from Sorted List
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Video Explanation (Telugu): https://youtu.be/YOUR_VIDEO_ID_HERE
#
# Time Complexity: O(N) - single pass through the linked list
# Space Complexity: O(1) - in-place node pointer manipulation


# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


# Helper function to convert a list to a linked list for testing
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


# Helper function to print linked list values
def print_linked_list(head):
    result = []
    curr = head
    while curr:
        result.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(result) if result else "Empty List")


# Example test run:
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: [1, 1, 2]
    head1 = create_linked_list([1, 1, 2])
    print("Original List 1: ", end="")
    print_linked_list(head1)
    res1 = sol.deleteDuplicates(head1)
    print("After Removing Duplicates: ", end="")
    print_linked_list(res1)

    print("\n" + "-" * 30 + "\n")

    # Test Case 2: [1, 1, 2, 3, 3]
    head2 = create_linked_list([1, 1, 2, 3, 3])
    print("Original List 2: ", end="")
    print_linked_list(head2)
    res2 = sol.deleteDuplicates(head2)
    print("After Removing Duplicates: ", end="")
    print_linked_list(res2)
