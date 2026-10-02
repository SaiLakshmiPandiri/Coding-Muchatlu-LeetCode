class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        
        # Method 1: Greedy Approach with Value-Symbol Pairs
        val_symbols = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        for val, symbol in val_symbols:
            if num == 0:
                break
            count = num // val
            if count > 0:
                result.append(symbol * count)
                num %= val
                
        return "".join(result)

        
        # Method 2: Optimal O(1) Pre-computed Digit Indexing approach
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
