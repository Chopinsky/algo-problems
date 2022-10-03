'''
Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the costs of deleting other characters will not change.

Example 1:

Input: s = "abaac", cost = [1,2,3,4,5]
Output: 3
Explanation: Delete the letter "a" with cost 3 to get "abac" (String without two identical letters next to each other).

Example 2:

Input: s = "abc", cost = [1,2,3]
Output: 0
Explanation: You don't need to delete any character because there are no identical letters next to each other.

Example 3:

Input: s = "aabaa", cost = [1,2,3,4,1]
Output: 2
Explanation: Delete the first and the last character, getting the string ("aba").
 

Constraints:

s.length == cost.length
1 <= s.length, cost.length <= 10^5
1 <= cost[i] <= 10^4
s contains only lowercase English letters.
'''


from typing import List


class Solution:
  def minCost(self, colors: str, time: List[int]) -> int:
    last = ''
    last_total = 0
    max_time = 0
    total = 0
    
    for i, c in enumerate(colors):
      if c == last:
        max_time = max(max_time, time[i])
        last_total += time[i]
        continue
        
      total += last_total - max_time
      last = c
      last_total = time[i]
      max_time = time[i]
      
    return total + (last_total - max_time)
   
   
  def minCost(self, s: str, cost: List[int]) -> int:
    ch = s[0]
    total, n = 0, len(s)
    curr_cost, high = cost[0], cost[0]
    
    for i in range(1, n):
      if s[i] != ch:
        # print(i, total, curr_cost, high)
        total += curr_cost - high
        curr_cost, high = cost[i], cost[i]
        ch = s[i]
      
      else:
        curr_cost += cost[i]
        high = max(high, cost[i])
        
    return total + curr_cost - high
