'''
!0001!1000!!110!0101 
9
3
'''

from typing import Dict

class Solution:
  def get_min_errors(self, s: str, x: int, y: int) -> int:
    mod = 10**9 + 7

    def update(cnt: Dict, prev: int, is_one: bool) -> Dict:
      res = {}

      for one_cnt, score in cnt.items():
        zero_cnt = prev - one_cnt

        if is_one:
          # add '01' pairs
          score += x * zero_cnt
          one_cnt += 1
        else:
          # add '10' pairs
          score += y * one_cnt

        res[one_cnt] = min(res.get(one_cnt, float('inf')), score)

      return res
    
    ones = {0:0}
    for i, d in enumerate(s):
      print(i, d)

      if d == '0':
        ones = update(ones, i, False)
        # print(ones)
        continue

      if d == '1':
        ones = update(ones, i, True)
        # print(ones)
        continue

      # '!' can be one and can be zero
      nxt1 = update(ones, i, True)
      nxt0 = update(ones, i, False)

      for c0, s0 in nxt0.items():
        if c0 in nxt1:
          nxt1[c0] = min(nxt1[c0], s0)
        else:
          nxt1[c0] = s0

      ones = nxt1
      # print(ones)

    # print('done:', ones)
    return min(ones.values()) % mod

test_cases = [
  ['!0001!1000!!11', 9, 3],
  # ['!0001!1000!!110!0101', 9, 3],
]

if __name__ == '__main__':
  s = Solution()
  for test_case in test_cases:
    res = s.get_min_errors(test_case[0], test_case[1], test_case[2])
    print(test_case)
    print(res)
