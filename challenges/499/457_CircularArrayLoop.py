'''
457. Circular Array Loop

You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.
Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:

Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
Every nums[seq[j]] is either all positive or all negative.
k > 1
Return true if there is a cycle in nums, or false otherwise.

Example 1:

Input: nums = [2,-1,1,2,2]
Output: true
Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --> 2 --> 3 --> 0 --> ..., and all of its nodes are white (jumping in the same direction).
Example 2:

Input: nums = [-1,-2,-3,-4,-5,6]
Output: false
Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
The only cycle is of size 1, so we return false.
Example 3:

Input: nums = [1,-1,5,1,4]
Output: true
Explanation: The graph shows how the indices are connected. White nodes are jumping forward, while red is jumping backward.
We can see the cycle 0 --> 1 --> 0 --> ..., and while it is of size > 1, it has a node jumping forward and a node jumping backward, so it is not a cycle.
We can see the cycle 3 --> 4 --> 3 --> ..., and all of its nodes are white (jumping in the same direction).

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
nums[i] != 0

Follow up: Could you solve it in O(n) time complexity and O(1) extra space complexity?
'''

from typing import List


class Solution:
  def circularArrayLoop(self, nums: List[int]) -> bool:
    seen = set()
    n = len(nums)
    
    def dfs(curr: int) -> bool:
      # print('check:', curr)
      while curr not in seen:
        seen.add(curr)
        
        # a self-ref cycle
        if abs(nums[curr])%n == 0:
          return False
          
        curr = (n+curr+nums[curr]) % n
        # print(curr)
      
      if abs(nums[curr])%n == 0:
        return False
      
      if curr in seen:
        flow = (nums[curr] > 0)
        # print('flow', curr, flow)
        head = curr
        nxt = (n+curr+nums[curr]) % n
        
        while nxt != head:
          if (nums[nxt] > 0) != flow or curr == nxt:
            return False
          
          curr = nxt
          nxt = (n+curr+nums[curr]) % n
      
      return True
      
    for i in range(n):
      if i in seen:
        continue
        
      if dfs(i):
        return True
      
    return False
  