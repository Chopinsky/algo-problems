'''
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
Example 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

Constraints:

1 <= envelopes.length <= 10^5
envelopes[i].length == 2
1 <= wi, hi <= 10^5
'''

from typing import List
from bisect import bisect_left, bisect_right


class Solution:
  def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    envelopes.sort(key=lambda x:(x[0],-x[1]))

    def lis(src: List[int]):
      dp = []
      for height in src:
        idx = bisect_left(dp, height)
        if idx == len(dp):
          dp.append(height)
        else:
          dp[idx] = height

      return len(dp)

    return lis([x[1] for x in envelopes])
  
  
  def maxEnvelopes0(self, env: List[List[int]]) -> int:
    env.sort(key=lambda x: (x[0], -x[1]))
    n = len(env)
    h_vals = []
    h_cnt = []
    last_w = -1
    last_h = []
    last_cnt = []
    long = 1
    
    for i in range(n):
      w, h = env[i]
      # print('=================>', i)
      # print(w, h)
      
      # update previous envelop heights and positions
      if w > last_w:
        for j in range(len(last_h)):
          if not h_vals or last_h[j] > h_vals[-1]:
            h_vals.append(last_h[j])
            h_cnt.append(max(1+h_cnt[-1] if h_cnt else 0, last_cnt[j]))
            continue
            
          k = bisect_left(h_vals, last_h[j])
          if k >= 0:
            #todo: merge
            if h_vals[k] == last_h[j]:
              h_cnt[k] = max(h_cnt[k], last_cnt[j])
            else:
              h_vals[k] = last_h[j]
              h_cnt[k] = last_cnt[j]
            
        last_w = w
        last_h.clear()
        last_cnt.clear()
        
      cnt = 1
      j = bisect_right(h_vals, h-1) - 1
      # print(h_vals, h_cnt, j)
      
      if 0 <= j < len(h_vals):
        cnt = max(cnt, 1+h_cnt[j])
    
      last_h.append(h)
      last_cnt.append(cnt)
      long = max(long, cnt)
      # print(last_h, last_cnt, cnt)
      
    return long
    