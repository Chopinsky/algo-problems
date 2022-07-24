from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution:
  '''
  this is a tricky math problem in the sense that you must understand what's the primary
  question the problem is actually asking: d(n1 & n2) + d(n1 | n2) == d(n1) + d(n2)

  let's break this down a little bit: d(n1) = d(a) + d(b), where a1 if the part that's unique
  to n1, and b1 is the part shared by both n1 and n2 (a and/or b can be 0), similarly we will
  have d(n2) = d(b) + d(c), where b is the unique part and c is the shared part, thus:
  d(n1 | n2) = d(a) + d(b) + d(c), and d(n1 & n2) = d(b), then sum the 2 parts together, we get:
  
      d(n1 | n2) + d(n1 & n2) == d(a) + d(b) + d(c) + d(b) 
                              == (d(a) + d(b)) + (d(b) + d(c)) 
                              == d(n1) + d(n2)

  then the problem transforms to "how many pairs can be formed with numbers with d0 digits and numbers
  with >= (k - d0) digits", which is trivial to solve at this point.
  '''
  def countExcellentPairs(self, nums: List[int], k: int) -> int:
    counter = defaultdict(int)
    
    def count_digits(val: int) -> int:
      cnt = 0
      while val > 0:
        if val & 1:
          cnt += 1
          
        val >>= 1
        
      return cnt
      
    for num in set(nums):
      digits = count_digits(num)
      counter[digits] += 1  
      
    d = sorted(counter)
    n = len(d)
    pairs_count = 0
    suffix_sums = [counter[val] for val in d]
    
    for i in range(n-2, -1, -1):
      suffix_sums[i] += suffix_sums[i+1]
    
    # print(counter, d, suffix_sums)
    for i in range(n):
      d0 = d[i]
      
      if 2*d0 < k:
        # find the number of digits that will sum to or beyond the target
        idx = bisect_left(d, k-d0)
        if idx < n:
          pairs_count += 2 * counter[d0] * suffix_sums[idx]
        
      else:
        # select within this digits count
        pairs_count += counter[d0] * counter[d0]
        
        # select from larger digits counts
        if i < n-1:
          pairs_count += 2 * counter[d0] * suffix_sums[i+1]
    
    return pairs_count
  