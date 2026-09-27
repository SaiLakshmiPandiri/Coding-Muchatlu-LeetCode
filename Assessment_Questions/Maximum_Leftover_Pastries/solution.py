"""
Problem Name: Maximum Leftover Pastries
Category: Campus Assessment / Placement Coding Question
Languages: Python 3 & C

Problem Statement:
Jack works in a bakery and wants to maximize the number of leftover pastries 
he gets to take home. Given 'n' pastries, he can choose a packet size from 1 to 'n'.
The leftover pastries for a packet size is given by (n % packet_size).
If multiple packet sizes produce the same maximum leftover, Jack chooses the 
largest packet size.

Complexity:
- Time Complexity: O(N)
- Space Complexity: O(1)
"""

def solve_maximum_leftover_pastries(n: int) -> int:
    max_leftover = -1
    answer = 1
    
    for packet_size in range(1, n + 1):
        leftover = n % packet_size
        # Using >= ensures we update 'answer' to the larger packet size on a tie
        if leftover >= max_leftover:
            max_leftover = leftover
            answer = packet_size
            
    return answer


if __name__ == "__main__":
    try:
        n = int(input().strip())
        print(solve_maximum_leftover_pastries(n))
    except (EOFError, ValueError):
        # Fallback test run
        sample_n = 10
        print(f"Sample Input: {sample_n}")
        print(f"Sample Output: {solve_maximum_leftover_pastries(sample_n)}")
