class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Approach: Track unmatched opening brackets and required closing brackets.
        open_count = 0
        need_close = 0

        for char in s:
            if char == '(':
                open_count += 1
            elif open_count > 0:
                # Match current ')' with an available unmatched '('
                open_count -= 1
            else:
                # Encountered ')' without a preceding '(', so we need an opening bracket
                need_close += 1

        # Total additions needed = unmatched open brackets + unmatched closing brackets
        return open_count + need_close

# Complexity Analysis & Example Test Runs:
# ----------------------------------------------------
# Time Complexity: O(N) - Where N is the length of the string s. We iterate through each character once.
# Space Complexity: O(1) - Only a constant amount of extra space is used for tracking counters.
#
# Example Test Run:
# Input: s = "())"
# - '(' -> open_count = 1, need_close = 0
# - ')' -> open_count > 0 -> open_count = 0, need_close = 0
# - ')' -> open_count == 0 -> need_close = 1
# Return: open_count + need_close = 0 + 1 = 1
