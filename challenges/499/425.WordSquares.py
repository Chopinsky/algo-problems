'''
Given a set of words (without duplicates), find all word squares 
you can build from them.

A sequence of words forms a valid word square if the kth row and 
column read the exact same string, where 0 ≤ k < max(numRows, 
numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms 
a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y

Note:

There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not 
matter (just the order of words in each word square matters).

Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "b a b a",
    "a b a t",
    "b a b a",
    "a t a l"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not 
matter (just the order of words in each word square matters).
'''


from typing import List
from collections import defaultdict


class Solution:
  def word_squares(self, words: List[str]) -> List[List[str]]:
    n = len(words)
    if n == 1:
      return [words[0]] if len(words[0]) == 1 else []

    ans = []
    prefix = defaultdict(set)
    wl = len(words[0])

    for i, w in enumerate(words):
      for j in range(1, wl+1):
        prefix[w[:j]].add(i)

    # print(prefix)
    w = []
    ans = []
    cache = {}

    def build():
      nxt = ''
      key = ''
      idx = len(w)

      if idx >= wl:
        res = w.copy()
        ans.append(res)
        return res

      for i, word in enumerate(w):
        nxt += word[idx]
        key += word[i+1:] + ','

      if nxt not in prefix:
        return None

      if key in cache:
        for arr in cache[key]:
          ans.append(w.copy() + arr)

        return cache[key]

      sub = []
      for i in prefix[nxt]:
        w.append(words[i])
        res = build()
        if res:
          sub.append(res)

        w.pop()

      return sub

    for i in range(n):
      w.clear()
      w.append(words[i])
      build()

    return ans

s = Solution()
t = [
  ["area","lead","wall","lady","ball"],
  ["abat","baba","atan","atal"]
]

for test_case in t:
  output = s.word_squares(test_case)
  print("test:", test_case)
  print("output", output)
