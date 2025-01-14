'''
2947. Count Beautiful Substrings I
'''

class Solution:
  def beautifulSubstrings(self, s: str, k: int) -> int:
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    count = 0
    n = len(s)

    for i in range(n):
      v_cnt = 0
      for j in range(i, n):
        if s[j] in vowels:
          v_cnt += 1

        c_cnt = (j-i+1) - v_cnt
        if v_cnt == c_cnt and (v_cnt*c_cnt)%k == 0:
          count += 1

    return count
