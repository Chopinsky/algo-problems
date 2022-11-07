'''
433. Minimum Genetic Mutation

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:

Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
Example 3:

Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3

Constraints:

start.length == 8
end.length == 8
0 <= bank.length <= 10
bank[i].length == 8
start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
'''

from typing import List
from collections import defaultdict


class Solution:
  def minMutation(self, start: str, end: str, bank: List[str]) -> int:
    if end not in bank:
      return -1
    
    if start == end:
      return 0
    
    pairs = defaultdict(set)
    n = len(bank)
    ln = len(bank[0])
    
    def get_diff(a, b):
      diff = 0
      
      for k in range(ln):
        if a[k] != b[k]:
          diff += 1
        
        if diff > 1:
          break
              
      return diff  
    
    for i in range(n):
      diff = get_diff(start, bank[i])
      if diff == 1:
        pairs[start].add(bank[i])
      
      for j in range(i+1, n):
        diff = get_diff(bank[i], bank[j])
        if diff == 1:
          pairs[bank[i]].add(bank[j])
          pairs[bank[j]].add(bank[i])
          
    # print(pairs)
    curr, nxt = pairs[start].copy(), set()
    steps = 1
    seen = set()
    
    while curr and end not in curr:
      seen |= curr
      for w in curr:
        nxt |= pairs[w]
      
      curr, nxt = nxt, curr
      nxt.clear()
      steps += 1
      
    return -1 if end not in curr else steps
    