'''
Under the grammar given below, strings can represent a set of lowercase words. Let's use R(expr) to denote the set of words the expression represents.

Grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
Formally, the three rules for our grammar:

For every lowercase letter x, we have R(x) = {x}.
For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

Example 1:

Input: expression = "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]
Example 2:

Input: expression = "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.

Constraints:

1 <= expression.length <= 60
expression[i] consists of '{', '}', ','or lowercase English letters.
The given expression represents a set of words based on the grammar given in the description.
'''


from typing import List


class Solution:
  def braceExpansionII(self, e: str) -> list[str]:
    n = len(e)
    if not e:
      return [e]

    def gen(i: int):
      res = set()
      curr = [""]
      j = i

      while j < n:
        ch = e[j]
        if ch == '}':
          res |= set(curr)
          j += 1
          break

        if ch == '{':
          arr, j = gen(j+1)
          nxt = []

          for s0 in curr:
            for s1 in arr:
              if not s1:
                continue

              nxt.append(s0+s1)

          curr = nxt
          continue

        if ch == ',':
          res |= set(curr)
          curr = [""]
          j += 1
          continue

        # a char, append to the current strings
        for i in range(len(curr)):
          curr[i] += ch

        j += 1

      # print('gen:', e[i:j+1], res)
      if curr:
        res |= set(curr)

      return res, j

    i = 1 if e[0] == '{' else 0
    ans = set()

    while i < n:
      res, i = gen(i)
      res.discard("")
      if not ans:
        ans = res
        continue

      nxt = set()
      for s0 in ans:
        if not s0:
          continue

        for s1 in res:
          if not s1:
            continue
            
          nxt.add(s0+s1)
      
      ans = nxt
      # print('inner:', res, nxt)

    return sorted(ans)
        
  def braceExpansionII(self, expr: str) -> List[str]:
    idx = 0
    n = len(expr)

    def parse() -> List[str]:
      nonlocal idx

      stack = set()
      last = ['']
      
      while idx < n:
        ch = expr[idx]
        
        if ch == '{':
          idx += 1
          batch = parse()
          nxt = []
          
          if last and last[0]:
            for lw in last:
              for bw in batch:
                nxt.append(lw + bw)
            
            last = nxt
            
          else:
            last = batch
            
          # print('from bottom', ch, last)
          continue
          
        if ch == '}' or ch == ',':
          idx += 1
          
          for w in last:
            if w not in stack:
              stack.add(w)
          
          # print('ending', ch, last, stack)
          if ch == '}':
            return sorted(stack)
          
          last = ['']
          continue
          
        for i in range(len(last)):
          last[i] += ch
          
        idx += 1
          
      if len(last) > 1 or last[0]:
        for w in last:
          stack.add(w)
        
      return sorted(stack)
      
    return parse()
          