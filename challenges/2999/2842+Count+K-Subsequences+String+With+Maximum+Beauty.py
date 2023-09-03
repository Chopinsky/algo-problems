'''
2842. Count K-Subsequences of a String With Maximum Beauty

You are given a string s and an integer k.

A k-subsequence is a subsequence of s, having length k, and all its characters are unique, i.e., every character occurs once.

Let f(c) denote the number of times the character c occurs in s.

The beauty of a k-subsequence is the sum of f(c) for every character c in the k-subsequence.

For example, consider s = "abbbdd" and k = 2:

f('a') = 1, f('b') = 3, f('d') = 2
Some k-subsequences of s are:
"abbbdd" -> "ab" having a beauty of f('a') + f('b') = 4
"abbbdd" -> "ad" having a beauty of f('a') + f('d') = 3
"abbbdd" -> "bd" having a beauty of f('b') + f('d') = 5
Return an integer denoting the number of k-subsequences whose beauty is the maximum among all k-subsequences. Since the answer may be too large, return it modulo 109 + 7.

A subsequence of a string is a new string formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.

Notes

f(c) is the number of times a character c occurs in s, not a k-subsequence.
Two k-subsequences are considered different if one is formed by an index that is not present in the other. So, two k-subsequences may form the same string.

Example 1:

Input: s = "bcca", k = 2
Output: 4
Explanation: From s we have f('a') = 1, f('b') = 1, and f('c') = 2.
The k-subsequences of s are: 
bcca having a beauty of f('b') + f('c') = 3 
bcca having a beauty of f('b') + f('c') = 3 
bcca having a beauty of f('b') + f('a') = 2 
bcca having a beauty of f('c') + f('a') = 3
bcca having a beauty of f('c') + f('a') = 3 
There are 4 k-subsequences that have the maximum beauty, 3. 
Hence, the answer is 4. 
Example 2:

Input: s = "abbcd", k = 4
Output: 2
Explanation: From s we have f('a') = 1, f('b') = 2, f('c') = 1, and f('d') = 1. 
The k-subsequences of s are: 
abbcd having a beauty of f('a') + f('b') + f('c') + f('d') = 5
abbcd having a beauty of f('a') + f('b') + f('c') + f('d') = 5 
There are 2 k-subsequences that have the maximum beauty, 5. 
Hence, the answer is 2. 

Constraints:

1 <= s.length <= 2 * 10^5
1 <= k <= s.length
s consists only of lowercase English letters.
'''

from collections import Counter
from functools import lru_cache


class Solution:
  def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
    f = Counter(s)
    if k > len(f):
      return 0
    
    if k == len(s):
      return 1 if k == len(f) else 0
    
    arr = sorted(f.values(), reverse=True)
    s0 = sum(arr[:k])
    n = len(arr)
    mod = 10**9 + 7
    # print(f, arr, s0)
    
    suffix = [val for val in arr]
    for i in range(n-2, -1, -1):
      suffix[i] += suffix[i+1]
    
    @lru_cache(None)
    def dp(i: int, r: int, s: int) -> int:
      # end 1: all unique chars searched
      if i >= n:
        return 0 if r > 0 or s > 0 else 1
      
      # end 2: no more chars to fill the subseq
      if r == 0:
        return 0 if s > 0 else 1
      
      # not enough unique chars left to fill the subseq
      if n-i < r:
        return 0
      
      max_rem = suffix[i] - (0 if n-i >= r else suffix[i+r])
      
      # if use this ch
      c0 = (arr[i] * dp(i+1, r-1, s-arr[i])) % mod
      
      # if don't use this ch
      c1 = dp(i+1, r, s)
      
      return (c0 + c1) % mod
      
    return dp(0, k, s0)
        