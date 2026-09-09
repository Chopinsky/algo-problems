'''
3964-minimum-lights-to-illuminate-a-road
'''


class Solution:
  def minLights(self, lights: list[int]) -> int:
    cnt = 0
    n = len(lights)
    cand = sorted([(max(0, i-val), min(n-1, i+val)) for i, val in enumerate(lights) if val > 0])
    # print('init:', cand)

    def count(val: int) -> int:
      return val//3 + (1 if val%3 > 0 else 0)

    if not cand:
      return count(n)

    merged = []
    for l, r in cand:
      if not merged or l-1 > merged[-1][1]:
        merged.append([l, r])
      else:
        merged[-1][1] = max(merged[-1][1], r)

    # print('merged:', merged)
    for i, [l, r] in enumerate(merged):
      if i == 0 and l > 0:
        cnt += count(l)
        # print('left:', count(l))

      if i == len(merged)-1 and r < n-1:
        cnt += count(n-1-r)

      if i > 0:
        cnt += count(l-1-merged[i-1][1])

    return cnt
