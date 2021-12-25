'''
We are given n different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

Example 1:

Input: stickers = ["with","example","science"], target = "thehat"
Output: 3
Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.

Example 2:

Input: stickers = ["notice","possible"], target = "basicbasic"
Output: -1
Explanation:
We cannot form the target "basicbasic" from cutting letters from the given stickers.

Constraints:

n == stickers.length
1 <= n <= 50
1 <= stickers[i].length <= 10
1 <= target <= 15
stickers[i] and target consist of lowercase English letters.
'''


import math
from typing import List, Dict
from collections import Counter, defaultdict


class Solution:
  def minStickers(self, stickers: List[str], target: str) -> int:
    s_chars = set()
    s_counters = []
    t_counter = Counter(target)
    t_chars = set(t_counter.keys())
    
    for s in stickers:
      sc = defaultdict(int)
      for ch in s:
        if ch in t_chars:
          sc[ch] += 1
          s_chars.add(ch)
      
      s_counters.append(sc)
  
    for t in t_chars:
      if t not in s_chars:
        return -1
  
    s_counters.sort(key=lambda x: len(x), reverse=True)
    counter = []
    
    def contains(src, tgt) -> bool:
      for ch in tgt:
        if ch not in src or src[ch] < tgt[ch]:
          return False
          
      return True
    
    def unique_chars(src) -> int:
      res = 0
      for ch in src.keys():
        res |= 1 << (ord(ch) - ord('a'))
        
      return res
    
    for curr in s_counters:
      # this sticker will do the job
      if contains(curr, t_counter):
        return 1
      
      if not s:
        counter.append(curr)
        continue
        
      found = False
      for prev in counter:            
        found |= contains(prev, curr)
        if found:
          break
            
      if not found:
        counter.append(curr)
      
    # print(t_counter, counter)
    n = len(counter)
    suffix = [0] * n
    
    for i in range(n-1, -1, -1):
      if i == n-1:
        suffix[i] = unique_chars(counter[i])
      else:
        suffix[i] = suffix[i+1] | unique_chars(counter[i])
        
      # print('suffix @', i, '{:026b}'.format(suffix[i]))
    best_hand = math.inf
    
    def search(i: int, count: int, req: int, hand: Dict[str, int]) -> int:
      nonlocal best_hand
      if i >= n or req & suffix[i] != req:
        return 
      
      upper = 0
      for ch, amnt in counter[i].items():
        if hand[ch] < t_counter[ch]:
          u = (t_counter[ch] - hand[ch]) // amnt
          if (t_counter[ch] - hand[ch]) % amnt != 0:
            u += 1
            
          upper = max(upper, u)
      
      # print(i, upper, counter[i])
      # none is needed from this sticker
      if upper <= 0:
        search(i+1, count, req, hand)
        return
      
      for j in range(upper+1):
        if count+j >= best_hand:
          break
          
        nxt_hand = hand.copy()
        nxt_req = req
        
        for ch, amnt in counter[i].items():
          nxt_hand[ch] += j*amnt
          idx = 1 << (ord(ch) - ord('a'))
          if nxt_hand[ch] >= t_counter[ch] and nxt_req & idx > 0:
            nxt_req ^= idx
            
        # print('amnt:', i, j, format(nxt_req, '0>12b'))
        if nxt_req == 0:
          best_hand = min(best_hand, count+j)
          break
          
        search(i+1, count+j, nxt_req, nxt_hand)
    
    search(0, 0, unique_chars(t_counter), defaultdict(int))
    
    return best_hand if best_hand < math.inf else -1
  