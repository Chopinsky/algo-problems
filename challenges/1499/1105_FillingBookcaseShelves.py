'''
You are given an array books where books[i] = [thicknessi, heighti] indicates the thickness and height of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is less than or equal to shelfWidth, then build another level of the shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Example 1:

Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.
Example 2:

Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4

Constraints:

1 <= books.length <= 1000
1 <= thicknessi <= shelfWidth <= 1000
1 <= heighti <= 1000
'''

from typing import List
from functools import lru_cache

class Solution:
  def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
    n = len(books)
    
    @lru_cache(None)
    def dp(i: int):
      if i >= n:
        return 0
      
      h, w = books[i][1]+dp(i+1), books[i][0]
      top_h = books[i][1]
      
      for j in range(i+1, n):
        w0, h0 = books[j]
        if w+w0 > shelfWidth:
          break
          
        w += w0
        top_h = max(top_h, h0)
        h = min(h, top_h + dp(j+1))
        
      return h
    
    return dp(0)
        
  def minHeightShelves(self, books: List[List[int]], width: int) -> int:
    last_min = books[-1][1]
    dp, nxt = {}, {}
    dp[books[-1][0]] = (0, books[-1][1])
    
    for i in range(len(books)-2, -1, -1):
      w, h = books[i]
      nxt = {}
      nxt[w] = (last_min, h)
      last_min += h
      
      for w0 in dp:
        w1 = w0 + w
        if w1 > width:
          continue
          
        nxt_h = max(h, dp[w0][1])
        nxt_total = dp[w0][0] + nxt_h
        
        if w1 not in nxt or nxt_total < sum(nxt[w1]) or (nxt_total == sum(nxt[w1]) and nxt[w1][0] > dp[w0][0]):
          nxt[w1] = (dp[w0][0], nxt_h)
          
        last_min = min(last_min, sum(nxt[w1]))
      
      dp, nxt = nxt, dp
      nxt.clear()
    
    return last_min
    