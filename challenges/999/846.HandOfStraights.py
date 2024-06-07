'''
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

Constraints:

1 <= hand.length <= 10^4
0 <= hand[i] <= 10^9
1 <= groupSize <= hand.length
'''

from collections import Counter
from typing import List

class Solution:
  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    n = len(hand)
    if n % groupSize != 0:
      return False
    
    c = Counter(hand)
    cand = sorted(c, reverse=True)
    
    while cand:
      num = cand.pop()
      cnt = c[num]
      if cnt == 0:
        continue
        
      for offset in range(groupSize):
        curr = num+offset
        if curr not in c or c[curr] < cnt:
          return False
        
        c[curr] -= cnt
      
    return True
    
  def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    count = Counter(hand)
    nums = sorted(set(hand))
    
    for n in nums:
      if not count[n]:
        continue
        
      base = count[n]
      
      for n0 in range(n, n+groupSize):
        if n0 not in count or count[n0] < base:
          return False
        
        count[n0] -= base
    
    # print(count, nums)
    
    return True
    