'''
2507. Smallest Value After Replacing With Sum of Prime Factors

You are given a positive integer n.

Continuously replace n with the sum of its prime factors.

Note that if a prime factor divides n multiple times, it should be included in the sum as many times as it divides n.
Return the smallest value n will take on.

Example 1:

Input: n = 15
Output: 5
Explanation: Initially, n = 15.
15 = 3 * 5, so replace n with 3 + 5 = 8.
8 = 2 * 2 * 2, so replace n with 2 + 2 + 2 = 6.
6 = 2 * 3, so replace n with 2 + 3 = 5.
5 is the smallest value n will take on.
Example 2:

Input: n = 3
Output: 3
Explanation: Initially, n = 3.
3 is the smallest value n will take on.

Constraints:

2 <= n <= 10^5
'''


class Solution:
  def smallestValue(self, n: int) -> int:
    def siev(n: int):
      s = [i for i in range(n+1)]
      for i in range(2, n):
        if s[i] < i:
          continue
          
        for j in range(i*i, n+1, i):
          if s[j] > i:
            s[j] = i
            
      # print(s)
      return s
      
    s = siev(n)
    while s[n] != n:
      val = n
      nxt = 0
      
      while s[val] != val:
        nxt += s[val]
        val //= s[val]

      # print('after:', n, nxt, val)
      if nxt+val == n:
        break
        
      n = nxt + val
      
    return n
      