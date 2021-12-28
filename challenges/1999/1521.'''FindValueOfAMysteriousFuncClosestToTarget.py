'''
Mysterious function:
https://assets.leetcode.com/uploads/2020/07/09/change.png

Winston was given the above mysterious function func. He has an integer array arr and an integer target and he wants to find the values l and r that make the value |func(arr, l, r) - target| minimum possible.

Return the minimum possible value of |func(arr, l, r) - target|.

Notice that func should be called with the values l and r where 0 <= l, r < arr.length.

Example 1:

Input: arr = [9,12,3,7,15], target = 5
Output: 2
Explanation: Calling func with all the pairs of [l,r] = [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]], Winston got the following results [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0]. The value closest to 5 is 7 and 3, thus the minimum difference is 2.
Example 2:

Input: arr = [1000000,1000000,1000000], target = 1
Output: 999999
Explanation: Winston called the func with all possible values of [l,r] and he always got 1000000, thus the min difference is 999999.
Example 3:

Input: arr = [1,2,4,8,16], target = 0
Output: 0
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^6
0 <= target <= 10^7
'''


from typing import List
from collections import defaultdict, deque


class Solution:
  def closestToTarget(self, arr: List[int], target: int) -> int:
    # for i-th val, curr contains all range sums up to (i-1)-th element,
    # use `val & prev` will generate all possible values for all the range
    # sums up to i-th element
    curr = set()

    # this set will contain all possible sums for a continuous range
    all_and_sums = set()
    
    # keep updating the continuous range, and the all-possible range sums
    for val in arr:
      curr = {val} | {(val & prev) for prev in curr}
      all_and_sums |= curr
      
    return min(abs(val - target) for val in all_and_sums)
    
    
  def closestToTarget0(self, arr: List[int], target: int) -> int:
    # target is found in the array
    if target in arr:
      return 0

    # target is 0, `and` of the entire array will warrant the
    # min and_sum
    if not target:
      and_sum = arr[0]

      for val in arr[1:]:
        and_sum &= val
        if not and_sum:
          break
        
      return and_sum
      
    # print('before:', len(arr))
    trimmed = []
    for i, val in enumerate(arr):
      if trimmed and val == trimmed[-1]:
        continue
      
      trimmed.append(val)
      
    arr = trimmed
    # print('after:', len(arr))
    min_diff = min(abs(val-target) for val in arr)
    ones = defaultdict(deque)
    n = len(arr)
    
    for i, val in enumerate(arr):
      pos = 0
      
      while val > 0:
        if val & 1 == 1:
          ones[pos].append(i)
        
        val >>= 1
        pos += 1
    
    digits = sorted(ones)
    # print(digits, sum(len(ones[d]) for d in digits))
    
    def calc_and_sum(i: int, j: int) -> int:
      if j <= i:
        return arr[i]
        
      if j >= n:
        j = n-1
        
      base = 0
      
      for d in digits:
        if not ones[d]:
          continue
          
        if ones[d][0] == i and j-i < len(ones[d]) and ones[d][j-i] == j:
          base |= (1 << d)
        
      return base
    
    def find_range_min_diff(i: int) -> int:
      diff = abs(arr[i] - target)
      if (i < n-1) and (arr[i]&arr[i+1] == 0):
        return min(diff, target)
      
      l, r = i, n

      while l < r:
        m = (l + r) // 2
        m_val = calc_and_sum(i, m)
        
        if m_val == target:
          return 0
        
        diff = min(diff, abs(m_val - target))
        
        if m_val < target:
          r = m - 1
        else:
          l = m + 1
      
      diff = min(diff, abs(calc_and_sum(i, l) - target))
      # diff = min(diff, abs(calc_and_sum(i, l+1) - target))
      
      return diff
    
    def update_ones(i: int):
      for d in digits:
        if ones[d] and ones[d][0] == i:
          ones[d].popleft()
  
    for i in range(n):
      # arr[i:j] will only be equal or smaller than the value 
      # of arr[i], if arr[i] <= target, looping over j's will 
      # not give us a smaller abs-diff
      if arr[i] <= target:
        update_ones(i)
        continue
        
      ''' code below are unnecessary optimizations ....
      if (i == n-1) or (arr[i]&arr[i+1] <= target):
        if i < n-1:
          min_diff = min(min_diff, abs(arr[i]&arr[i+1] - target))
          
        update_ones(i)
        continue
        
      full_range = calc_and_sum(i, n-1)
      less_full_range = calc_and_sum(i, n-2)
      
      if less_full_range >= target and full_range <= target:
        min_diff = min(min_diff, abs(less_full_range-target), abs(full_range-target))
        update_ones(i)
        continue

      if full_range >= target and abs(full_range - target) >= min_diff:
        update_ones(i)
        continue
      '''

      min_diff = min(min_diff, find_range_min_diff(i))
      update_ones(i)
      
      if not min_diff:
        break
    
    return min_diff
