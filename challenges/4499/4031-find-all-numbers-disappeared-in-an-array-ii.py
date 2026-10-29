'''
4031-find-all-numbers-disappeared-in-an-array-ii
'''


class Solution:
  def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
    covered = []
    for val in sorted(set(nums)):
      if not covered or covered[-1][1]+1 != val:
        covered.append([val, val])
      else:
        covered[-1][1] += 1

    # print('init:', covered)
    res = []
    src = []

    for s, e in covered:
      if e < lower:
        continue

      if s > upper:
        break

      if s <= lower <= e:
        src.append((lower, e))
        continue

      if s <= upper <= e:
        src.append((s, upper))
        continue

      src.append((s, e))

    # print('init:', src)
    if not src:
      return [[lower, upper]]

    for i, (s, e) in enumerate(src):
      if i == 0 and s > lower:
        res.append((lower, s-1))

      if i > 0:
        res.append((src[i-1][1]+1, s-1))

      if i == len(src)-1 and e < upper:
        res.append((e+1, upper))

    return res
        