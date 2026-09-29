# Problem: 50. Pow(x, n)
# Difficulty: Medium
# LeetCode Link: https://leetcode.com/problems/powx-n/
# Video Explanation (Telugu): https://youtu.be/YOUR_VIDEO_ID_HERE
#
# Time Complexity: O(log N) - for both Binary Exponentiation and Python's built-in power operation
# Space Complexity: O(1) - iterative solution using constant auxiliary space


class Solution(object):

    # Method 1: Python Built-in Exponentiation Operator
    def myPow_builtin(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n

    # Method 2: Binary Exponentiation (Fast Powering / Divide & Conquer)
    def myPow_binary_exponentiation(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Handle negative exponents
        N = n
        if N < 0:
            x = 1 / x
            N = -N

        ans = 1.0
        current_product = x

        # Iterative Binary Exponentiation
        while N > 0:
            if N % 2 == 1:
                ans *= current_product
            current_product *= current_product
            N //= 2

        return ans

    # Default LeetCode submission method
    def myPow(self, x, n):
        return self.myPow_builtin(x, n)


# Example test run:
if __name__ == "__main__":
    sol = Solution()

    print("--- Method 1: Built-in Operator (x ** n) ---")
    print(f"2.0 ^ 10  = {sol.myPow_builtin(2.00000, 10):.5f}")   # Output: 1024.00000
    print(f"2.1 ^ 3   = {sol.myPow_builtin(2.10000, 3):.5f}")    # Output: 9.26100
    print(f"2.0 ^ -2  = {sol.myPow_builtin(2.00000, -2):.5f}")   # Output: 0.25000

    print("\n--- Method 2: Binary Exponentiation ---")
    print(f"2.0 ^ 10  = {sol.myPow_binary_exponentiation(2.00000, 10):.5f}")   # Output: 1024.00000
    print(f"2.1 ^ 3   = {sol.myPow_binary_exponentiation(2.10000, 3):.5f}")    # Output: 9.26100
    print(f"2.0 ^ -2  = {sol.myPow_binary_exponentiation(2.00000, -2):.5f}")   # Output: 0.25000
