'''
You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment [left, right] where left <= right is the XOR of all the elements with indices between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right].

Return the minimum number of elements to change in the array such that the XOR of all segments of size k​​​​​​ is equal to zero.

Example 1:

Input: nums = [1,2,0,3,0], k = 1
Output: 3
Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].

Example 2:

Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
Output: 3
Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].

Example 3:

Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
Output: 3
Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].
 

Constraints:

1 <= k <= nums.length <= 2000
​​​​​​0 <= nums[i] < 2^10
'''


from typing import List
from collections import defaultdict


class Solution:
  def minChanges(self, nums: List[int], k: int) -> int:        
    freq = [defaultdict(int) for _ in range(k)]
    for i, val in enumerate(nums):
      freq[i%k][val] += 1

    max_reuse = []
    for i in range(k):
      max_reuse.append(max(freq[i].values()))

    max_reuse_suffix = max_reuse.copy()
    for i in range(k-2, -1, -1):
      max_reuse_suffix[i] += max_reuse_suffix[i+1]
      
    ### case 1: choose k-1 num, swap it to a different 
    ###         number such that the xor of the most seen 
    ###         numbers from other positions equals this number
    reuse = max_reuse_suffix[0] - min(max_reuse)
    
    ### case 2: choose k num, try finding the number combinations
    ###         such that using these numbers will lead us to the
    ###         xor sum of 0, i.e. reuse some of the numbers in the
    ###         positions and swap only between seen numbers; this
    ###         could include the *correct* solution to case 1 if
    ###         the xor sum of the rest numbers are also seen in the
    ###         min(max_reuse) position
    def dfs(i: int, xor: int, curr: int):
      nonlocal reuse
      
      if i == k:
        if xor == 0:
          reuse = max(reuse, curr)

        return
      
      # pruning, only taking the route that can yield to a larger
      # usage of the existing numbers
      if curr + max_reuse_suffix[i] > reuse:
        for val in freq[i]:
          dfs(i+1, xor^val, curr+freq[i][val])

    dfs(0, 0, 0)
    
    return len(nums) - reuse 
      
      
  def minChanges0(self, nums: List[int], k: int) -> int:
    n = len(nums)
    
    if k == 1:
      return sum(1 if nums[i] else 0 for i in range(n))
    
    if n <= k:
      xor = nums[0]
      for val in nums[1:]:
        xor ^= val
        
      return 1 if xor != 0 else 0
    
    counter = [defaultdict(int) for _ in range(k)]
    least = n
    
    for i, val in enumerate(nums):
      counter[i%k][val] += 1
      least = min(least, n - counter[i%k][val])
      
    singles_xor = 0
    singles_cnt = 0
    
    for c in counter:
      if len(c) == 1:
        val = list(c)[0]
        singles_xor ^= val
        singles_cnt += c[val]
        
    singles_max_save = 0
    for c in counter:
      if len(c) > 1:
        singles_max_save = max(singles_max_save, c[singles_xor])
    
    # edge case: all segment-positions have unique numbers, we
    # only need to change the number with the least counts, or 
    # if xor is already 0, we're done
    if singles_cnt == n:
      if not singles_xor:
        return 0
      
      return min(list(counter[i].values())[0] for i in range(len(counter)))
    
    least = min(least, n-singles_cnt-singles_max_save)
    last, curr = {}, {}
    seg_cnt = n // k
    
    for i in range(k-1):
      total = seg_cnt + (1 if seg_cnt*k+i < n else 0)
      if i == 0:
        for v0, c0 in counter[i].items():
          last[v0] = total - c0
          
        # print('init', i, last)
        continue
      
      for v0, c0 in counter[i].items():
        change = total - c0        
        for v1, c1 in last.items():
          if v1^v0 not in curr:
            curr[v1^v0] = c1 + change
          else:
            curr[v1^v0] = min(curr[v1^v0], c1 + change)
      
      last, curr = curr, last
      curr.clear()
      # print('dp', i, last)
      
    total = seg_cnt + (1 if seg_cnt*k+(k-1) < n else 0)
    curr = counter[k-1]
    # print('final', last, curr)
    
    for v1, c1 in last.items():
      cnt = c1 + total - curr[v1]
      least = min(least, cnt)
    
    return least
  