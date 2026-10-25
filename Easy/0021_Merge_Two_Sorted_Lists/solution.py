# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next

        curr.next = list1 or list2
        
        return dummy.next

# Helper function to convert a Python list to a Linked List
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to convert a Linked List back to a Python list for easy printing
def linked_list_to_list(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr

# Local terminal execution and test driver
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged_head = solution.mergeTwoLists(list1, list2)
    print(f"Test 1 Output: {linked_list_to_list(merged_head)}")  # Expected: [1, 1, 2, 3, 4, 4]

    # Test Case 2
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged_head = solution.mergeTwoLists(list1, list2)
    print(f"Test 2 Output: {linked_list_to_list(merged_head)}")  # Expected: []

    # Test Case 3
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged_head = solution.mergeTwoLists(list1, list2)
    print(f"Test 3 Output: {linked_list_to_list(merged_head)}")  # Expected: [0]
