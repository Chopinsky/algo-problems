'''
# Minimum Moves to Pick K Ones

## Descriptions

You are given a 0-indexed binary array nums of length n, a positive integer k and a non-negative integer maxChanges.

Dylan Smith plays a game, where the goal is for Dylan to pick up k ones from nums using the minimum number of moves. When the game starts, Dylan picks up any index dylanIndex in the range [0, n - 1] and stands there. If nums[dylanIndex] == 1 , Dylan picks up the one and nums[dylanIndex] becomes 0(this does not count as a move). After this, Dylan can make any number of moves (including zero) where in each move Dylan must perform exactly one of the following actions:

Select any index j != dylanIndex such that nums[j] == 0 and set nums[j] = 1. This action can be performed at most maxChanges times.
Select any two adjacent indices x and y (|x - y| == 1) such that nums[x] == 1, nums[y] == 0, then swap their values (set nums[y] = 1 and nums[x] = 0). If y == dylanIndex, Dylan picks up the one after this move and nums[y] becomes 0.
Return the minimum number of moves required by Dylan to pick exactly k ones.

Example 1:

Input: nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1

Output: 3

Explanation: Dylan can pick up 3 ones in 3 moves, if Dylan performs the following actions in each move when standing at dylanIndex == 1:

 At the start of the game Dylan picks up the one and nums[1] becomes 0. nums becomes [1,0,1,0,0,1,1,0,0,1].
Select j == 2 and perform an action of the first type. nums becomes [1,0,1,0,0,1,1,0,0,1]
Select x == 2 and y == 1, and perform an action of the second type. nums becomes [1,1,0,0,0,1,1,0,0,1]. As y == dylanIndex, Dylan picks up the one and nums becomes [1,0,0,0,0,1,1,0,0,1].
Select x == 0 and y == 1, and perform an action of the second type. nums becomes [0,1,0,0,0,1,1,0,0,1]. As y == dylanIndex, Dylan picks up the one and nums becomes [0,0,0,0,0,1,1,0,0,1].
Note that it may be possible for Dylan to pick up 3 ones using some other sequence of 3 moves.

Example 2:

Input: nums = [0,0,0,0], k = 2, maxChanges = 3

Output: 4

Explanation: Dylan can pick up 2 ones in 4 moves, if Dylan performs the following actions in each move when standing at dylanIndex == 0:

Select j == 1 and perform an action of the first type. nums becomes [0,1,0,0].
Select x == 1 and y == 0, and perform an action of the second type. nums becomes [1,0,0,0]. As y == dylanIndex, Dylan picks up the one and nums becomes [0,0,0,0].
Select j == 1 again and perform an action of the first type. nums becomes [0,1,0,0].
Select x == 1 and y == 0 again, and perform an action of the second type. nums becomes [1,0,0,0]. As y == dylanIndex, Dylan picks up the one and nums becomes [0,0,0,0].

## Constraints:

2 <= n <= 10^5
0 <= nums[i] <= 1
1 <= k <= 10^5
0 <= maxChanges <= 10^5
maxChanges + sum(nums) >= k

## Test Cases
[0,0]
3
3
[1,1,0,0,0,1,1,0,0,1]
3
1
[0,0,0,0]
2
3
[1,0,0]
1
0
[0,1,0,0,1,0]
3
1
[1,0,1,0,1,1,0,0,0,1,0]
7
4
'''

from typing import List
from bisect import bisect_left, bisect_right

class Solution:
  def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
    n = len(nums)
    min_ops = float('inf')
    pos, prefix = [], []
    debug = False
    
    for i in range(n):
      if nums[i] == 0:
        continue
        
      pos.append(i)
      if not prefix:
        prefix.append(i)
      else:
        prefix.append(i+prefix[-1])
    
    if debug:
      print('init:', pos, prefix)
    
    def get_dist(i: int) -> int:
      l, r = 1, n
      last = l
      target = k - maxChanges
      
      while l <= r:
        mid = (l+r) // 2
        ldx = max(0, i-mid)
        rdx = min(n, i+mid)
        
        lptr = bisect_left(pos, ldx)
        rptr = bisect_right(pos, rdx)-1
        cnt = rptr-lptr+1
        # print('bi:', i, shift, cnt, (ldx, lptr), (rdx, rptr))
        
        if cnt >= target:
          last = mid
          r = mid - 1
        else:
          l = mid + 1
        
      return last
    
    def get_ops(start, end):
      if end < start or start >= len(prefix):
        return 0, 0
      
      cnt = end - start + 1
      ops = prefix[end] - (0 if start == 0 else prefix[start-1])
      
      return ops, cnt
      
    def get_left_ops(i: int, j: int):
      start = bisect_left(pos, j)
      end = bisect_left(pos, i)-1
      # print('left-0:', (i, j), (start, end))
      p0, cnt = get_ops(start, end)
      # print('left-1:', (p0, cnt), cnt*i-p0)
      return cnt*i-p0, cnt
      
    def get_right_ops(i: int, j: int):
      start = bisect_right(pos, i)
      end = bisect_right(pos, j)-1
      # print('right-0:', (i, j), (start, end))
      p0, cnt = get_ops(start, end)
      # print('right-1:', (p0, cnt), p0-cnt*i)
      return p0-cnt*i, cnt
    
    def count(i: int):
      ops = 0
      rem = k-1 if nums[i] == 1 else k
      # print('start:', i, ops, rem)
      
      # just swap
      if rem > 0 and i-1 >= 0 and nums[i-1] == 1:
        rem -= 1
        ops += 1
        
      # just swap
      if rem > 0 and i+1 < n and nums[i+1] == 1:
        rem -= 1
        ops += 1
        
      # set neighbor to 1 and swap
      if rem > 0 and maxChanges > 0:
        cnt = min(rem, maxChanges)
        rem -= cnt
        ops += 2*cnt
        
      # done with the easy ops
      if rem == 0:
        # print('*** early:', i, ops)
        return ops
      
      d = get_dist(i)
      ops = 2*maxChanges
      lops, lcnt = get_left_ops(i, max(0, i-d))
      rops, rcnt = get_right_ops(i, min(n-1, i+d))
      
      if debug:
        print('--- check:', i, d, (lops, lcnt), (rops, rcnt))
      
      # taken 1 more node than needed, back it out
      if lcnt+rcnt+maxChanges+nums[i] > k:
        # print('???', lcnt+rcnt+maxChanges+nums[i])
        ops -= d
      
      if debug:
        print('*** late:', (ops, lops, rops), ops+lops+rops)
        
      return ops+lops+rops
    
    for i in range(n):
      min_ops = min(min_ops, count(i))
    
    return min_ops
        