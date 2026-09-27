/*
Problem Name: Maximum Leftover Pastries
Category: Campus Assessment / Placement Coding Question
Language: C (GCC)

Complexity:
- Time Complexity: O(N)
- Space Complexity: O(1)
*/

#include <stdio.h>

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;

    int max_leftover = -1;
    int answer = 1;

    for (int packet_size = 1; packet_size <= n; packet_size++) {
        int leftover = n % packet_size;
        if (leftover >= max_leftover) {
            max_leftover = leftover;
            answer = packet_size;
        }
    }

    printf("%d\n", answer);
    return 0;
}
