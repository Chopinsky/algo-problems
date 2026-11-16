'''
2243-calculate-digit-sum-of-a-string
'''


class Solution:
  def digitSum(self, s: str, k: int) -> str:
    while len(s) > k:
      ln = len(s)  
      n = ln//k + (0 if ln%k == 0 else 1)
      cand = [s[k*i:k*(i+1)] for i in range(n) if len(s[k*i:k*(i+1)]) > 0]
      vals = [str(sum(int(d) for d in val)) for val in cand]
      # print('iter:', s, cand, vals)
      s = ''.join(vals)

    return s
        