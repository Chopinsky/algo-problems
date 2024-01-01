'''
2983. Palindrome Rearrangement Queries

You are given a 0-indexed string s having an even length n.

You are also given a 0-indexed 2D integer array, queries, where queries[i] = [ai, bi, ci, di].

For each query i, you are allowed to perform the following operations:

Rearrange the characters within the substring s[ai:bi], where 0 <= ai <= bi < n / 2.
Rearrange the characters within the substring s[ci:di], where n / 2 <= ci <= di < n.
For each query, your task is to determine whether it is possible to make s a palindrome by performing the operations.

Each query is answered independently of the others.

Return a 0-indexed array answer, where answer[i] == true if it is possible to make s a palindrome by performing operations specified by the ith query, and false otherwise.

A substring is a contiguous sequence of characters within a string.
s[x:y] represents the substring consisting of characters from the index x to index y in s, both inclusive.
 

Example 1:

Input: s = "abcabc", queries = [[1,1,3,5],[0,2,5,5]]
Output: [true,true]
Explanation: In this example, there are two queries:
In the first query:
- a0 = 1, b0 = 1, c0 = 3, d0 = 5.
- So, you are allowed to rearrange s[1:1] => abcabc and s[3:5] => abcabc.
- To make s a palindrome, s[3:5] can be rearranged to become => abccba.
- Now, s is a palindrome. So, answer[0] = true.
In the second query:
- a1 = 0, b1 = 2, c1 = 5, d1 = 5.
- So, you are allowed to rearrange s[0:2] => abcabc and s[5:5] => abcabc.
- To make s a palindrome, s[0:2] can be rearranged to become => cbaabc.
- Now, s is a palindrome. So, answer[1] = true.
Example 2:

Input: s = "abbcdecbba", queries = [[0,2,7,9]]
Output: [false]
Explanation: In this example, there is only one query.
a0 = 0, b0 = 2, c0 = 7, d0 = 9.
So, you are allowed to rearrange s[0:2] => abbcdecbba and s[7:9] => abbcdecbba.
It is not possible to make s a palindrome by rearranging these substrings because s[3:6] is not a palindrome.
So, answer[0] = false.
Example 3:

Input: s = "acbcab", queries = [[1,2,4,5]]
Output: [true]
Explanation: In this example, there is only one query.
a0 = 1, b0 = 2, c0 = 4, d0 = 5.
So, you are allowed to rearrange s[1:2] => acbcab and s[4:5] => acbcab.
To make s a palindrome s[1:2] can be rearranged to become abccab.
Then, s[4:5] can be rearranged to become abccba.
Now, s is a palindrome. So, answer[0] = true.

Constraints:

2 <= n == s.length <= 10^5
1 <= queries.length <= 10^5
queries[i].length == 4
ai == queries[i][0], bi == queries[i][1]
ci == queries[i][2], di == queries[i][3]
0 <= ai <= bi < n / 2
n / 2 <= ci <= di < n
n is even.
s consists of only lowercase English letters.

*** test cases:

"abcabc"
[[1,1,3,5],[0,2,5,5]]
"abbcdecbba"
[[0,2,7,9]]
"acbcab"
[[1,2,4,5]]
"fxdqcfqdxc"
[[1,1,7,8],[1,1,5,9],[2,4,8,8],[0,4,6,8],[2,3,7,8],[2,4,5,9],[1,4,9,9]]
'''

from typing import List
from bisect import bisect_left


