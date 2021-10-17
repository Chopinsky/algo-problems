'''
Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:

Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.

Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1

Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1

Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
'''

class Solution:
  def ways(self, pizza: List[str], k: int) -> int:
    m, n, mod = len(pizza), len(pizza[0]), 1000000007
    counts = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(m-1, -1, -1):
      for j in range(n-1, -1, -1):
        counts[i][j] = (1 if pizza[i][j] == 'A' else 0) + counts[i][j+1] + counts[i+1][j] - counts[i+1][j+1]
        
    # for r in counts:
    #   print(r)
      
    # for pizza with (i, j) as the top-left corner, and
    # we need to make k cuts from it
    @lru_cache(None)
    def dp(i: int, j: int, k: int) -> int:
      # no apples beyond this point, always 0 cuts
      if not counts[i][j]:
        return 0
      
      # if no more pieces to be cut, done, render the 
      # remaining pizza as the one -- 1 way to make this
      # happen
      if not k:
        return 1
      
      cnt = 0
      
      # horizontal cuts
      for i0 in range(i+1, m):
        # there are apples in between row-i and row-i0, 
        # this is a valid cut
        if counts[i][j] - counts[i0][j] > 0:
          cnt = (cnt + dp(i0, j, k-1)) % mod
      
      # vertical cuts
      for j0 in range(j+1, n):
        # there are apples in between col-j and col-j0,
        # this is a valid cut
        if counts[i][j] - counts[i][j0] > 0:
          cnt = (cnt + dp(i, j0, k-1)) % mod

      return cnt 
    
    return dp(0, 0, k-1)
    
