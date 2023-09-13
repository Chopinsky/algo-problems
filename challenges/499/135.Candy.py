'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Constraints:

n == ratings.length
1 <= n <= 2 * 10 ** 4
0 <= ratings[i] <= 2 * 10 ** 4
'''

from collections import defaultdict
from typing import List
from heapq import heappop, heappush


class Solution:
  def candy(self, ratings: List[int]) -> int:
    n = len(ratings)
    if n == 1:
      return 1
    
    if n == 2:
      return 2 if ratings[0] == ratings[1] else 3
    
    stack = sorted([(r, i) for i, r in enumerate(ratings)])
    candies = [1] * n
    # print(stack)
    
    for _, idx in stack:
      if idx == 0:
        if ratings[idx] > ratings[idx+1]:
          candies[idx] += candies[idx+1]
          
        continue
        
      if idx == n-1:
        if ratings[idx] > ratings[idx-1]:
          candies[idx] += candies[idx-1]
          
        continue
        
      if ratings[idx] > ratings[idx-1] and ratings[idx] > ratings[idx+1]:
        candies[idx] = 1 + max(candies[idx-1], candies[idx+1])
      elif ratings[idx] > ratings[idx-1]:
        candies[idx] = 1 + candies[idx-1]
      elif ratings[idx] > ratings[idx+1]:
        candies[idx] = 1 + candies[idx+1]
      
    # print(candies)
    return sum(candies)
        

  def candy(self, ratings: List[int]) -> int:
    n = len(ratings)
    if n == 1:
      return 1
    
    cnt = [0] * n
    cand = []
    
    for i, r in enumerate(ratings):
      heappush(cand, (r, i))
      
    small = cand[0][0]
    while cand:
      curr, i = heappop(cand)
      if curr == small:
        cnt[i] = 1
        continue
        
      if i == 0:
        cnt[i] = 1 if ratings[i+1] == curr else cnt[i+1] + 1
        
      elif i == n-1:
        cnt[i] = 1 if ratings[i-1] == curr else cnt[i-1] + 1
          
      else:
        min_cnt = 1
        if ratings[i-1] < curr:
          min_cnt = max(min_cnt, cnt[i-1]+1)
          
        if ratings[i+1] < curr:
          min_cnt = max(min_cnt, cnt[i+1]+1)
          
        cnt[i] = min_cnt
        
    # print(cnt)
    return sum(cnt)
    

  def candy(self, ratings: List[int]) -> int:
    nums = []
    n = len(ratings)
    candy = [0] * n
    rp = defaultdict(list)
    
    for i, r in enumerate(ratings):
      if len(rp[r]) == 0:
        nums.append(r)
        
      rp[r].append(i)
      
    nums.sort()
    # print(nums, rp)
    
    for r in nums:
      for pos in rp[r]:
        lc, rc = 0, 0
        if pos > 0 and ratings[pos] > ratings[pos-1]:
          lc = candy[pos-1]
          
        if pos < n-1 and ratings[pos] > ratings[pos+1]:
          rc = candy[pos+1]
          
        candy[pos] = max(lc, rc) + 1
        # print(pos, lc, rc, candy)
        
    # print(candy)
    
    return sum(candy)
  