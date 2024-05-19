'''
3154. Find Number of Ways to Reach the K-th Stair

You are given a non-negative integer k. There exists a staircase with an infinite number of stairs, with the lowest stair numbered 0.

Alice has an integer jump, with an initial value of 0. She starts on stair 1 and wants to reach stair k using any number of operations. If she is on stair i, in one operation she can:

Go down to stair i - 1. This operation cannot be used consecutively or on stair 0.
Go up to stair i + 2jump. And then, jump becomes jump + 1.
Return the total number of ways Alice can reach stair k.

Note that it is possible that Alice reaches the stair k, and performs some operations to reach the stair k again.

Example 1:

Input: k = 0

Output: 2

Explanation:

The 2 possible ways of reaching stair 0 are:

Alice starts at stair 1.
Using an operation of the first type, she goes down 1 stair to reach stair 0.
Alice starts at stair 1.
Using an operation of the first type, she goes down 1 stair to reach stair 0.
Using an operation of the second type, she goes up 20 stairs to reach stair 1.
Using an operation of the first type, she goes down 1 stair to reach stair 0.
Example 2:

Input: k = 1

Output: 4

Explanation:

The 4 possible ways of reaching stair 1 are:

Alice starts at stair 1. Alice is at stair 1.
Alice starts at stair 1.
Using an operation of the first type, she goes down 1 stair to reach stair 0.
Using an operation of the second type, she goes up 20 stairs to reach stair 1.
Alice starts at stair 1.
Using an operation of the second type, she goes up 20 stairs to reach stair 2.
Using an operation of the first type, she goes down 1 stair to reach stair 1.
Alice starts at stair 1.
Using an operation of the first type, she goes down 1 stair to reach stair 0.
Using an operation of the second type, she goes up 20 stairs to reach stair 1.
Using an operation of the first type, she goes down 1 stair to reach stair 0.
Using an operation of the second type, she goes up 21 stairs to reach stair 2.
Using an operation of the first type, she goes down 1 stair to reach stair 1.

Constraints:

0 <= k <= 10^9
'''

from collections import defaultdict

class Solution:
  '''
  the state-space is small enough (at most 32 jumps) such that we can enumerate all 
  possible positions at i-th jump, and break the loop if we over-shot the target
  '''
  def waysToReachStair(self, k: int) -> int:
    count = 1 if k == 1 else 0
    jump = 1
    curr, nxt = defaultdict(int), defaultdict(int)
    curr[1] += 1
    
    while curr:
      # print('j:', jump, count, curr)
      
      for pos, cnt in curr.items():
        # print('iter:', jump, (pos, cnt))
        if pos > 0:
          if pos-1 == k:
            count += cnt
            
          if pos-1+jump == k:
            count += cnt
            
          nxt_pos = pos-1+jump
          if nxt_pos <= 2*k:
            nxt[pos-1+jump] += cnt
          
        if pos+jump == k:
          count += cnt
          
        nxt_pos = pos+jump
        if nxt_pos <= 2*k:
          nxt[pos+jump] += cnt
        
      # print('jump:', jump, curr, nxt)
      
      jump <<= 1
      if (k == 0 and jump > 2) or (k > 0 and jump > 4*k):
        # print('break')
        break
      
      curr, nxt = nxt, curr
      nxt.clear()
    
    return count
        