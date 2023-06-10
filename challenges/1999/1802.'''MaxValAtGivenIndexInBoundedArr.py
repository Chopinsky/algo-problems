'''
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3
 

Constraints:

1 <= n <= maxSum <= 109
0 <= index < n
'''


class Solution:
  def maxValue(self, n: int, index: int, maxSum: int) -> int:
    def check(val: int) -> bool:
      if val*n <= maxSum:
        return True
      
      val -= 1
      
      lc = index
      lv = max(1, val-lc)
      ls = ((lv+val-1) * (val-lv)) // 2
      
      rc = n-1-index
      rv = max(0, val-rc)
      rs = ((rv+val-1) * (val-rv)) // 2
      
      # print('check:', val+1, (lc, lv, ls), (rc, rv, rs))
      
      return ls + rs + val + n <= maxSum
    
    l, r = 0, maxSum
    res = 0
    
    while l <= r:
      mid = (l+r)//2
      if check(mid):
        res = max(res, mid)
        l = mid + 1
      else:
        r = mid - 1
        
    return res
    
        
  def maxValue(self, n: int, index: int, maxSum: int) -> int:
    if n == 1:
      return maxSum
    
    extra = maxSum - n
    l, r = 1, extra + 1
    last = l
    
    def check(val: int) -> int:
      total = 0
      above = val - 1
      
      # add left
      if index-above+1 >= 0:
        total += ((above+1) * above) // 2
      else:
        total += ((above+above-index) * (index+1)) // 2
        
      # add right
      if index+above <= n:
        total += ((above+1) * above) // 2
      else:
        total += ((above+above-n+index+1) * (n-index)) // 2
        
      # added 1 more above into the total
      total -= above
      # if val == 3:
      #   print('check', val, total, extra, above)
      
      if total == extra:
        return 0
      
      return -1 if total < extra else 1
    
    while l < r:
      m = (l+r) // 2
      diff = check(m)
      # print('mid', m, diff, l, r)
      
      if not diff:
        return m
        
      if diff < 0:
        # m is in the range, try lift low
        last = m
        l = m+1
      else:
        # m is too large, try reduce high
        r = m-1
      
    # print('out', last, l)
    return last if check(l) > 0 else l
  
