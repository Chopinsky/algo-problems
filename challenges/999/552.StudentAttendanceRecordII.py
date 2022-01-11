'''
An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
Example 2:

Input: n = 1
Output: 3
Example 3:

Input: n = 10101
Output: 183236316

Constraints:

1 <= n <= 105
'''


class Solution:
  def checkRecord0(self, n: int) -> int:
    mod = 10 ** 9 + 7
    if n == 0:
      return 0
    
    if n == 1:
      return 3
    
    dp = [0] * (n + 1)

    # without having 'A' in the str
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4

    for i in range(3, n+1):
      # any (n - 1) valid string, add 'p'
      # any (n - 2) valid string, add 'pl'
      # any (n - 3) valid string, add 'pll'
      dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % mod

    # adding 'A', concate 2 valid strings with length
    # `i` and `n-i-1` ==> total length is still `n`.
    ans = dp[n]
    for i in range(n):
      # [<valid_str_len_i>] + ['A'] + [<valid_str_len_(n-i-1)>]
      ans += (dp[i] * dp[n-i-1]) % mod

    return ans % mod
    
    
  def checkRecord(self, n: int) -> int:
    mod = 1_000_000_007
    
    # no a: (0) xxxP, (1) xxxL, (2) xxLL; with a: (3) xxxA, (4) xAxP, (5) xAxL, (6) xALL
    stack, nxt = [1, 1, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]
    
    for _ in range(1, n):
      # still no absent:
      nxt[0] = sum(stack[:3]) % mod
      nxt[1] = stack[0]
      nxt[2] = stack[1]
      
      # with an absent 
      nxt[3] = sum(stack[:3]) % mod
      nxt[4] = sum(stack[3:]) % mod
      nxt[5] = (stack[3] + stack[4]) % mod
      nxt[6] = stack[5]
      
      stack, nxt = nxt, stack
      # print(stack, last_absent_total)
      
    return sum(stack) % mod
  