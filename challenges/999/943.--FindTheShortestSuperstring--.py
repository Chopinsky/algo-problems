from itertools import permutations
from collections import defaultdict
from typing import List

'''
Given an array of strings words, return the smallest string that contains each string in words as a substring. If there are multiple valid strings of the smallest length, return any of them.

You may assume that no string in words is a substring of another string in words.

Example 1:

Input: words = ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.

Example 2:

Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"

Constraints:

1 <= words.length <= 12
1 <= words[i].length <= 20
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''

class Solution:
  '''
  The idea is that we only care what's the last word in a word series, since
  it will affect the length of the next word to be added. So the `dp`
  states can be expressed as `dp[mask][i]`, where `mask` represents the index of
  all the words in the series, and `i` as the last word to be used in this
  series.

  Then the state transition is:
    dp[mask][i] = min(dp[mask][i], dp[prev_mask][j] + overlap[j][i])

  where `mask == prev_mask | (1<<i)`, and overlap[j][i] represents
  the length to be added to the series if we append `words[i]` to the series
  which was ended with `words[j]`

  In addition, we also record the parent (the last word to be added),
  such that we can reconstruct the series from the `dp`
  '''

  def shortestSuperstring(self, words: List[str]) -> str:
    dic = defaultdict(list)
    n = len(words)
    ans = ""

    for (i, w) in enumerate(words):
      ans += w
      for j in range(1, len(w)):
        dic[w[:j]].append(i)

    pairs = [[0] * n for _ in range(n)]
    found = False

    for i, w in enumerate(words):
      for j in range(1, len(w)):
        l = len(w)-j
        for k in dic[w[j:]]:
          pairs[i][k] = max(pairs[i][k], l)
          found = True

    # no overlaps found
    if not found:
      return ans

    ''' slow brutal force solution
    for p in permutations([i for i in range(n)]):
      l0 = len(words[p[0]])
      for j in range(1, n):
        curr, last = p[j], p[j-1]
        if last in pairs and curr in pairs[last]:
          l0 += pairs[last][curr]
        else:
          l0 += len(words[curr])

      # print(p, l0)

      if l0 < len(ans):
        s = ""
        for j in range(n):
          if j == 0:
            s += words[p[0]]
          else:
            curr, last = p[j], p[j-1]
            if last in pairs and curr in pairs[last]:
              s += words[curr][-pairs[last][curr]:]
            else:
              s += words[curr]

        ans = s
    '''

    h = 1 << n
    # dp states, where dp[mask][i] = [min-length, parent-index-to-get-min-length]
    dp = [[[0, -1] for _ in range(n)] for _ in range(h)]

    for mask in range(1, h):
      for i in range(n):
        # this word hasn't been present in this mask
        if mask & (1<<i) == 0:
          continue

        prev = mask ^ (1<<i)
        l = len(words[i])

        # first word in the series
        if prev == 0:
          dp[mask][i][0] = l
          continue

        for j in range(n):
          # j not in the previous mask
          if prev & (1<<j) == 0:
            continue

          base = dp[prev][j][0] + (l - pairs[j][i])

          if dp[mask][i][0] == 0 or base < dp[mask][i][0]:
            dp[mask][i][0] = base
            dp[mask][i][1] = j

    # get the best string length
    last = -1
    for i, cell in enumerate(dp[h-1]):
      if last < 0 or cell[0] < dp[h-1][last][0]:
        last = i

    ans = words[last]
    parent = dp[mask][last][1]
    mask = h-1

    while parent >= 0:
      # get the overlap and the parent word to add
      prefix = pairs[parent][last]
      src = words[parent]

      # add prefix string to the answer
      ans = src[:len(src)-prefix] + ans

      # remove the word's index after added
      mask ^= (1<<last)

      # reset the current / parent index
      last, parent = parent, dp[mask][last][1]

    return ans
