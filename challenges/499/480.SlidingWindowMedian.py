'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.

For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation: 
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6

Example 2:

Input: nums = [1,2,3,4,2,3,1,4,2], k = 3
Output: [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]

Constraints:

1 <= k <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
'''


from typing import List
from heapq import heapify, heappop, heappush, heappushpop
from collections import defaultdict


class Solution:
  def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    large, small = [], []
    ans = []
    removed = defaultdict(int)

    def median():
      return (large[0]-small[0]) / 2.0 if k%2 == 0 else large[0]

    # build the init stacks
    for i in range(k):
      if len(large) == len(small):
        heappush(large, -heappushpop(small, -nums[i]))
      else:
        heappush(small, -heappushpop(large, nums[i]))
    
    ans.append(median())

    for i in range(k, len(nums)):
      heappush(small, -heappushpop(large, nums[i]))
      
      remove = nums[i-k]
      removed[remove] += 1

      # removed 1 element from the large stack
      if remove > -small[0]:
        heappush(large, -heappop(small))

      while small and removed[-small[0]] > 0:
          removed[-small[0]] -= 1
          heappop(small)
      
      while large and removed[large[0]] > 0:
          removed[large[0]] -= 1
          heappop(large)

      ans.append(median())

    return ans


  def medianSlidingWindow0(self, nums: List[int], k: int) -> List[float]:
    ans = []
    
    # no array, done    
    if not nums:
      return ans
    
    # all median value is the number itself
    if k == 1:
      return nums
    
    # build the init window
    n = len(nums)
    src = sorted(nums[:k])
    small = src[:(k+1)//2]
    big = src[(k+1)//2:]
    
    # add the first median
    remove = defaultdict(int)
    s_cnt, b_cnt = len(small), len(big)
    even_dist = (s_cnt == b_cnt)
    
    for i in range(s_cnt):
      small[i] = -small[i]
    
    heapify(small)
    heapify(big)
    ans.append(-small[0] if (k % 2) else (big[0] - small[0]) / 2.0)
    
    # print(k, s_cnt, b_cnt, even_dist)
    # print(small, big)
    
    def remove_popped():
      # actually pop removed values from small's max-heap
      top = -small[0]
      while small and remove[top] > 0:
        heappop(small)
        remove[top] -= 1
        top = -small[0] if small else None
      
      # pop removed values from big's min-heap
      top = big[0]
      while big and remove[top] > 0:
        heappop(big)
        remove[top] -= 1
        top = big[0] if big else None
    
    # slide the window
    for i in range(k, n):
      # mark nums[i-k] as removed
      rval, val = nums[i-k], nums[i]
      # print(i, nums[i-k+1:i+1])
      
      # pretend we popped rval from the heaps it belongs
      remove[rval] += 1
      if rval <= ans[-1]:
        s_cnt -= 1
      else:
        b_cnt -= 1
        
      # print('after pops', small, big, s_cnt, b_cnt)
      # curr_med = -small[0] if (k % 2) else (big[0]-small[0]) / 2.0
      
      # adding new value to the proper arr
      if val <= ans[-1]:
        heappush(small, -val)
        s_cnt += 1
      else:
        heappush(big, val)
        b_cnt += 1
        
      # get rid of the popped
      remove_popped()
      
      # overflow rebalance
      while True:
        # if balanced, done
        if (even_dist and s_cnt == b_cnt) or (not even_dist and s_cnt == b_cnt+1):
          break
          
        if s_cnt < b_cnt:
          # from big to small
          p_val = heappop(big)
          if remove[p_val] > 0:
            remove[p_val] -= 1
            continue
            
          heappush(small, -p_val)
          s_cnt += 1
          b_cnt -= 1
        
        else:
          # from small to big
          p_val = -heappop(small)
          if remove[p_val] > 0:
            remove[p_val] -= 1
            continue
            
          heappush(big, p_val) 
          s_cnt -= 1
          b_cnt += 1
            
      # get rid of the popped again
      remove_popped()
        
      # print('after all', small, big)
      ans.append(-small[0] if (k % 2) else (big[0]-small[0]) / 2.0)
    
    return ans
  