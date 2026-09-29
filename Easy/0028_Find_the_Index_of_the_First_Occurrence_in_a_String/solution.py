# Problem: 28. Find the Index of the First Occurrence in a String
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Video Explanation (Telugu): https://youtu.be/YOUR_VIDEO_ID_HERE
#
# Time Complexity: O((N - M + 1) * M) for string slicing iteration, where N = len(haystack) and M = len(needle)
# Space Complexity: O(1) auxiliary space (excluding substring slicing)


class Solution(object):

    # Method 1: Manual Substring Slicing (Sliding Window)
    def strStr_slicing(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n, m = len(haystack), len(needle)

        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i

        return -1

    # Method 2: Python Built-in str.find() Method
    def strStr_builtin(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

    # Default LeetCode submission method
    def strStr(self, haystack, needle):
        return self.strStr_slicing(haystack, needle)


# Example test run:
if __name__ == "__main__":
    sol = Solution()

    haystack1, needle1 = "sadbutsad", "sad"
    haystack2, needle2 = "leetcode", "leeto"

    print("--- Method 1: Substring Slicing ---")
    print(f"Input: haystack='{haystack1}', needle='{needle1}' -> Output: {sol.strStr_slicing(haystack1, needle1)}")  # Output: 0
    print(f"Input: haystack='{haystack2}', needle='{needle2}' -> Output: {sol.strStr_slicing(haystack2, needle2)}")  # Output: -1

    print("\n--- Method 2: Built-in str.find() ---")
    print(f"Input: haystack='{haystack1}', needle='{needle1}' -> Output: {sol.strStr_builtin(haystack1, needle1)}")  # Output: 0
    print(f"Input: haystack='{haystack2}', needle='{needle2}' -> Output: {sol.strStr_builtin(haystack2, needle2)}")  # Output: -1
