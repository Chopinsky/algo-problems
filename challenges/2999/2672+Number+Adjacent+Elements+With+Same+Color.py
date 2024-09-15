'''
2672. Number of Adjacent Elements With the Same Color

You are given an integer n representing an array colors of length n where all elements are set to 0's meaning uncolored. You are also given a 2D integer array queries where queries[i] = [indexi, colori]. For the ith query:

Set colors[indexi] to colori.
Count adjacent pairs in colors set to the same color (regardless of colori).
Return an array answer of the same length as queries where answer[i] is the answer to the ith query.

Example 1:

Input: n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]

Output: [0,1,1,0,2]

Explanation:

Initially array colors = [0,0,0,0], where 0 denotes uncolored elements of the array.
After the 1st query colors = [2,0,0,0]. The count of adjacent pairs with the same color is 0.
After the 2nd query colors = [2,2,0,0]. The count of adjacent pairs with the same color is 1.
After the 3rd query colors = [2,2,0,1]. The count of adjacent pairs with the same color is 1.
After the 4th query colors = [2,1,0,1]. The count of adjacent pairs with the same color is 0.
After the 5th query colors = [2,1,1,1]. The count of adjacent pairs with the same color is 2.
Example 2:

Input: n = 1, queries = [[0,100000]]

Output: [0]

Explanation:

After the 1st query colors = [100000]. The count of adjacent pairs with the same color is 0.

Constraints:

1 <= n <= 10^5
1 <= queries.length <= 10^5
queries[i].length == 2
0 <= indexi <= n - 1
1 <=  colori <= 10^5
'''

from typing import List

class Solution:
  def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
    if n <= 1:
      return [0]*len(queries)
    
    ans = []
    colors = [0]*n
    total = 0
    
    for i, c in queries:
      prev_c = colors[i]
      if c == prev_c:
        ans.append(total)
        continue
      
      # update the color
      colors[i] = c
      
      if i > 0:
        if c == colors[i-1]:
          total += 1
          
        if prev_c > 0 and prev_c == colors[i-1]:
          total -= 1
      
      if i < n-1:
        if c == colors[i+1]:
          total += 1
          
        if prev_c > 0 and prev_c == colors[i+1]:
          total -= 1
          
      ans.append(total)
    
    return ans
        