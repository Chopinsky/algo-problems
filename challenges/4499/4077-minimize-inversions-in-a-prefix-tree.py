'''
4077-minimize-inversions-in-a-prefix-tree
'''


class Solution:
  def minInversions(self, words: list[str], target: list[int]) -> int:
    mem = {}
    INF = float('inf')

    def solve(words: tuple[str]) -> int:
      if not words:
        return 0

      if words in mem:
        return mem[words]

      ans = INF

      # iterate all choices of the starting idx
      for ch in set(w[0] for w in words):
        inv = 0
        p1: list[str] = []
        p2: list[str] = []

        for w in words:
          if w[0] == ch:
            rest = w[1:]
            if rest:
              # iterate this subtree
              p1.append(rest)
            else:
              # reaching end state
              inv += len(p1)

            # add the inversions from the other subtree
            inv += len(p2)

          else:
            p2.append(w)

        ans = min(
          ans,
          inv + solve(tuple(p1)) + solve(tuple(p2))
        )
        
      mem[words] = ans
      return ans

    n = len(words)
    tmp = [""] * n
    pos = [0] * n

    for i in range(n):
      pos[target[i]] = i

    for i in range(n):
      tmp[pos[i]] = words[i]

    # print('init:', tmp)
    return solve(tuple(tmp))
    