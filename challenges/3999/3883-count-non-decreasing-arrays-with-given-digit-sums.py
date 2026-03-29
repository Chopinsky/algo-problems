'''
3883-count-non-decreasing-arrays-with-given-digit-sums
'''

from collections import defaultdict


cand = defaultdict(list)
for val in range(5001):
  s = sum(int(d) for d in str(val))
  cand[s].append(val)


class Solution:
  def countArrays(self, digit_sum: list[int]) -> int:
    # print('init:', cand)
    if any(val not in cand for val in digit_sum):
      return 0
    
    mod = 10**9 + 7
    i = len(digit_sum)-1
    curr = [1]*len(cand[digit_sum[i]])
    nxt = []
    # print('init:', curr)

    while i > 0 and curr:
      i -= 1
      lst = cand[digit_sum[i]]
      prev = cand[digit_sum[i+1]]
      j = len(lst)-1
      k = len(prev)-1
      accu = 0
      # print('iter:', i, curr)
      # print('vals:', lst, prev)

      while j >= 0:
        val = lst[j]
        while k >= 0 and prev[k] >= val:
          accu += curr[k]
          k -= 1

        nxt.append(accu%mod)
        j -= 1
        # print('inner:', k, accu, (val, prev[k]))

      nxt = nxt[::-1]
      curr, nxt = nxt, curr
      nxt.clear()
      # print('end:', curr)

    return sum(curr)%mod if curr else 0