class Solution:
  def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    n = len(s)
    left_end = n//2 - 1
    
    prefix = []
    curr = [0]*26
    for i in range(n):
      idx = ord(s[i]) - ord('a')
      curr[idx] += 1
      prefix.append(curr.copy())
      
    matches = []
    i, j = 0, n-1
    while i < j:
      if s[i] == s[j]:
        matches.append(i)
        
      i += 1
      j -= 1
    
    # print(prefix)
    # print(matches)
    
    def query(l, r):
      # print('query:', (l, r))
      
      if l > r:
        return [0]*26
      
      if l == 0:
        return prefix[r].copy()
      
      res = prefix[r].copy()
      for i in range(26):
        res[i] -= prefix[l-1][i]
        
      return res
    
    def check(a1, a2):
      for i in range(26):
        if a1[i] != a2[i]:
          return False
        
      return True
      
    def check_unchangables(l, r):
      if l > r:
        return True
      
      idx = bisect_left(matches, l)
      if idx >= len(matches) or matches[idx] != l:
        return False

      # check if all indices are in the matching group
      jdx = idx + (r - l)
      
      return jdx < len(matches) and matches[jdx] == r
      
    def to_left(l, r):
      ln = r-l
      l0 = n-1-r
      r0 = l0+ln
      
      return l0, r0
      
    def to_right(l, r):
      ln = r-l
      r0 = n-1-l
      l0 = r0-ln
      
      return l0, r0
      
    def test_no_overlap(l0, r0, l1, r1):
      # print('** no overlap', (l0, r0), (l1, r1))
      
      l2, r2 = to_right(l0, r0)
      if not check(query(l0, r0), query(l2, r2)):
        return False
      
      l3, r3 = to_left(l1, r1)
      if not check(query(l3, r3), query(l1, r1)):
        return False
      
      if l3 < l0:
        l0, r0, l3, r3 = l3, r3, l0, r0
        
      return check_unchangables(0, l0-1) and check_unchangables(r0+1, l3-1) and check_unchangables(r3+1, left_end)
      
    def test_cover(l0, r0, l1, r1):
      # print('** full overlap', (l0, r0), (l1, r1))
      
      l3, r3 = to_left(l1, r1)
      if l3 <= l0 and r3 >= r0:
        l0, r0 = l3, r3
        
      l1, r1 = to_right(l0, r0)
      a0 = query(l0, r0)
      a1 = query(l1, r1)
      
      if not check(a0, a1):
        return False
      
      return check_unchangables(0, l0-1) and check_unchangables(r0+1, left_end)
    
    def test_overlap(l0, r0, l1, r1):
      # print('** overlap', (l0, r0), (l1, r1))
      l2, r2 = to_right(l0, r0)
      l3, r3 = to_left(l1, r1)
      
      a0 = query(l0, r0)
      a3 = query(l1, r1)

      # subcase-1: left has the front
      if l0 <= l3:
        a1 = query(r1+1, r2)
        a2 = query(r0+1, r3)

      # subcase-2: right has the front
      else:
        a1 = query(l2, l1-1)
        a2 = query(l3, l0-1)

      # print('a0', (l0, r0), a0)
      # print('a1', (l2, l1-1), a1)
      # print('a2', (l3, l0-1), a2)
      # print('a3', (l1, r1), a3)
      
      for i in range(26):
        if a0[i] < a1[i] or a3[i] < a2[i]:
          return False
        
        a0[i] -= a1[i]
        a3[i] -= a2[i]

      # final: check the overlapped part 
      # print('final:', a0, a3)
      for i in range(26):
        if a0[i] != a3[i]:
          return False

      return check_unchangables(0, min(l0, l3)-1) and check_unchangables(max(r0, r3)+1, left_end)
    
    ans = []
    for l0, r0, l1, r1 in queries:
      l3, r3 = to_left(l1, r1)
      # print('=='*10)
      # print((l0, r0), '->', to_right(l0, r0))
      # print((l3, r3), '<-', (l1, r1))
      
      # case 1: no overlaps
      if l3 > r0 or r3 < l0:
        ans.append(test_no_overlap(l0, r0, l1, r1))
        continue
        
      # case 2: one interval inside the over
      if (l3 <= l0 and r3 >= r0) or l3 >= l0 and r3 <= r0:
        ans.append(test_cover(l0, r0, l1, r1))
        continue
      
      # case 3: partial overlapping
      ans.append(test_overlap(l0, r0, l1, r1))
      
    return ans
        