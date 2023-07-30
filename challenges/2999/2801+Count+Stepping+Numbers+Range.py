'''
2801. Count Stepping Numbers in Range

Given two positive integers low and high represented as strings, find the count of stepping numbers in the inclusive range [low, high].

A stepping number is an integer such that all of its adjacent digits have an absolute difference of exactly 1.

Return an integer denoting the count of stepping numbers in the inclusive range [low, high].

Since the answer may be very large, return it modulo 109 + 7.

Note: A stepping number should not have a leading zero.

Example 1:

Input: low = "1", high = "11"
Output: 10
Explanation: The stepping numbers in the range [1,11] are 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10. There are a total of 10 stepping numbers in the range. Hence, the output is 10.
Example 2:

Input: low = "90", high = "101"
Output: 2
Explanation: The stepping numbers in the range [90,101] are 98 and 101. There are a total of 2 stepping numbers in the range. Hence, the output is 2. 

Constraints:

1 <= int(low) <= int(high) < 10^100
1 <= low.length, high.length <= 100
low and high consist of only digits.
low and high don't have any leading zeros.
'''

from functools import lru_cache


class Solution:
  def countSteppingNumbers(self, low: str, high: str) -> int:
    n = len(high)
    if n == 1:
      return int(high) - int(low) + 1
    
    # add prefix so we can compare easily
    if len(low) < n:
      low = '0' * (n-len(low)) + low

    mod = 10**9 + 7
    idx = 0
    
    # excluding same prefix between low and high, 
    # as these won't affect the final count
    while idx < n:
      if low[idx] != high[idx]:
        break
        
      # same prefix, won't match the criteria, quit with 0
      if idx > 0 and abs(int(low[idx]) - int(low[idx-1])) != 1:
        return 0
      
      idx += 1
      
    # low == high, done
    if idx == n:
      return 1
    
    debug = False
    if debug:
      print('init:', low, high, idx)
    
    # count number of matching numbers based on the status:
    #  * [-2] -> we're sitting on the lower bound, and the prefix only contains 0,
    #            this means we shall count from low_digit_at_idx -> 10
    #  * [-1] -> we're sitting on the lower bound, must check if the next digit be above
    #            low_digit_at_idx
    #  * [0]  -> we're in the middle, free zone, can go low or high either way
    #  * [1]  -> we're sitting on the higher bound, must check if the next digit be below
    #            high_digit_at_idx
    @lru_cache(None)
    def dp(i: int, prev: int, status: int) -> int:
      if i >= n:
        return 1
      
      cnt = 0
      l, h = int(low[i]), int(high[i])
      
      # prefix are pure 0s, do the full range
      if status == -2:
        if i == n-1:
          return 10 - l
        
        status = -1
        if l == 0:
          status = -2
        
        cnt = (cnt + dp(i+1, l, status))
        for v0 in range(l+1, 10):
          cnt = (cnt + dp(i+1, v0, 0)) % mod
          
        if debug:
          print('zero', (i, prev), status, cnt)
          
        return cnt
          
      l0, h0 = prev-1, prev+1
      
      # sitting on lower bound previously, must check if we're above the low
      if status == -1:
        if h0 >= l and h0 < 10:
          cnt = (cnt + dp(i+1, h0, -1 if h0 == l else 0)) % mod
          
        if l0 >= l:
          cnt = (cnt + dp(i+1, l0, -1 if l0 == l else 0)) % mod
        
        if debug:
          print('low', (i, prev), (l0, h0), cnt)
          
        return cnt
      
      # sitting on the higher bound previously, must check if we're below the high
      if status == 1:
        if l0 <= h and l0 >= 0:
          cnt = (cnt + dp(i+1, l0, 1 if l0 == h else 0)) % mod
          
        if h0 <= h:
          cnt = (cnt + dp(i+1, h0, 1 if h0 == h else 0)) % mod
          
        if debug:
          print('high', (i, prev), (l0, h0), cnt)
          
        return cnt
      
      # mostly free, just check if l0 and h0 are valid digits
      if h0 < 10:
        cnt = (cnt + dp(i+1, h0, 0)) % mod
        
      if l0 >= 0:
        cnt = (cnt + dp(i+1, l0, 0)) % mod
      
      if debug:
        print('mid', (i, prev), (l0, h0), cnt)
        
      return cnt
    
    cnt = 0
    l, h = int(low[idx]), int(high[idx])
    
    # if low and high differs at 0, we need to count low bounds and high bounds, and then
    # count all the middle digits manually, as these can't be put under the `dp` algo
    if idx == 0:
      cnt = (cnt + dp(idx+1, l, -2 if l == 0 else -1)) % mod
      cnt = (cnt + dp(idx+1, h, 1)) % mod

      for v0 in range(l+1, h):
        cnt = (cnt + dp(idx+1, v0, 0)) % mod
        
      return cnt

    # low and high differs at a later digit, we can check both `go low` and `go high` senarios
    # seperately, but need to set the status correctly for either case
    prev = int(low[idx-1])
    l0, h0 = prev-1, prev+1

    if l0 >= l and l0 <= h:
      status = 0
      if l0 == h:
        status = 1
      elif l0 == l:
        status = -1
        
      if debug:
        print('start low', status)
        
      cnt = (cnt + dp(idx+1, l0, status)) % mod

    if h0 >= l and h0 <= h:
      status = 0
      if h0 == h:
        status = 1
      elif h0 == l:
        status = -1
        
      if debug:
        print('start high', status)
        
      cnt = (cnt + dp(idx+1, h0, status)) % mod
    
    return cnt
        