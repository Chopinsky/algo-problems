'''
2761-prime-pairs-with-target-sum
'''

from typing import List


top = 10**6 + 1
nums = [val for val in range(top)]

for v0 in range(2, top):
  if nums[v0] < v0:
    continue

  for v1 in range(v0*v0, top, v0):
    nums[v1] = v0

primes = [val for i, val in enumerate(nums) if i == val and i >= 2]
ps = set(primes)


class Solution:
  def findPrimePairs(self, n: int) -> List[List[int]]:
    # print('init:', len(primes))
    ans = []

    for v0 in primes:
      v1 = n-v0
      if v0 > v1:
        break

      # print('check:', v0, v1)
      if v1 in ps:
        ans.append([v0, v1])

    return ans    

