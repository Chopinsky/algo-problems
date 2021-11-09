from typing import List


class Solution:
  '''
  idea is that for a player, he/she is at an unknown position, but
  is taking the first i stones as his/her round's score (i.e. more
  than i stones on board before the action), then the alt-player
  will act optimally, and take a `diff`, which is max(dp(i+1), 
  dp(i+2), ..., dp(n)), and the optimal `diff` for the current play
  is `sum(stones[:i]) - max(dp(i+1), dp(i+2), ..., dp(n))`, and
  we only update the `max(...)` part becomes dp(i) = sum(...) - 
  max(i+1...), and max(i...) = max(dp(i), max(i+1...)).
  '''
  def stoneGameVIII(self, stones: List[int]) -> int:
    n = len(stones)
    if n <= 2:
      return sum(stones)
    
    presum = [val for val in stones]
    for i in range(1, n):
      presum[i] += presum[i-1]
      
    # the final state of the game -- only 1 stone left
    diff = presum[-1]
    
    # the curr player can have the score of presum[i-1], and minus the 
    # best score diff the next player can get, which is dp, is the best
    # score the curr player can obtain
    for i in range(n-1, 1, -1):
      diff = max(diff, presum[i-1] - diff)
      
    return diff

  def stone_game_vii0(self, stones: List[int]) -> int:
    def calc(stones: List[int], start: int) -> int:
      ln = len(stones)
      if ln <= 2:
        return sum(stones)

      s = stones[0]
      best = None

      for i in range(1, ln):
        s += stones[i]
        score = s - calc([s] + stones[i+1:], i) if i < ln-1 else s
        best = s if i == 1 else max(best, score)

      return best

    return calc(stones, 0)


s = Solution()
t = [
  [[-1, 2, -3, 4, -5], 5],
  [[7, -6, 5, 10, 5, -2, -6], 13],
  [[-10, -12], -22],
]

for test in t:
  res = s.stone_game_vii(test[0])
  print("Expected:", test[1], "- Get:", res)
