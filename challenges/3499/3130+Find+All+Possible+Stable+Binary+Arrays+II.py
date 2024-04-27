'''
3130. Find All Possible Stable Binary Arrays II

You are given 3 positive integers zero, one, and limit.

A binary array arr is called stable if:

The number of occurrences of 0 in arr is exactly zero.
The number of occurrences of 1 in arr is exactly one.
Each subarray of arr with a size greater than limit must contain both 0 and 1.
Return the total number of stable binary arrays.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: zero = 1, one = 1, limit = 2

Output: 2

Explanation:

The two possible stable binary arrays are [1,0] and [0,1].

Example 2:

Input: zero = 1, one = 2, limit = 1

Output: 1

Explanation:

The only possible stable binary array is [1,0,1].

Example 3:

Input: zero = 3, one = 3, limit = 2

Output: 14

Explanation:

All the possible stable binary arrays are [0,0,1,0,1,1], [0,0,1,1,0,1], [0,1,0,0,1,1], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,1,0,0,1], [0,1,1,0,1,0], [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,1,0,0,1], [1,0,1,0,1,0], [1,0,1,1,0,0], [1,1,0,0,1,0], and [1,1,0,1,0,0].

Constraints:

1 <= zero, one, limit <= 1000
'''

from collections import defaultdict

class Solution:
  '''
  the dp[x, y, 0/1] represents the valid array counts with x_zeros, y_ones, and ending with 0 or 1;
  the dp state transition is the following:
    1) dp[x, y, 0] = sum(dp[x-k, y, 1] for k in range(1, limit+1))
    2) dp[x, y, 1] = sum(dp[x, y-k ,0] for k in range(1, limit+1))
  to speed up the sum(...) part, we can save the sum(dp[x-k, y, 1] for i in range(limit)) as prefix[1, y],
  then for each newly calculated dp[x, y, 0], we can update prefix accordingly:
    1) prefix[1, y] += dp[x, y, 1];
    2) if x-limit >= 0, we need to pop the dp value no longer in the `limit` consideration, with: 
       prefix[1, y] -= dp[x-limit, y, 1]; 
    3) repeat step 1 and 2 for prefix[0, x] as well
  '''
  def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
    if limit == 1:
      if abs(zero-one) > 1:
        return 0
      
      return 2 if zero == one else 1
      
    mod = 10**9 + 7
    dp = defaultdict(int)
    prefix = defaultdict(int)
    
    for x in range(zero+1):
      for y in range(one+1):
        # current combo: (x_zeros, y_ones)
        if x == 0:
          if y > limit:
            break
            
          if y > 0:
            dp[x, y, 1] = 1
            prefix[1, y] += 1
            
          continue
        
        if y == 0:
          if x <= limit:
            dp[x, y, 0] = 1
            prefix[0, x] += 1
            
          continue
          
        dp[x, y, 0] = prefix[1, y] # aka: sum(dp[x-k, y, 1] for k in range(1, limit+1))
        dp[x, y, 1] = prefix[0, x] # aka: sum(dp[x, y-k, 0] for k in range(1, limit+1))
        
        # update prefix sums for 0 @ x
        prefix[0, x] = (prefix[0, x] + dp[x, y, 0]) % mod
        if y-limit >= 0:
          prefix[0, x] = (prefix[0, x] - dp[x, y-limit, 0] + mod) % mod
        
        # update prefix sums for 1 @ y
        prefix[1, y] = (prefix[1, y] + dp[x, y, 1]) % mod
        if x-limit >= 0:
          prefix[1, y] = (prefix[1, y] - dp[x-limit, y, 1] + mod) % mod
        
        # print('*** calc:', (x, y))
        # print('0:', dp[x, y, 0], p0)
        # print('1:', dp[x, y, 1], p1)
    
    return (dp[zero, one, 0] + dp[zero, one, 1]) % mod
    