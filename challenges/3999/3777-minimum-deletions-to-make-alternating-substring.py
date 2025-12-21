'''
3777-minimum-deletions-to-make-alternating-substring
'''

from typing import List 


class Solution:
  def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
    n = len(s)
    tree = [0]*(n+1)

    def update(i: int, delta: int):
      if i == 0:
        tree[0] += delta
        return

      while i < len(tree):
        tree[i] += delta
        i += i & (-i)

    def query(i: int):
      s = tree[0]

      while i > 0:
        s += tree[i]
        i -= i & (-i)

      return s

    arr = [1 if c == 'B' else 0 for c in s]
    for i in range(1, n):
      # add incorrect pair
      if arr[i] == arr[i-1]:
        update(i, 1)

    ans = []

    for q in queries:
      if q[0] == 1:
        i = q[1]
        arr[i] = 1 - arr[i]

        # update incorrect pairs for the left and right
        if i > 0:
          update(i, 1 if arr[i] == arr[i-1] else -1)

        if i < n-1:
          update(i+1, 1 if arr[i+1] == arr[i] else -1)

        continue

      ans.append(query(q[2]) - query(q[1]))

    return ans

        