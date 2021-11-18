'''
Given strings S and T, find the minimum (contiguous) 
substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters 
in T, return the empty string "". If there are multiple such 
minimum-length windows, return the one with the left-most starting index.

Example:
Input: S = "abcdebdde", T = "bde"
Output: "bcde"

Explanation: 
There are many substrings with "bde" but the smallest amongst them is 
"bcde" and "bdde" of length 4. Out of these 2, "bcde" occurs first, Hence 
it is the answer.

Note:

- All the strings in the input will only contain lowercase letters.
- The length of S will be in the range [1, 20000].
- The length of T will be in the range [1, 100].
'''


import math
from collections import Counter, defaultdict
from bisect import bisect_right, bisect_left


class Solution:
  def min_win_subseq(self, s: str, t: str) -> str:
    m, n = len(s), len(t)
    if m < n:
      return ''

    if n == 1:
      return t if t in s else ''

    dp = [[-1]*(n) for _ in range(m)]
    res = ''
    min_len = math.inf

    for i in range(m):
      if s[i] == t[0]:
        dp[i][0] = i

      else:
        dp[i][0] = -1 if i == 0 else dp[i-1][0]

    for i in range(m):
      for j in range(1, min(i, n)):
        # if s[i] == t[j], get the 1st matching char from dp[i-1][j-1], otherwise
        # get it from dp[i-1][j], i.e. the last substr that has the matches
        dp[i][j] = dp[i-1][j-1] if (s[i] == t[j]) else dp[i-1][j]

      if dp[i][n-1] >= 0:
        # this valid substring start from dp[i][n] and ends at i
        l = i - dp[i][n-1] + 1
        if l < min_len:
          min_len = l
          res = s[dp[i][n-1]:i+1]

    # for i in range(m):
    #   print(s[i], dp[i])
    # print(min_len)

    return res


  def min_win_subseq0(self, s: str, t: str) -> str:
    sc = defaultdict(list)
    tc = Counter(t)

    for i, ch in enumerate(s):
      sc[ch].append(i)

    for ch, cnt in tc.items():
      if ch not in sc or cnt > len(sc[ch]):
        return ''

    if len(t) == 1:
      return t

    # print(sc)
    subseq = []
    seq_str = ''

    for ch in t:
      if not subseq:
        subseq.append(sc[ch][0])
      else:
        idx = bisect_right(sc[ch], subseq[-1])
        if idx >= len(sc[ch]):
          return ''

        subseq.append(sc[ch][idx])

    # tighten the left bound first
    if t[1] != t[0]:
      idx = bisect_left(sc[t[0]], subseq[1]) - 1
      # print('tighten to:', idx, sc[t[0]])
      if 0 <= idx < len(sc[t[0]]):
        subseq[0] = sc[t[0]][idx]

    seq_str = s[subseq[0]:subseq[-1]+1]
    init_idx = bisect_left(sc[t[0]], subseq[0])+1
    # print(subseq, seq_str, init_idx)

    for i in range(init_idx, len(sc[t[0]])):
      # print('iterate', i)
      subseq[0] = sc[t[0]][i]
      done = False

      for j in range(1, len(t)):
        if subseq[j] > subseq[j-1]:
          break

        # if the next index will fallout form s, break 
        # the process
        idx = bisect_right(sc[t[j]], subseq[j-1])
        if idx < 0 or idx >= len(sc[t[j]]):
          done = True
          break

        subseq[j] = sc[t[j]][idx]

      if done:
        break

      # if the new substring is shorter, replace it
      nxt = s[subseq[0]:subseq[-1]+1]
      # print('next:', nxt, subseq)

      if len(nxt) < len(seq_str):
        seq_str = nxt

    return seq_str


s = Solution()
t = [['abcdebdde', 'bde', 'bcde']]

for s0, t0, ans in t:
  res = s.min_win_subseq(s0, t0)
  print('Expected:', ans)
  print('Got:     ', res)
