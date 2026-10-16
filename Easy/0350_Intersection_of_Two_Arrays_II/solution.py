from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Count frequencies of each number in both arrays
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        # The & operator on Counters takes the minimum frequency of common elements
        result_counter = c1 & c2

        # Convert the counter back to a list containing repeated elements as per minimum frequency
        return list(result_counter.elements())


if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    print(f"Input: nums1={nums1}, nums2={nums2} | Output: {sol.intersect(nums1, nums2)}")  # Expected: [2, 2]
    
    # Test Case 2
    nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
    print(f"Input: nums1={nums1}, nums2={nums2} | Output: {sol.intersect(nums1, nums2)}")  # Expected: [4, 9] or [9, 4]
