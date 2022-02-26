'''
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:

0 <= i < j <= n - 1 and
nums[i] * nums[j] is divisible by k.

Example 1:

Input: nums = [1,2,3,4,5], k = 2
Output: 7
Explanation: 
The 7 pairs of indices whose corresponding products are divisible by 2 are
(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 3), and (3, 4).
Their products are 2, 4, 6, 8, 10, 12, and 20 respectively.
Other pairs such as (0, 2) and (2, 4) have products 3 and 15 respectively, which are not divisible by 2.    
Example 2:

Input: nums = [1,2,3,4], k = 5
Output: 0
Explanation: There does not exist any pair of indices whose corresponding product is divisible by 5.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i], k <= 10^5
'''


from collections import defaultdict
from math import gcd
from typing import List


class Solution:
  def countPairs(self, nums, k: int) -> int:
    cnt = defaultdict(int)
    
    # get all the gcd values with k, this will be the 
    # gcd multiplier number `val` can provide in the pair
    for val in nums:
      cnt[gcd(val, k)] += 1
      
    # get all the base numbers that `nums` can offer
    arr, m = list(cnt.keys()), len(cnt)

    # count the pairs where one offers d1 as the base multiplier,
    # and the other offers d2 as the base multiplier, and we want 
    # to count the pairs if d1 * d2 can be divided by k
    def count_pairs(d1: int, d2: int):
      # not divisible by k
      if (d1*d2) % k != 0: 
        return 0
      
      # if d1 == d2, take pairs from the same set; otherwise, take
      # all the combos from cnt[d1] and cnt[d2]
      return cnt[d1]*cnt[d2] if d1 != d2 else cnt[d1]*(cnt[d1]-1)//2

    total = 0
    
    # try to match all the base numbers
    for i in range(m):
      for j in range(i, m):
        total += count_pairs(arr[i], arr[j])
    
    return total
  
  
  def countPairs0(self, nums: List[int], k: int) -> int:
    n = len(nums)
    seen = defaultdict(int)
    top = max(nums)
    
    def get_sive(n: int) -> int:
      s = [i for i in range(n+1)]
      for i in range(2, n+1):
        if s[i] != i:
          continue
          
        for j in range(i*i, n+1, i):
          # if s[j] > i:
          s[j] = i
            
      return s
            
    sive = get_sive(top)
    # print(sive)
    
    count = 0
    added = set()
    
    for i, val in enumerate(nums):
      if val % k == 0:
        count += i
        # print('full', val, i)
        
      else:
        other = k // gcd(k, val)
        count += seen[other]
        # print('partial', val, other, seen[other], seen)
      
      # if a prime number itself, we're done
      if sive[val] == val:
        seen[val] += 1
        continue
        
      primes = []
      src = val
      
      while val > 1:
        f = sive[val]
        primes.append(f)
        val //= f
        
      # print(src, primes)
      div = set()
      nxt = set()
      
      for val in primes:
        nxt.add(val)
        for d in div:
          nxt.add(val * d)
          
        div |= nxt
        nxt.clear()
      
      # print(src, div)
      for val in div:
        seen[val] += 1
      
    return count
    