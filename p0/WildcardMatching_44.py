import re

'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:

Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:

Input: s = "acdcb", p = "a*c?b"
Output: false

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
'''

class Solution44:
  def test(self):
    print("Testing problem 8:")

    tests = [
      ("abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb", "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb", False),
      ("leetcode", "*e*t?d*", False),
    ]

    for (a, b, c) in tests:
      assert self.isMatch(a, b) == c, "Failed: " + a + ", " + b

    print("All passed")

  '''
  The idea is that in the case of a mis-match, we trace back to
  the last wildcard pattern location, and advance the substring
  by 1, such that we will match against a "new" substring after
  the last wildcard.
  '''
  def isMatch(self, s: str, p: str) -> bool:
    ps, pp = 0, 0
    ls, lp = len(s), len(p)
    str_start = 0
    last_wc_pos = -1

    while ps < ls:
      # matching a char or the single wildcard, advance both pointers
      if pp < lp and (p[pp] == '?' or p[pp] == s[ps]):
        ps += 1
        pp += 1
        continue

      # matching random lengh wildcard, remember the position which we
      # will trace back to for future mis-matches
      if pp < lp and p[pp] == '*':
        str_start = ps     # the beginning of the post-wc-substring
        last_wc_pos = pp   # rememebr where the '*' is, and we will restart from its next pattern char
        pp += 1
        continue

      # not a match, trace back to the last '*' state and advance source
      # string's `ps` by 1 (i.e. excluding the first char from the
      # current iter and try again)
      if last_wc_pos >= 0:
        str_start += 1
        ps = str_start
        pp = last_wc_pos+1
        continue

      # can't match and no more '*' to trace back with
      return False

    # check if we can ignore the rest of the patterns (i.e. all '*' wildcards)
    # otherwise, there are tail patterns that don't get matched, and the regex
    # returns false
    while pp < lp and p[pp] == '*':
      pp += 1

    return pp == lp


  def isMatch1(self, s: str, p: str) -> bool:
    if p == '*':
      return True

    rp = re.split(r"(\?|\*)", p)
    raw = [val for val in rp if val != '']
    seg = []

    for pat in raw:
      if len(seg) > 0 and seg[-1] == '*' and pat == '*':
        continue

      if pat != '?' and pat != '*' and s.find(pat) < 0:
        return False

      seg.append(pat)

    si, pi = 0, 0
    ls, lp = len(s), len(seg)
    last_wc = None

    # print(seg)

    while si < ls:
      # print(pi, si, pat)
      if pi >= lp:
        if not last_wc:
          return False

        pi = last_wc[0]
        si = last_wc[1]
        last_wc[1] += 1

      pat = seg[pi]
      lc = len(pat)

      if pat == '*':
        if pi == lp-1:
          return True

        last_wc = [pi+1, si+1]
        pi += 1
        continue

      if pat == '?':
        if pi == lp-1 and si == ls-1:
          return True

        si += 1
        pi += 1
        continue

      if ls-si < lc or s[si:si+lc] != pat:
        if not last_wc:
          return False

        pi = last_wc[0]
        si = last_wc[1]
        last_wc[1] += 1
        continue

      pi += 1
      si += lc

    while pi < lp and seg[pi] == '*':
      pi += 1

    # print("all done", si, pi)
    return pi == lp
