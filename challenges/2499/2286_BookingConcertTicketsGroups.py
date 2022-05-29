'''
A concert hall has n rows numbered from 0 to n - 1, each with m seats, numbered from 0 to m - 1. You need to design a ticketing system that can allocate seats in the following cases:

If a group of k spectators can sit together in a row.
If every member of a group of k spectators can get a seat. They may or may not sit together.
Note that the spectators are very picky. Hence:

They will book seats only if each member of their group can get a seat with row number less than or equal to maxRow. maxRow can vary from group to group.
In case there are multiple rows to choose from, the row with the smallest number is chosen. If there are multiple seats to choose in the same row, the seat with the smallest number is chosen.
Implement the BookMyShow class:

BookMyShow(int n, int m) Initializes the object with n as number of rows and m as number of seats per row.
int[] gather(int k, int maxRow) Returns an array of length 2 denoting the row and seat number (respectively) of the first seat being allocated to the k members of the group, who must sit together. In other words, it returns the smallest possible r and c such that all [c, c + k - 1] seats are valid and empty in row r, and r <= maxRow. Returns [] in case it is not possible to allocate seats to the group.
boolean scatter(int k, int maxRow) Returns true if all k members of the group can be allocated seats in rows 0 to maxRow, who may or may not sit together. If the seats can be allocated, it allocates k seats to the group with the smallest row numbers, and the smallest possible seat numbers in each row. Otherwise, returns false.

Example 1:

Input
["BookMyShow", "gather", "gather", "scatter", "scatter"]
[[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]
Output
[null, [0, 0], [], true, false]

Explanation
BookMyShow bms = new BookMyShow(2, 5); // There are 2 rows with 5 seats each 
bms.gather(4, 0); // return [0, 0]
                  // The group books seats [0, 3] of row 0. 
bms.gather(2, 0); // return []
                  // There is only 1 seat left in row 0,
                  // so it is not possible to book 2 consecutive seats. 
bms.scatter(5, 1); // return True
                   // The group books seat 4 of row 0 and seats [0, 3] of row 1. 
bms.scatter(5, 1); // return False
                   // There are only 2 seats left in the hall.

Constraints:

1 <= n <= 5 * 10^4
1 <= m, k <= 10^9
0 <= maxRow <= n - 1
At most 5 * 10^4 calls in total will be made to gather and scatter.
'''

from typing import List


'''
build a segment tree to query and/or update the range sum or max sum of the rows
'''
class TreeNode:
  def __init__(self, l: int, r: int, m: int):
    if l > r:
      return
    
    self.l = l
    self.r = r
    self.m = m
    
    if l == r:
      self.max_rem = m
      self.total_rem = m
      return
    
    mid = (l + r) // 2
    self.lc = TreeNode(l, mid, m)
    self.rc = TreeNode(mid+1, r, m)
    self.max_rem = m
    self.total_rem = 0

    if self.lc:
      self.total_rem += self.lc.total_rem

    if self.rc:
      self.total_rem += self.rc.total_rem
  
  
  def update(self):
    self.max_rem = max(self.lc.max_rem if self.lc else 0, 
                       self.rc.max_rem if self.rc else 0)
    
    self.total_rem = (self.lc.total_rem if self.lc else 0) + (self.rc.total_rem if self.rc else 0)
    
    if self.lc and not self.lc.total_rem:
      self.lc = None
      
    if self.rc and not self.rc.total_rem:
      self.rc = None
    
  
  def gather(self, k: int, mr: int):
    if self.max_rem < k or self.l > mr:
      return None
    
    # is leaf
    if self.l == self.r:
      start = self.m - self.total_rem
      self.total_rem -= k
      self.max_rem -= k
      return [self.l, start]
    
    # not a leaf, find answer in the subtree
    res = None
    if self.lc:
      res = self.lc.gather(k, mr)
      
    if not res and self.rc:
      res = self.rc.gather(k, mr)
    
    # self adjustment
    self.update()
    
    return res
    
  
  def scatter(self, k: int, mr: int) -> bool:
    cnt = self.count(k, mr)
    if cnt < k:
      return False
    
    self.scatter_take(k, mr)  
    return True
  
    
  def count(self, k: int, mr: int) -> int:
    if self.l > mr:
      return 0
    
    if self.r <= mr:
      return self.total_rem
    
    cnt = self.lc.count(k, mr) if self.lc else 0
    if cnt < k and self.rc and self.rc.l <= mr:
      cnt += self.rc.count(k, mr)
    
    return cnt
    
    
  def scatter_take(self, k: int, mr: int):
    if self.l > mr:
      return k
    
    # if we must use all seats in the subtree
    if self.r <= mr and self.total_rem <= k:
      rest = k - self.total_rem
      self.lc = None
      self.rc = None
      self.max_rem = 0
      self.total_rem = 0
      return rest
    
    # if a leaf (and has more than needed)
    if self.l == self.r:
      self.max_rem -= k
      self.total_rem -= k
      return 0
    
    # update required seat counts
    if self.lc:
      k = self.lc.scatter_take(k, mr)
      
    if k > 0 and self.rc:
      k = self.rc.scatter_take(k, mr)
    
    self.update()
    return k
  
  
class BookMyShow:
  '''
  build row-based segement tree to query seat availabilities
  '''
  def __init__(self, n: int, m: int):
    self.root = TreeNode(0, n-1, m)


  def gather(self, k: int, max_row: int) -> List[int]:
    return self.root.gather(k, max_row)


  def scatter(self, k: int, max_row: int) -> bool:
    return self.root.scatter(k, max_row)
        


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)