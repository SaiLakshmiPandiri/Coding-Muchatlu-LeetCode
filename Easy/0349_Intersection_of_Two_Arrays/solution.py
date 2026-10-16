class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Convert both lists into sets and perform set intersection
        # to find unique common elements.
        return list(set(nums1).intersection(set(nums2)))


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    print(f"Input: nums1={nums1}, nums2={nums2} | Output: {sol.intersection(nums1, nums2)}")  # Expected: [2]
    
    # Test Case 2
    nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
    print(f"Input: nums1={nums1}, nums2={nums2} | Output: {sol.intersection(nums1, nums2)}")  # Expected: [9, 4] or [4, 9]
