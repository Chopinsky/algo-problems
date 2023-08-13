'''
2818. Apply Operations to Maximize Score

You are given an array nums of n positive integers and an integer k.

Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:

Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
Multiply your score by x.
Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.

The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.

Return the maximum possible score after applying at most k operations.

Since the answer may be large, return it modulo 109 + 7.

Example 1:

Input: nums = [8,3,9,3,8], k = 2
Output: 81
Explanation: To get a score of 81, we can apply the following operations:
- Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
It can be proven that 81 is the highest score one can obtain.
Example 2:

Input: nums = [19,12,14,6,10,18], k = 3
Output: 4788
Explanation: To get a score of 4788, we can apply the following operations: 
- Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0]. The score becomes 1 * 19 = 19.
- Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5]. The score becomes 19 * 18 = 342.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index. Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
It can be proven that 4788 is the highest score one can obtain.

Constraints:

1 <= nums.length == n <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= min(n * (n + 1) / 2, 10^9)
'''

from typing import List
from math import pow


class Solution:
  def maximumScore(self, nums: List[int], k: int) -> int:
    mod = 10**9 + 7
    score = 1
    n = len(nums)
    
    def get_prime_score(t: int):
      s = [i for i in range(t+1)]
      c = [0] * (t+1)
      
      for v0 in range(2, t+1):
        if s[v0] < v0:
          continue
          
        c[v0] += 1
        # print('prime:', v0)
        
        for v1 in range(2*v0, t+1, v0):
          s[v1] = v0
          c[v1] += 1
        
      return c
    
    count = get_prime_score(max(nums))
    c = [count[v] for v in nums]
    
    left = [-1]*n
    right = [n]*n
    # print(c)
    
    src = sorted((v, i) for i, v in enumerate(c))
    stack = []

    # clac left
    for i in range(n):
      while stack and c[i] > c[stack[-1]]:
        stack.pop()
        
      if stack:
        left[i] = stack[-1]
        
      stack.append(i)
        
    stack.clear()
    
    # calc right
    for i in range(n-1, -1, -1):
      while stack and c[i] >= c[stack[-1]]:
        stack.pop()
        
      if stack:
        right[i] = stack[-1]
      
      stack.append(i)
    
    src = sorted([(v, i) for i, v in enumerate(nums)], reverse=True)
    for val, idx in src:
      if val <= 1 or k <= 0:
        break
      
      cnt = min(k, (idx-left[idx])*(right[idx]-idx))
      # print(val, cnt, (idx-left[idx]), right[idx]-idx)
      
      score = (score * pow(val, cnt, mod)) % mod
      k -= cnt
    
    return score
  