'''
4064-longest-subarray-divisible-by-k-with-at-most-one-negation-ii
'''


class Solution:
  def longestSubarray(self, nums: list[int], k: int) -> int:
    n = len(nums)
    prefix = [0] + nums.copy()

    # appearing index
    first = [n+1]*k
    last = [-1]*k

    for i in range(n+1):
      if i > 0:
        prefix[i] = (prefix[i-1] + prefix[i]) % k

      last[prefix[i]] = i
      if first[prefix[i]] > n:
        first[prefix[i]] = i

    # best is the subarray without changing values in it
    best = max(0, max(map(lambda x, y: x-y, last, first)))

    # the compensation amount with the negation change
    doubled = [(2*x)%k for x in nums]
    neg = [n+1]*k
    i = n-1

    # candidate scan -- reverse scan from the value last appeared
    cand = sorted(range(k), key=lambda x: first[x], reverse=True)
    # print('init:', best, first, last, cand)

    for val in cand:
      # val not seen in the array, skip
      start = first[val]
      if start > n:
        continue

      # adding values that's moved into the scope
      while i >= start:
        neg[doubled[i]] = i
        i -= 1

      # rotate last by val such that ends[v] is the last index for v
      ends = last[val:] + last[:val]

      # end is the index where by negating the v which is inside the subarray,
      # we can reach the modular of 0 which meets the k-divisible requirement
      end = max(list(ends[v0] for v0 in range(k) if neg[v0] < ends[v0]), default=-1)
      if end > start:
        best = max(best, end-start)

    return best
        