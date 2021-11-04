'''
You are given a string s, an integer k, a letter letter, and an integer repetition.

Return the lexicographically smallest subsequence of s of length k that has the letter letter appear at least repetition times. The test cases are generated so that the letter appears in s at least repetition times.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A string a is lexicographically smaller than a string b if in the first position where a 
and b differ, string a has a letter that appears earlier in the alphabet than the corresponding 
letter in b.

Example 1:

Input: s = "leet", k = 3, letter = "e", repetition = 1
Output: "eet"
Explanation: There are four subsequences of length 3 that have the letter 'e' appear at least 1 time:
- "lee" (from "leet")
- "let" (from "leet")
- "let" (from "leet")
- "eet" (from "leet")
The lexicographically smallest subsequence among them is "eet".

Example 2:

example-2
Input: s = "leetcode", k = 4, letter = "e", repetition = 2
Output: "ecde"
Explanation: "ecde" is the lexicographically smallest subsequence of length 4 that has the letter "e" appear at least 2 times.

Example 3:

Input: s = "bb", k = 2, letter = "b", repetition = 2
Output: "bb"
Explanation: "bb" is the only subsequence of length 2 that has the letter "b" appear at least 2 times.

Constraints:

1 <= repetition <= k <= s.length <= 5 * 10^4
s consists of lowercase English letters.
letter is a lowercase English letter, and appears in s at least repetition times.
'''


class Solution:
  def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
    drop, letter_drop, stack = len(s) - k, s.count(letter) - repetition, [chr(ord('a')-1)]
    
    for ch in s:
      # if we can drop the last char in the stack
      while drop and stack[-1] > ch and (stack[-1] != letter or letter_drop):
        last = stack.pop()
        drop -= 1
        if last == letter:
          letter_drop -= 1
          
      stack.append(ch)
        
    ans = ''.join(stack[1:])
    fill = max(repetition - ans.count(letter, 0, k), 0)
    i = k - 1
    
    while i >= 0 and fill:
      if ans[i] != letter:
        fill -= 1
        
      i -= 1
      
    return ans[:i+1] + letter * (k-i-1)


  def smallestSubsequence0(self, s: str, k: int, letter: str, repetition: int) -> str:
    n = len(s)
    if k == n:
      return s
    
    if k == repetition:
      return letter * k
    
    rem, added = 0, 0
    for i in range(n):
      if s[i] == letter:
        rem += 1
        
    i, n = 0, len(s)
    stack = []
    
    while i < n:
      # need all chars in the remainder string
      if len(stack) + n - i == k:
        # stack.append(i)
        # i += 1
        # continue
        return ''.join([s[j] for j in stack]) + s[i:]
      
      # smaller subseq possible and we still have chars left in the remaining
      # string to play with
      if stack and s[i] < s[stack[-1]] and len(stack) + n - i > k:
        # can pop the last char to get a smaller subseq
        if (s[stack[-1]] != letter) or (rem + added > repetition):
          j = stack.pop()
          if s[j] == letter:
            added -= 1
            
          continue
        
      # skip char to save space for the letters
      if (len(stack) - added + repetition == k) and (s[i] != letter):
        # i += 1
        # continue
        return ''.join([s[j] for j in stack]) + letter * (k - len(stack))
        
      if s[i] != letter and len(stack) >= k:
        i += 1
        continue

      # update counters
      if s[i] == letter:
        rem -= 1
        added += 1
        
      stack.append(i)
      i += 1
        
    # popping out all extra chars
    while len(stack) > k:
      stack.pop()
      
    # build the answer string
    return ''.join([s[i] for i in stack])
    