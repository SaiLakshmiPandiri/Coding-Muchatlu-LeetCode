class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Optimal O(1) Pre-computed Digit Indexing approach
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        return (
            thousands[num // 1000] + 
            hundreds[(num % 1000) // 100] + 
            tens[(num % 100) // 10] + 
            ones[num % 10]
        )
