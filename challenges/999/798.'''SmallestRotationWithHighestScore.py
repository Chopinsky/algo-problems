'''
You are given an array nums. You can rotate it by a non-negative integer k so that the array becomes [nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]]. Afterward, any entries that are less than or equal to their index are worth one point.

For example, if we have nums = [2,4,1,3,0], and we rotate by k = 2, it becomes [1,3,0,2,4]. This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].
Return the rotation index k that corresponds to the highest score we can achieve if we rotated nums by it. If there are multiple answers, return the smallest such index k.

Example 1:

Input: nums = [2,3,1,4,0]
Output: 3
Explanation: Scores for each k are listed below: 
k = 0,  nums = [2,3,1,4,0],    score 2
k = 1,  nums = [3,1,4,0,2],    score 3
k = 2,  nums = [1,4,0,2,3],    score 3
k = 3,  nums = [4,0,2,3,1],    score 4
k = 4,  nums = [0,2,3,1,4],    score 3
So we should choose k = 3, which has the highest score.
Example 2:

Input: nums = [1,3,0,2,4]
Output: 0
Explanation: nums will always have 3 points no matter how it shifts.
So we will choose the smallest k, which is 0.
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] < nums.length
'''


from typing import List


class Solution:
  def bestRotation(self, nums: List[int]) -> int:
    n = len(nums)
    
    # count of numbers with 0 score for i-shifts, 
    # this will needs to accumulate to get the 
    # actual count ... 
    no_score = [0] * n
    
    for i, val in enumerate(nums):
      # the number of shifts that will yield 0 score 
      # as a result for number val @ index-i
      left, right = (i - val + 1) % n, (i + 1) % n
      
      # keep track of the accumulated area, i.e. for 
      # [left, right] to be the bad region, we only need
      # to do no_score[left]--, and no_score[right+1]++,
      # which they wrap needs to round around `n`.
      no_score[left] -= 1
      no_score[right] += 1
      
      # wrapping around the `n` here
      if left > right:
        no_score[0] -= 1
        # `no_score[n] += 1` is omitted here

    best = -n
    ans, curr = 0, 0
    
    # the accumulated scores 
    for i, score in enumerate(no_score):
      curr += score
      if curr > best:
        best = curr
        ans = i

    return ans
  
      
  def bestRotation0(self, nums: List[int]) -> int:
    n = len(nums)
    arr = [0] * (n+2)
    score, rotates = 0, 0
    
    def update(idx: int, val: int):
      idx += 1

      while idx < n+1:
        arr[idx] += val
        idx += (idx & -idx)

    def query(idx: int) -> int:
      s = 0
      idx += 1

      while idx > 0:
        s += arr[idx]
        idx -= (idx & -idx)

      return s
    
    def make_updates(x: int, y: int):
      if y < x:
        return 
      
      # print('updating:', x, y)
      update(x, 1)
      update(y+1, -1)
      
    for i, val in enumerate(nums):
      # print(i, val)
      if val == 0:
        # any shifts will always add 1 point
        make_updates(0, n-1)
        continue
        
      if val == n-1:
        if i == n-1:
          make_updates(0, 0)
        else:
          make_updates(i+1, i+1)
          
        continue
        
      if val > i:
        # if the range has 1 part
        x = i+1
        y = x + (n-1-val)
        make_updates(x, y)
        
      else:
        # if the range has 2 parts
        make_updates(0, i-val)
        make_updates(i+1, n-1)
      
    # print(arr)
    for i in range(n):
      curr_score = query(i)
      # print(i, curr_score)
      
      if curr_score > score:
        rotates = i
        score = curr_score
    
    return rotates
    