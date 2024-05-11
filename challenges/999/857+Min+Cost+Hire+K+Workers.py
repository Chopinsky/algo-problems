'''
There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0th worker and 35 to 2nd worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.

Constraints:

n == quality.length == wage.length
1 <= k <= n <= 10^4
1 <= quality[i], wage[i] <= 10^4

Test cases:

[10,20,5]
[70,50,30]
2
[3,1,10,10,1]
[4,8,2,2,7]
3
[14,56,59,89,39,26,86,76,3,36]
[90,217,301,202,294,445,473,245,415,487]
2
[4,4,4,5]
[13,12,13,12]
2
[32,43,66,9,94,57,25,44,99,19]
[187,366,117,363,121,494,348,382,385,262]
4
'''

from typing import List
from heapq import heappush, heappop, heappushpop
import math

class Solution:
  def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
    if k == 1:
      return min(wage)
    
    n = len(quality)
    workers = sorted((wage[i]/quality[i], quality[i], i) for i in range(n))
    quality_sum = 0
    stack = []
    cost = 0
    # print('init:', workers)
    
    for i, (r, q, idx) in enumerate(workers):
      if i < k:
        quality_sum += q
        heappush(stack, -q)
        cost = quality_sum * r
        continue
        
      # print('iter:', (idx, r, q), stack)
      
      q_pop = heappushpop(stack, -q)
      quality_sum += q_pop + q
      cost = min(cost, quality_sum*r)
    
    return cost
        
  '''
  the idea is that the payment is determined by the highest `wage/quality` ratio of the
  worker in the group, times the total quality points from the workers in the group.

  hence we can sort the workers by their ratios, and add them into the pool from low
  ratio to high ratio, then only use those with the smallest quality points.
  '''
  def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
    n = len(wage)
    workers = sorted(((wage[i]/quality[i]), quality[i], wage[i]) for i in range(n))
    ans = math.inf
    worker_pool = []
    total_group_quality = 0

    for ratio, q, _ in workers:
      # add the worker to the pool, since all workers in the 
      # pool has a smaller ratio, they can be used to form 
      # the payment group as the ratio will be determined
      # by the highest ratio in the group, which is `ratio`
      # since `workers` are sorted by `ratio` increamentally
      heappush(worker_pool, -q)
      total_group_quality += q

      # if we have more than k workers, remove the one 
      # with the most quality points -- since `pool` is
      # a max-heap, the top value is negative, so `+=`
      # serves as the removal
      if len(worker_pool) > k:
        total_group_quality += heappop(worker_pool)

      # we have gathered k workers with the min total 
      # quality points, calc the total money to be paid out
      if len(worker_pool) == k:
        ans = min(ans, ratio * total_group_quality)

    return float(ans)


  def mincostToHireWorkers0(self, q: List[int], w: List[int], k: int) -> float:
    if k == 1:
      return min(w)
    
    n = len(q)
    base = sorted([(w[i]/q[i], i) for i in range(n)], reverse=True)
    size = sorted([(q[i], i) for i in range(n)], reverse=True)
    oor = set()
    
    money_total = math.inf
    size_total = 0
    size_heap = []
    size_dict = set() #defaultdict(int)
    
    # build the initial quality worker's size heap
    for i in range(k):
      q0, idx = size.pop()
      heappush(size_heap, (-q0, idx))
      size_dict.add(idx)
      size_total += q0
    
    # print('init', base, size_total, size_dict, size_heap)
    
    for ratio, i in base:
      # print('before', i, size_total, size_dict, size_heap)
      if i in size_dict:
        # this worker is already in the smallest quality size
        # heap, no need to make any change
        curr_total = ratio * size_total
        
      else:
        # this worker is not in the smallest quality size
        # heap, replace the largest quality point worker from
        # the heap with this worker, then calculate the total points
        last_size, _ = size_heap[0]
        curr_size = size_total + last_size + q[i]
        curr_total = ratio * curr_size
        
      # print(i, ratio, curr_total)
      money_total = min(money_total, curr_total)
      oor.add(i)
      
      # the q[i] size can no longer be used as we move on to visit
      # higher ratios
      if i in size_dict:
        size_dict.discard(i)
        while size_heap and (size_heap[0][1] not in size_dict):
          heappop(size_heap)
      
        # find the next smallest quality size to be added
        nxt_q, idx = 0, -1
        while size:
          nxt_q, idx = size.pop()
          if idx not in oor:
            break
            
          idx = -1
            
        # can't find the next smallest size, we're done
        if idx < 0:
          break
          
        size_total += nxt_q - q[i]
        size_dict.add(idx)
        heappush(size_heap, (-nxt_q, idx))
      
    return money_total
    