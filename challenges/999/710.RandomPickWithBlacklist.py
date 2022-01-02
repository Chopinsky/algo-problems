'''
You are given an integer n and an array of unique integers blacklist. Design an algorithm to pick a random integer in the range [0, n - 1] that is not in blacklist. Any integer that is in the mentioned range and not in blacklist should be equally likely to be returned.

Optimize your algorithm such that it minimizes the number of calls to the built-in random function of your language.

Implement the Solution class:

Solution(int n, int[] blacklist) Initializes the object with the integer n and the blacklisted integers blacklist.
int pick() Returns a random integer in the range [0, n - 1] and not in blacklist.

Example 1:

Input
["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
[[7, [2, 3, 5]], [], [], [], [], [], [], []]
Output
[null, 0, 4, 1, 6, 1, 0, 4]

Explanation
Solution solution = new Solution(7, [2, 3, 5]);
solution.pick(); // return 0, any integer from [0,1,4,6] should be ok. Note that for every call of pick,
                 // 0, 1, 4, and 6 must be equally likely to be returned (i.e., with probability 1/4).
solution.pick(); // return 4
solution.pick(); // return 1
solution.pick(); // return 6
solution.pick(); // return 1
solution.pick(); // return 0
solution.pick(); // return 4
 

Constraints:

1 <= n <= 10^9
0 <= blacklist.length <- min(10^5, n - 1)
0 <= blacklist[i] < n
All the values of blacklist are unique.
At most 2 * 10^4 calls will be made to pick.
'''


from random import randint, random
from typing import List
from bisect import bisect_right


class Solution0:
  def __init__(self, n: int, blacklist: List[int]):
    m = len(blacklist)
    self.valid_len = n - m
    
    b_a = [num for num in blacklist if num < self.valid_len]
    b_b = [num for num in blacklist if num >= self.valid_len]
    
    whitelist = set(list(range(n - m, n)))
    for num in b_b:
      whitelist.remove(num)

    self.mapping = {}
    for num in b_a:
      self.mapping[num] = whitelist.pop()

  def pick(self) -> int:
    k = int(random() * self.valid_len)
    if k not in self.mapping:
      return k
    
    return self.mapping[k]
      

class Solution:
  def __init__(self, n: int, blacklist: List[int]):
    self.blacklist = sorted(blacklist)
    self.total = n - len(blacklist)
    self.partial_range_count = self.blacklist[-1] + 1 - len(blacklist) if blacklist else 0


  def pick(self) -> int:
    idx = randint(0, self.total-1)
    # print('init', idx, self.blacklist[0], self.blacklist[-1])
    
    if (not self.blacklist) or (idx < self.blacklist[0]):
      return idx
      
    if idx >= self.partial_range_count:
      # print('exceed', idx, self.partial_range_count)
      return self.blacklist[-1] + 1 + (idx - self.partial_range_count)
    
    l, r = self.blacklist[0], self.blacklist[-1]
    
    while l < r:
      m = (l + r) // 2
      jdx = bisect_right(self.blacklist, m) - 1
      cnt = m - jdx
      # print('bisect', idx, m, jdx, cnt)
      
      if cnt == idx+1 and self.blacklist[jdx] != m:
        l = m
        break
        
      if cnt < idx+1:
        l = m + 1
      else:
        r = m - 1
      
    # print(idx, l)
    return l
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()