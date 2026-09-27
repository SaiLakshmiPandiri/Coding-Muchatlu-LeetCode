# Problem: 4. Median of Two Sorted Arrays
# Difficulty: Hard
# LeetCode Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Video Explanation (Telugu): https://youtu.be/CA7cz-lYpG0
#
# Time Complexity: O((N + M) log(N + M)) - due to merging and sorting
# Space Complexity: O(N + M) - extra space for the merged array


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = sorted(nums1 + nums2)
        length = len(merged_array)
        if length % 2 == 0:
            return (
                merged_array[length // 2 - 1] + merged_array[length // 2]
            ) / 2.0
        else:
            return float(merged_array[length // 2])


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5
