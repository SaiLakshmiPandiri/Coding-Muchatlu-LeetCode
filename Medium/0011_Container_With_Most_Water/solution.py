# Problem: 11. Container With Most Water
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/container-with-most-water/
# Video Explanation (Telugu): https://youtu.be/ngsfhojVJ00
#
# Time Complexity: O(N) - two pointers moving inward
# Space Complexity: O(1) - constant memory usage


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ptr1 = 0
        ptr2 = len(height) - 1
        max_water = 0
        while ptr1 < ptr2:
            water = min(height[ptr1], height[ptr2]) * (ptr2 - ptr1)
            if max_water < water:
                max_water = water
            if height[ptr1] < height[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
        return max_water


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Output: 49
