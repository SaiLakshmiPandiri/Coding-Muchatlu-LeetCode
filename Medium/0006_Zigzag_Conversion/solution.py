# Problem: 6. Zigzag Conversion
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/zigzag-conversion/
# Video Explanation (Telugu): https://youtu.be/si-pn9oV8Jc
#
# Time Complexity: O(N) - single pass over string s
# Space Complexity: O(N) - space needed to store the formatted result


class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        res = []
        cycle_len = 2 * numRows - 2

        for r in range(numRows):
            for i in range(r, len(s), cycle_len):
                res.append(s[i])
                # Add middle diagonal elements for interior rows
                diag_idx = i + cycle_len - 2 * r
                if 0 < r < numRows - 1 and diag_idx < len(s):
                    res.append(s[diag_idx])

        return "".join(res)


# Example test run:
if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))  # Output: "PAHNAPLSIIGYIR"
