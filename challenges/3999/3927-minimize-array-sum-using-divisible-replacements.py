'''
3927-minimize-array-sum-using-divisible-replacements
'''

from collections import Counter


class Solution:
  def minArraySum(self, nums: list[int]) -> int:
    cnt = Counter(nums)
    cand = sorted(cnt)

    # replace all with 1
    if 1 in cand:
      return len(nums)

    top = cand[-1]
    for val in cand:
      # merged
      if val not in cnt:
        continue

      # find dividers
      nxt = val+val
      while nxt <= top:
        if nxt in cnt:
          c0 = cnt[nxt]
          cnt[val] += c0
          del cnt[nxt]

        nxt += val

    return sum(v*c for v, c in cnt.items())
        