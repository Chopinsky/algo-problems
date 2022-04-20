'''
Alice is a caretaker of n gardens and she wants to plant flowers to maximize the total beauty of all her gardens.

You are given a 0-indexed integer array flowers of size n, where flowers[i] is the number of flowers already planted in the ith garden. Flowers that are already planted cannot be removed. You are then given another integer newFlowers, which is the maximum number of flowers that Alice can additionally plant. You are also given the integers target, full, and partial.

A garden is considered complete if it has at least target flowers. The total beauty of the gardens is then determined as the sum of the following:

The number of complete gardens multiplied by full.
The minimum number of flowers in any of the incomplete gardens multiplied by partial. If there are no incomplete gardens, then this value will be 0.
Return the maximum total beauty that Alice can obtain after planting at most newFlowers flowers.

 

Example 1:

Input: flowers = [1,3,1,1], newFlowers = 7, target = 6, full = 12, partial = 1
Output: 14
Explanation: Alice can plant
- 2 flowers in the 0th garden
- 3 flowers in the 1st garden
- 1 flower in the 2nd garden
- 1 flower in the 3rd garden
The gardens will then be [3,6,2,2]. She planted a total of 2 + 3 + 1 + 1 = 7 flowers.
There is 1 garden that is complete.
The minimum number of flowers in the incomplete gardens is 2.
Thus, the total beauty is 1 * 12 + 2 * 1 = 12 + 2 = 14.
No other way of planting flowers can obtain a total beauty higher than 14.
Example 2:

Input: flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6
Output: 30
Explanation: Alice can plant
- 3 flowers in the 0th garden
- 0 flowers in the 1st garden
- 0 flowers in the 2nd garden
- 2 flowers in the 3rd garden
The gardens will then be [5,4,5,5]. She planted a total of 3 + 0 + 0 + 2 = 5 flowers.
There are 3 gardens that are complete.
The minimum number of flowers in the incomplete gardens is 4.
Thus, the total beauty is 3 * 2 + 4 * 6 = 6 + 24 = 30.
No other way of planting flowers can obtain a total beauty higher than 30.
Note that Alice could make all the gardens complete but in this case, she would obtain a lower total beauty.
 

Constraints:

1 <= flowers.length <= 10^5
1 <= flowers[i], target <= 10^5
1 <= newFlowers <= 10^10
1 <= full, partial <= 10^5
'''

from typing import List
from bisect import bisect_left, bisect_right


class Solution:
  def maximumBeauty0(self, A: List[int], new: int, t: int, full: int, part: int) -> int:
    A = [min(t, a) for a in A]
    A.sort()

    # Two edge cases
    if min(A) == t: 
      return full * len(A)
    
    if new >= t * len(A) - sum(A):
      return max(full*len(A), full*(len(A)-1) + part*(t-1))

    # Build the array `cost`.
    cost = [0]
    for i in range(1, len(A)):
      pre = cost[-1]
      cost.append(pre + i * (A[i] - A[i - 1]))

    # Since there might be some gardens having `target` flowers already, we will skip them.
    j = len(A) - 1
    while A[j] == t:
      j -= 1

    # Start the iteration
    ans = 0
    while new >= 0:
      # idx stands for the first `j` gardens, notice a edge case might happen.
      idx = min(j, bisect_right(cost, new) - 1)

      # bar is the current minimum flower in the incomplete garden
      bar = A[idx] + (new - cost[idx]) // (idx + 1)
      ans = max(ans, bar * part + full *(len(A) - j - 1))

      # Now we would like to complete garden j, thus deduct the cost for garden j 
      # from new and move on to the previous(next) incomplete garden!
      new -= (t - A[j])
      j -= 1

      return ans


  def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
    n = len(flowers)
    flowers.sort()
    if flowers[0] >= target:
      return n * full
    
    prefix = [val for val in flowers]
    for i in range(1, n):
      prefix[i] += prefix[i-1]
      
    idx = bisect_left(flowers, target)
    if idx == 0:
      return n * full
      
    rem = newFlowers
    full_score = full * (n - idx)
    max_score = full_score + flowers[0] * partial
    # print('init', flowers, idx, full_score, max_score)
    
    def get_needed(m: int, i: int) -> int:
      j = bisect_right(flowers, m) - 1
      j = min(i, j)
      if j < 0:
        return 0
      
      if j >= n:
        return m*n - prefix[-1]
        
      # print('needed:', m, i, j)
      return max(0, m*(j+1) - prefix[j])
    
    def get_count(rem: int, i: int) -> int:
      l, r = flowers[0], target
      last = l
      
      while l < r:
        m = (l + r) // 2
        needed = get_needed(m, i)
        
        if needed == rem:
          last = m
          l = m
          break
          
        if needed < rem:
          last = m
          l = m + 1
        else:
          r = m - 1
          
      # print(last, rem, l, get_needed(l, i))
      if l < target and get_needed(l, i) <= rem:
        last = max(last, l)
        
      return last
    
    while idx >= 0 and rem >= 0:
      last = get_count(rem, idx-1) if idx > 0 else 0
      # print('iter:', idx, last, full_score, last*partial + full_score, rem)
      
      max_score = max(max_score, last*partial + full_score)
      idx -= 1    
      
      if idx >= 0:
        full_score += full
        rem -= target - flowers[idx]
        
    return max_score
  