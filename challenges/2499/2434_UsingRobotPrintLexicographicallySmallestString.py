'''
2434. Using a Robot to Print the Lexicographically Smallest String

You are given a string s and a robot that currently holds an empty string t. Apply one of the following operations until s and t are both empty:

Remove the first character of a string s and give it to the robot. The robot will append this character to the string t.
Remove the last character of a string t and give it to the robot. The robot will write this character on paper.
Return the lexicographically smallest string that can be written on the paper.

Example 1:

Input: s = "zza"
Output: "azz"
Explanation: Let p denote the written string.
Initially p="", s="zza", t="".
Perform first operation three times p="", s="", t="zza".
Perform second operation three times p="azz", s="", t="".
Example 2:

Input: s = "bac"
Output: "abc"
Explanation: Let p denote the written string.
Perform first operation twice p="", s="c", t="ba". 
Perform second operation twice p="ab", s="c", t="". 
Perform first operation p="ab", s="", t="c". 
Perform second operation p="abc", s="", t="".
Example 3:

Input: s = "bdda"
Output: "addb"
Explanation: Let p denote the written string.
Initially p="", s="bdda", t="".
Perform first operation four times p="", s="", t="bdda".
Perform second operation four times p="addb", s="", t="".

Constraints:

1 <= s.length <= 10^5
s consists of only English lowercase letters.
'''

from collections import Counter


class Solution:
  def robotWithString(self, s: str) -> str:
    stack = []
    res = []
    rem = Counter(s)
    cand = sorted(rem)[::-1]
    # print('init:', rem, cand)

    for ch in s:
      while cand and rem[cand[-1]] == 0:
        cand.pop()

      while stack and stack[-1] <= cand[-1]:
        res.append(stack.pop())

      # take the char from s
      # print('ch:', ch, cand, rem, stack)
      rem[ch] -= 1
      if ch == cand[-1]:
        res.append(ch)
      else:
        stack.append(ch)

    res += stack[::-1]

    return ''.join(res)
        
  def robotWithString(self, s: str) -> str:
    cand = sorted(set(s), reverse=True)
    counter = Counter(s)
    stack = []
    res = ''
    
    for ch in s:
      # print(ch, cand, counter['o'])
      while stack and stack[-1] <= cand[-1]:
        top = stack.pop()
        res += top
        
      if ch == cand[-1]:
        res += ch
        counter[ch] -= 1
        # print('append', ch)
        
        while cand and counter[cand[-1]] == 0:
          cand.pop()
          
      else:
        # print('back up', ch, cand[-1], stack)
        stack.append(ch)
        counter[ch] -= 1
        while cand and counter[cand[-1]] == 0:
          cand.pop()
          
    return res + (''.join(stack[::-1]) if stack else '')
     