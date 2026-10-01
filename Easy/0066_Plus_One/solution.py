# Problem: 66. Plus One
# Difficulty: Easy
# LeetCode Link: https://leetcode.com/problems/plus-one/
# Video Explanation (Telugu): https://youtu.be/653wtBKrdfc
#
# Time Complexity: O(N) - processing digits to form integer sum and converting back
# Space Complexity: O(N) - storing the result array of digits


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = []
        total_sum = 0
        for i in digits:
            total_sum = (total_sum * 10) + i
        total_sum += 1
        for i in str(total_sum):
            res.append(int(i))
        return res


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
    print(sol.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
    print(sol.plusOne([9]))  # Output: [1, 0]
