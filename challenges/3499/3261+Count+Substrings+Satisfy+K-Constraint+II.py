'''
3261. Count Substrings That Satisfy K-Constraint II

You are given a binary string s and an integer k.

You are also given a 2D integer array queries, where queries[i] = [li, ri].

A binary string satisfies the k-constraint if either of the following conditions holds:

The number of 0's in the string is at most k.
The number of 1's in the string is at most k.
Return an integer array answer, where answer[i] is the number of substrings of s[li..ri] that satisfy the k-constraint.

Example 1:

Input: s = "0001111", k = 2, queries = [[0,6]]

Output: [26]

Explanation:

For the query [0, 6], all substrings of s[0..6] = "0001111" satisfy the k-constraint except for the substrings s[0..5] = "000111" and s[0..6] = "0001111".

Example 2:

Input: s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]

Output: [15,9,3]

Explanation:

The substrings of s with a length greater than 3 do not satisfy the k-constraint.

Constraints:

1 <= s.length <= 10^5
s[i] is either '0' or '1'.
1 <= k <= s.length
1 <= queries.length <= 10^5
queries[i] == [li, ri]
0 <= li <= ri < s.length
All queries are distinct.
'''

from typing import List

class Solution:
  def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
    # sliding window to get all the ranges
    cand = []
    n = len(s)
    j = 0
    oc = 0
    zc = 0
    
    for i in range(n):
      if i > 0:
        oc -= 1 if s[i-1] == '1' else 0
        zc -= 1 if s[i-1] == '0' else 0
        
      while j < n and (oc <= k or zc <= k):
        val = s[j]
        if val == '1':
          oc += 1
        else:
          zc += 1
          
        j += 1
        
      if oc > k and zc > k:
        cand.append((i, j-1))
    
    # sort the cand
    cand.sort()
    # print(cand)
    
    # sort the queries
    q = sorted((l, r, i) for i, (l, r) in enumerate(queries))
    ans = [0]*len(q)
    
    # fenwick to add the tail position and count
    fenwick_tail = [0] * (n+1)
    fenwick_cnt = [0] * (n+1)
    
    def update(i: int):
      if i == 0:
        fenwick_tail[i] += i
        fenwick_cnt[i] += 1
        return
      
      while i < len(fenwick_tail):
        fenwick_tail[i] += i
        fenwick_cnt[i] += 1
        i += i & -i
    
    def query(i: int) -> tuple:
      s, c = fenwick_tail[0], fenwick_cnt[0]
      while i > 0:
        s += fenwick_tail[i]
        c += fenwick_cnt[i]
        i -= i & -i
      
      return s, c
      
    # add ranges while becoming available
    while q:
      l, r, idx = q.pop()
      while cand and cand[-1][0] >= l:
        _, e = cand.pop()
        update(e)
        
      # get the raw count of all subarrays in the range
      c0 = r-l+1
      cnt = c0 + c0*(c0-1)//2
      
      # remove count of subarry that don't meet the criteria
      ps1, c1 = query(r)
      ps2 = (r+1)*c1
      cnt -= ps2 - ps1
      # print('q:', (l, r), (ps1, c1), ps2, cnt)
      
      ans[idx] = cnt
    
    return ans
        