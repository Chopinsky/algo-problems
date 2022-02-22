'''
We define the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this:

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
Given a string p, return the number of unique non-empty substrings of p are present in s.

Example 1:

Input: p = "a"
Output: 1
Explanation: Only the substring "a" of p is in s.
Example 2:

Input: p = "cac"
Output: 2
Explanation: There are two substrings ("a", "c") of p in s.
Example 3:

Input: p = "zab"
Output: 6
Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of p in s.
 

Constraints:

1 <= p.length <= 10^5
p consists of lowercase English letters.
'''


from collections import defaultdict


class Solution:
  def findSubstringInWraproundString(self, p: str) -> int:
    d = defaultdict(int)
    prev, count = 0, 0
        
    for i, c in enumerate(p):
      idx = ord(c) - ord('a')
      count = count + 1 if i and (prev + 1) % 26 == idx else 1
      prev = idx
      d[c] = max(d[c], count)
      
    return sum(d.values())
    
    
  def findSubstringInWraproundString0(self, p: str) -> int:
    count = [0] * 26
    start = 0
    
    for i, ch in enumerate(p):
      idx = ord(ch) - ord('a')
      if i == 0:
        count[idx] += 1
        continue
        
      if (p[i-1] == 'z' and ch == 'a') or (ord(ch) - ord(p[i-1]) == 1):
        for j in range(start, i+1):
          # a round updates
          if j != start and p[j] == p[start]:
            break
            
          jdx = ord(p[j]) - ord('a')
          count[jdx] = max(count[jdx], i-j+1)
          
      else:
        count[idx] = max(count[idx], 1)
        start = i
        
    return sum(count)
  