'''
2564. Substring XOR Queries

You are given a binary string s, and a 2D integer array queries where queries[i] = [firsti, secondi].

For the ith query, find the shortest substring of s whose decimal value, val, yields secondi when bitwise XORed with firsti. In other words, val ^ firsti == secondi.

The answer to the ith query is the endpoints (0-indexed) of the substring [lefti, righti] or [-1, -1] if no such substring exists. If there are multiple answers, choose the one with the minimum lefti.

Return an array ans where ans[i] = [lefti, righti] is the answer to the ith query.

A substring is a contiguous non-empty sequence of characters within a string.

Example 1:

Input: s = "101101", queries = [[0,5],[1,2]]
Output: [[0,2],[2,3]]
Explanation: For the first query the substring in range [0,2] is "101" which has a decimal value of 5, and 5 ^ 0 = 5, hence the answer to the first query is [0,2]. In the second query, the substring in range [2,3] is "11", and has a decimal value of 3, and 3 ^ 1 = 2. So, [2,3] is returned for the second query. 

Example 2:

Input: s = "0101", queries = [[12,8]]
Output: [[-1,-1]]
Explanation: In this example there is no substring that answers the query, hence [-1,-1] is returned.
Example 3:

Input: s = "1", queries = [[4,5]]
Output: [[0,0]]
Explanation: For this example, the substring in range [0,0] has a decimal value of 1, and 1 ^ 4 = 5. So, the answer is [0,0].

Constraints:

1 <= s.length <= 10^4
s[i] is either '0' or '1'.
1 <= queries.length <= 10^5
0 <= firsti, secondi <= 10^9
'''

from functools import lru_cache
from typing import List
from collections import defaultdict


class Solution:
  def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
    res = [[-1, -1]] * len(queries)
    q = defaultdict(list)
    size = set()
    n = len(s)
    
    @lru_cache(None)
    def to_str(val: int) -> str:
      if val == 0:
        return '0'
      
      s = ''
      while val > 0:
        if val & 1 == 1:
          s = '1' + s
        else:
          s = '0' + s
          
        val >>= 1
      
      return s
      
    for i, [a, b] in enumerate(queries):
      val = to_str(a^b)
      q[val].append(i)
      size.add(len(val))
      
    for ln in sorted(size):
      # print('check:', ln)
      
      for idx in range(n-ln+1):
        base = s[idx:idx+ln]
        if base in q:
          for j in q[base]:
            if res[j][0] < 0:
              res[j] = [idx, idx+ln-1]
          
          del q[base]
      
    return res
    