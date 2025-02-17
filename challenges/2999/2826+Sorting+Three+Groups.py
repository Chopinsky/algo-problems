'''
2826. Sorting Three Groups

You are given an integer array nums. Each element in nums is 1, 2 or 3. In each operation, you can remove an element from nums. Return the minimum number of operations to make nums non-decreasing.

Example 1:

Input: nums = [2,1,3,2,1]

Output: 3

Explanation:

One of the optimal solutions is to remove nums[0], nums[2] and nums[3].

Example 2:

Input: nums = [1,3,2,1,3,3]

Output: 2

Explanation:

One of the optimal solutions is to remove nums[1] and nums[2].

Example 3:

Input: nums = [2,2,2,2,3,3]

Output: 0

Explanation:

nums is already non-decreasing.

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 3

Follow-up: Can you come up with an algorithm that runs in O(n) time complexity?

[2,1,3,2,1]
[1,3,2,1,3,3]
[2,2,2,2,3,3]
[3,3,2]
'''

from typing import List
from bisect import bisect_right

class Solution:
  '''
  longest increamental subseq
  '''
  def minimumOperations(self, nums: List[int]) -> int:
    res=[]
    
    for num in nums:
      n=bisect_right(res, num)
      if n < len(res):
        res[n] = num
      else:
        res.append(num)
        
    return len(nums) - len(res)
  
  def minimumOperations(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
      return 0
    
    if n == 2:
      return 1 if nums[0] > nums[1] else 0
    
    ones = []
    twos = []
    threes = []
    debug = False
      
    for val in nums:
      if val == 1:
        ones.append(ones[-1]+1 if ones else 1)
      else:
        ones.append(ones[-1] if ones else 0)
        
      if val == 2:
        twos.append(twos[-1]+1 if twos else 1)
      else:
        twos.append(twos[-1] if twos else 0)
        
      if val == 3:
        threes.append(threes[-1]+1 if threes else 1)
      else:
        threes.append(threes[-1] if threes else 0)
    
    ops = len(nums)-1
    # only 1s, or 2s, or 3s
    ops = min(ops, n-ones[-1], n-twos[-1], n-threes[-1])
    
    if debug:
      print(ones, twos, threes)
    
    def count(arr: List, i: int, j: int) -> int:
      if i >= n or j < i:
        return 0
      
      return arr[j] - (arr[i-1] if i > 0 else 0)
    
    for i in range(n):
      # [1,3]
      c1 = ones[i]
      c3 = count(threes, i+1, n-1)
      op = (i+1-c1) + (n-i-1-c3)
      ops = min(ops, op)
      
      # [2,3]
      c2 = twos[i]
      op = (i+1-c2) + (n-i-1-c3)
      ops = min(ops, op)
      
      if debug:
        print('iter:', i)
        print('0:', op)
        print('1:', op, c2, c3)
      
      # [1,2,3]
      for j in range(i+1, n):
        c2 = count(twos, i+1, j)
        c3 = count(threes, j+1, n-1)
        l2 = j-(i+1)+1
        l3 = n-j-1
        op = (i+1-c1) + (l2-c2) + (l3-c3)
        ops = min(ops, op)
        if debug:
          print('2:', j, op)
    
    return ops
        