'''
2260. Minimum Consecutive Cards to Pick Up

You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.

Constraints:

1 <= cards.length <= 10^5
0 <= cards[i] <= 10^6
'''

from typing import List

class Solution:
  def minimumCardPickup(self, cards: List[int]) -> int:
    n = len(cards)
    min_count = float('inf')
    i, j = 0, 0
    seen = set()
    
    while j < n:
      # print('iter:', (i, j), cards[i:j])
      while j < n and cards[j] not in seen:
        seen.add(cards[j])
        j += 1
        
      if j < n:
        min_count = min(min_count, j-i+1)
      
      i += 1
      seen.discard(cards[i-1])
    
    return min_count if min_count < float('inf') else -1
  