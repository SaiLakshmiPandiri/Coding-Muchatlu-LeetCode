class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # Step 2: Determine the sign
        sign = 1
        start = 0
        if s[0] == '-':
            sign = -1
            start = 1
        elif s[0] == '+':
            start = 1
            
        # Step 3: Convert digits to integer manually
        result = 0
        for i in range(start, len(s)):
            if not s[i].isdigit():
                break
            result = result * 10 + int(s[i])
            
        # Apply sign
        result *= sign
        
        # Step 4: Handle 32-bit signed integer overflow limits [-2^31, 2^31 - 1]
        INT_MAX = 2147483647      # 2^31 - 1
        INT_MIN = -2147483648     # -2^31
        
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
            
        return result
