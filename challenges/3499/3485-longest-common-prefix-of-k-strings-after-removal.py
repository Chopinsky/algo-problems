'''
3485-longest-common-prefix-of-k-strings-after-removal/
'''

from typing import List


class Node:
  def __init__(self):
    self.children = [None]*26
    self.count = 0
    self.prefix_len = -1

class Solution:
  def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
    n = len(words)
    if n-1 < k:
      return [0]*n

    root = Node()
    result = []

    def update_trie(w: str, delta: int, k: int):
      ln = len(w)
      path = [None]*(ln+1)
      path[0] = root
      
      for i in range(ln):
        ldx = ord(w[i]) - ord('a')
        if not path[i].children[ldx]:
          path[i].children[ldx] = Node()

        path[i+1] = path[i].children[ldx]

      for node in path:
        node.count += delta

      for i in range(ln, -1, -1):
        curr = path[i]
        cand = i if curr.count >= k else -1
        for node in curr.children:
          if not node:
            continue

          cand = max(cand, node.prefix_len)

        curr.prefix_len = cand

    for w in words:
      update_trie(w, 1, k)

    for w in words:
      update_trie(w, -1, k)
      result.append(root.prefix_len)
      update_trie(w, 1, k)

    return result

