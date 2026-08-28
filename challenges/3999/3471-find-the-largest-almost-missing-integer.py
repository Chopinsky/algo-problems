'''
3471-find-the-largest-almost-missing-integer
'''


class Solution:
  def largestInteger(self, nums: List[int], k: int) -> int:
    cand = sorted(set(nums), reverse=True)
    sub = []
    res = None

    for i in range(len(nums)-k+1):
      sub.append(set(nums[i:i+k]))

    # print('init', sub)
    def check(val: int) -> bool:
      cnt = sum(1 if val in arr else 0 for arr in sub)
      return cnt == 1

    for val in cand:
      if check(val):
        return val

    return -1
