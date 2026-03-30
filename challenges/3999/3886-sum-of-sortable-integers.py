'''
3886-sum-of-sortable-integers
'''


def divisors(n: int) -> list[int]:
  if n <= 0:
    return []

  res = []
  i = 2

  while i*i <= n:
    if n % i == 0:
      res.append(i)
      j = n // i
      if j != i:
        res.append(j)
    
    i += 1

  res.sort()
  res.append(n)

  return res

class Solution:
  def sortableIntegers(self, nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
      return 1

    total = 0 
    d = divisors(n)

    # the array is already sorted
    if all(nums[i] >= nums[i-1] for i in range(1, n)):
      return sum(d)+1
    
    vals = { div: [None]*(n//div) for div in d }
    prefix = [0]*n

    for i in range(n):
      val = nums[i]

      if i > 0:
        prefix[i] = prefix[i-1]
        if val < nums[i-1]:
          prefix[i] += 1 

      for div, lst in vals.items():
        j = i//div
        if lst[j] is None:
          lst[j] = [val, val]
        else:
          lst[j][0] = min(lst[j][0], val)
          lst[j][1] = max(lst[j][1], val)

    # print('prefix:', prefix)
    # print('vals:', vals)

    def is_qualified(div: int, lst: list) -> bool:
      for i in range(len(lst)):
        # mismatch
        if i > 0 and lst[i][0] < lst[i-1][1]:
          return False

        l = i*div
        r = (i+1)*div - 1
        cnt = prefix[r] - (0 if l == 0 else prefix[l-1])

        # can't rotate to be sorted
        if cnt > 1:
          return False

        # actually 2 drops
        if cnt == 1 and nums[l] < nums[r]:
          return False

      return True

    for div, lst in vals.items():
      if is_qualified(div, lst):
        total += div

    return total
