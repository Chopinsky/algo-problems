'''
You are given a string text. You should split it to k substrings (subtext1, subtext2, ..., subtextk) such that:

subtexti is a non-empty string.
The concatenation of all the substrings is equal to text (i.e., subtext1 + subtext2 + ... + subtextk == text).
subtexti == subtextk - i + 1 for all valid values of i (i.e., 1 <= i <= k).
Return the largest possible value of k.

Example 1:

Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
Example 2:

Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".
Example 3:

Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
Example 4:

Input: text = "aaa"
Output: 3
Explanation: We can split the string on "(a)(a)(a)".

Constraints:

1 <= text.length <= 1000
text consists only of lowercase English characters.
'''


from typing import defaultdict
from bisect import bisect_left


class Solution:
  # greedy, ye solution
  def longestDecomposition(self, text: str) -> int:
    n = len(text)
    i, ii = 0, 0
    j, jj = n-1, n-1
    count = 0
    
    while i < j:
      if text[ii:i+1] == text[j:jj+1]:
        ii, jj = i+1, j-1
        count += 2
        
      # extend the comparison range
      i += 1
      j -= 1
      
    return count + (1 if (ii <= jj) else 0)
      
    
  def longestDecomposition0(self, text: str) -> int:
    n = len(text)
    oa = ord('a')
    pos = [[] for _ in range(26)]
    hash_dict = [defaultdict(int) for _ in range(n)]
    mod = 1_000_000_007
    
    for i, ch in enumerate(text):
      pos[ord(ch) - oa].append(i)
      curr_hash = (ord(ch) - oa)
      
      for j in range(i+1, n):
        curr_hash = (curr_hash * 26 + ord(text[j]) - oa) % mod
        hash_dict[i][j] = curr_hash

    start, end = 0, n
    count = 0
    
    while start < end:
      if start+1 == end:
        count += 1
        break
        
      ch = ord(text[start]) - oa
      idx, jdx = bisect_left(pos[ch], start), bisect_left(pos[ch], end)-1
      if idx >= jdx:
        count += 1
        break
        
      i, j = pos[ch][idx], pos[ch][jdx]
      ln = end - j
      found = False
      # print('start', start, end, text[start:end], pos[ch], i, j, ln)
      
      while i+ln <= j:
        if hash_dict[i][i+ln-1] == hash_dict[j][end-1] and text[i:i+ln] == text[j:end]:
          found = True
          count += 2
          start = i+ln
          end = j
          break
          
        jdx -= 1
        j = pos[ch][jdx]
        ln = end-j
      
      # print('finish', start, end, ln, n, found)
      if not found:
        count += 1
        break
    
    return count
  