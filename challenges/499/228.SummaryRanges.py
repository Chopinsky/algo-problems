'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-2^31 <= nums[i] <= 2^31 - 1
All the values of nums are unique.
nums is sorted in ascending order.
'''


from typing import List


class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
    if not nums:
      return ''
    
    start, end = nums[0], nums[0]
    res = []
    
    for val in nums[1:]:
      if val != end+1:
        res.append(f'{start}' if start == end else f'{start}->{end}')
        start = val
        end = val
      else:
        end = val
      
    res.append(f'{start}' if start == end else f'{start}->{end}')
    
    return res
        
        
  def summaryRanges(self, nums: List[int]) -> List[str]:
    if not nums:
      return []
      
    s, e = nums[0], nums[0]
    ans = []
    
    for val in nums[1:]:
      if val == e+1:
        e = val
      else:
        if s == e:
          ans.append(str(s))
        else:
          ans.append(str(s) + '->' + str(e))
          
        s, e = val, val
        
    if s == e:
      ans.append(str(s))
    else:
      ans.append(str(s) + '->' + str(e))
      
    return ans
    