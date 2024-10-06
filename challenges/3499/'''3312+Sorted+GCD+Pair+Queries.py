'''
3312. Sorted GCD Pair Queries
'''

from collections import Counter, defaultdict
from typing import List
from bisect import bisect_left

MAX = 5*10**4 + 1
divisors = [list() for _ in range(MAX)]

for v0 in range(1, MAX):
  for v1 in range(v0, MAX, v0):
    divisors[v1].append(v0)


class Solution:
  '''
  the idea is to calculate the count of value pairs for common denominator, this will be done
  be get the counter of values [1, MAX], then check and count the number of values that has 
  `number` as one of its denominator, then the total count of paris for `number` is 
  `pairs[num] = count*(count-1)//2`, then the GCD for `number` will be 
  `pairs[num] - sum(pairs[val] for val in range(2*num, MAX+1, num))`, in this case, we deduct
  the count of the pairs at larger common denomirnators, aka remove the duplicate counts as 
  we only care about GCD;

  once we have the `pairs`, we can use the prefix sum of counts to get the i-th count of the
  GCD pair easily;
  '''
  def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
    vals = Counter(nums)
    counter = defaultdict(int)
    top = -1
    
    for val, cnt in vals.items():
      top = max(top, val)
      for d in divisors[val]:
        counter[d] += cnt
        
    # print('init:', counter)
    pairs = defaultdict(int)
    
    for val in range(top, 0, -1):
      cnt = counter[val]
      if cnt <= 1:
        continue
        
      pairs[val] += (cnt * (cnt-1)) // 2
      for val_mul in range(2*val, top+1, val):
        pairs[val] -= pairs.get(val_mul, 0)
    
    # print('agg:', pairs)
    cand = sorted(pairs.keys())
    prefix = []
    ans = []
    
    for val in cand:
      if not prefix:
        prefix.append(pairs[val]-1)
      else:
        prefix.append(prefix[-1]+pairs[val])
    
    # print('prefix:', cand, prefix)
    for q in queries:
      idx = bisect_left(prefix, q)
      ans.append(cand[idx])
    
    return ans
        