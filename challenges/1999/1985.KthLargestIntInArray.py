'''
You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

Example 1:

Input: nums = ["3","6","7","10"], k = 4
Output: "3"
Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3".

Example 2:

Input: nums = ["2","21","12","1"], k = 3
Output: "2"
Explanation:
The numbers in nums sorted in non-decreasing order are ["1","2","12","21"].
The 3rd largest integer in nums is "2".

Example 3:

Input: nums = ["0","0"], k = 2
Output: "0"
Explanation:
The numbers in nums sorted in non-decreasing order are ["0","0"].
The 2nd largest integer in nums is "0".

Constraints:

1 <= k <= nums.length <= 104
1 <= nums[i].length <= 100
nums[i] consists of only digits.
nums[i] will not have any leading zeros.
'''


class Solution:
  def kthLargestNumber(self, nums: List[str], k: int) -> str:
    # arr = [int(s) for s in nums]
    arr = sorted(nums, key=lambda x: int(x))
    return arr[len(arr)-k]
  
    '''
    def kth(i: int, j: int, k: int) -> int:
      if j-i+1 == k:
        return min(arr[i:j+1])
      
      high, low = max(arr[i:j+1]), min(arr[i:j+1])
      if high == low:
        return high
      
      p = (high + low) / 2.0
      l, r = i, j
      
      while i < j:
        while i <= r and arr[i] <= p:
          i += 1
          
        while j >= l and arr[j] > p:
          j -= 1
        
        if i >= j:
          break
          
        arr[i], arr[j] = arr[j], arr[i]
      
      count = r-i+1
      # print('after', l, r, k, i, j, count)
      
      if count == k:
        return min(arr[i:r+1])
      
      if count < k:
        return kth(l, j, k-count)
      
      return kth(i, r, k)
    
    return str(kth(0, len(arr)-1, k))
    '''
  
