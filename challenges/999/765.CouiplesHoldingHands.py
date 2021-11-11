'''
There are n couples sitting in 2n seats arranged in a row and want to hold hands.

The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).

Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

Example 1:

Input: row = [0,2,1,3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:

Input: row = [3,2,0,1]
Output: 0
Explanation: All couples are already seated side by side.

Constraints:

2n == row.length
2 <= n <= 30
n is even.
0 <= row[i] < 2n
All the elements of row are unique.
'''


from typing import List
from collections import defaultdict


class Solution:
  '''
  the idea is to "connect" all couches that seat different couples, then the amount of
  needed swaps == the number of couches in the "connected" groups - 1 if number > 2, else 1.
  '''
  def minSwapsCouples(self, row: List[int]) -> int:
    n = len(row)
    idx = 0
    couples = defaultdict(list)
    couches = [i for i in range(n//2+1)]
    
    def find(i: int) -> int:
      while i != couches[i]:
        i = couches[i]
        
      return i
    
    def union(i: int, j: int) -> int:
      ii, ji = find(i), find(j)
      if ii <= ji:
        couches[ji] = ii
        return ii
      
      couches[ii] = ji
      return ji
    
    for i in range(0, n, 2):
      h, w = min(row[i], row[i+1]), max(row[i], row[i+1])
      # print(h, w)
      
      # the couple are in the same seat already
      if (h+1 == w) and (h%2 == 0):
        continue
        
      hi, wi = h//2, w//2
      couples[hi].append(idx)
      couples[wi].append(idx)
      
      if len(couples[hi]) == 2:
        union(couples[hi][0], couples[hi][1])
        
      if len(couples[wi]) == 2:
        union(couples[wi][0], couples[wi][1])
      
      idx += 1
      
    swaps = [0] * idx
    total = 0
    
    for i in range(idx):
      root = find(i)
      swaps[root] += 1
      
    # print(idx, couples, swaps)
    for s in swaps:
      if not s:
        continue
        
      total += s-1 if s > 1 else 1
      
    return total
  