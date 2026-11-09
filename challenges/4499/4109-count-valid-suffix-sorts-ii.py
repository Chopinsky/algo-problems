'''
4109-count-valid-suffix-sorts-ii
'''


class Solution:
  def countSuffix(self, nums: list[int], target: list[int]) -> list[int]:
    n = len(nums)
    m = len(target)
    ans = [0] * (m-n+1)
    
    base = nums + [0] + target
    ln = len(base)
    z = [0]*(ln)
    l = 0
    r = 0

    # calc z-values
    for i in range(1, ln):
      if i <= r:
        z[i] = min(r-i+1, z[i-l])
      
      while i+z[i] < ln and base[z[i]] == base[i+z[i]]:
        z[i] += 1

      if i+z[i]-1 > r:
        l = i
        r = i+z[i]-1

    pre = [0]*m
    for i in range(1, m):
      pre[i] = pre[i-1] if target[i-1] >= target[i] else i

    freq = [0] * 100001
    bad = 0

    for val in nums:
      fx = freq[val]
      freq[val] -= 1
      if freq[val] == 0:
        bad -= 1

    for i in range(n):
      val = target[i]
      freq[val] += 1
      if freq[val] == 1:
        bad += 1

    anchor = n + 1
    for k in range(m-n+1):
      if bad == 0:
        right = k+n-1
        ldx = max(0, pre[right]-k)
        rdx = min(n-1, z[anchor+k])

        if ldx <= rdx:
          ans[k] = rdx - ldx + 1

      if k+n < m:
        v1 = target[k]
        freq[v1] -= 1
        if freq[v1] == 0:
          bad -= 1

        v2 = target[k+n]        
        freq[v2] += 1
        if freq[v2] == 1:
          bad += 1

    return ans

        