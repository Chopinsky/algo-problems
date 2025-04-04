'''
A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

Example 1:

Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".
Example 2:

Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.
Example 3:

Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"

Constraints:

1 <= n <= 10
1 <= k <= 100
'''


class Solution:
  def __init__(self):
    n = 10
    cand = ["a", "b", "c"]
    nxt = []
    ln = 1
    self.store = [None]*11
    self.store[ln] = cand.copy()

    while ln < n:
      for w in cand:
        for ch in ("a", "b", "c"):
          if ch == w[-1]:
            continue

          nxt.append(w+ch)

      cand, nxt = nxt, cand
      cand = cand[:100]
      nxt.clear()
      ln += 1
      self.store[ln] = cand.copy()

  def getHappyString(self, n: int, k: int) -> str:
    def can_get(n: int, k: int) -> bool:
      count = 3
      n -= 1

      while n > 0:
        count *= 2
        n -= 1

      return count >= k

    if not can_get(n, k):
      return ""

    return self.store[n][k-1]

        
  def getHappyString(self, n: int, k: int) -> str:
    str_lst = []
    
    def dp(curr: str):
      if len(curr) >= n:
        str_lst.append(curr)
        return
      
      for ch in ['a', 'b', 'c']:
        if curr and curr[-1] == ch:
          continue
          
        dp(curr + ch)
        if len(str_lst) >= k:
          break
      
    dp('')
    # print(str_lst)
    
    return str_lst[k-1] if len(str_lst) >= k else ''
    