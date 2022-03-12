'''
You are given a string s consisting only of lowercase English letters.

In one move, you can select any two adjacent characters of s and swap them.

Return the minimum number of moves needed to make s a palindrome.

Note that the input will be generated such that s can always be converted to a palindrome.

Example 1:

Input: s = "aabb"
Output: 2
Explanation:
We can obtain two palindromes from s, "abba" and "baab". 
- We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
- We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
Thus, the minimum number of moves needed to make s a palindrome is 2.
Example 2:

Input: s = "letelt"
Output: 2
Explanation:
One of the palindromes we can obtain from s in 2 moves is "lettel".
One of the ways we can obtain it is "letelt" -> "letetl" -> "lettel".
Other palindromes such as "tleelt" can also be obtained in 2 moves.
It can be shown that it is not possible to obtain a palindrome in less than 2 moves.
 

Constraints:

1 <= s.length <= 2000
s consists only of lowercase English letters.
s can be converted to a palindrome using a finite number of moves.
'''


class Solution:
  '''
  idea is to find chars from left and right that will move to the left/right-ends
  with the minimum amount of total swaps, remove these 2 chars, and rinse and repeat
  '''
  def minMovesToMakePalindrome(self, s: str) -> int:
    steps = 0
    lp, rp = {}, {}
        
    while len(s) > 2:
      n = len(s)
      l, r = 0, n-1
      least_steps = n
      lpos, rpos = -1, -1
      lp.clear()
      rp.clear()
      
      while l < n and l < least_steps:
        lc, rc = s[l], s[r]
        
        if lc not in lp:
          lp[lc] = l
          
        if rc not in rp:
          rp[rc] = n-1-r
          
        if lc in rp and lp[lc]+rp[lc] < least_steps:
          least_steps = lp[lc] + rp[lc]
          lpos = lp[lc]
          rpos = n-1-rp[lc]
          
        if rc in lp and lp[rc]+rp[rc] < least_steps:
          least_steps = lp[rc] + rp[rc]
          lpos = lp[rc]
          rpos = n-1-rp[rc]
          
        l += 1
        r -= 1
        
      steps += least_steps
      # print(steps, s, lpos, rpos)
      s = s[:lpos] + s[lpos+1:rpos] + s[rpos+1:]
      
    return steps
  