'''
You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
Example 2:

Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
Example 3:

Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].
 

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6
'''


class Solution:
  def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
    s1, s2 = sum(nums1), sum(nums2)
    count = 0
    
    # nums1 sums to a smaller number, and nums2 to a larger number
    if s1 > s2:
      s1, s2 = s2, s1
      nums1, nums2 = nums2, nums1
      
    l1, l2 = len(nums1), len(nums2)
    if l1 * 6 < l2:
      return -1
    
    c1, c2 = Counter(nums1), Counter(nums2)
    c1.pop(6, None)
    c2.pop(1, None)
    
    n1, n2 = sorted(c1, reverse=True), sorted(c2)
    print(c1, c2, n1, n2, s1, s2)
    
    while s1 < s2:
      if (not n1) or (n2 and (n2[-1]-1) >= (6-n1[-1])):
        val = n2.pop()
        cnt = c2[val]
        diff = val - 1
        pop_arr = 2
      else:
        val = n1.pop()
        cnt = c1[val]
        diff = 6 - val
        pop_arr = 1
        
      total = cnt * diff
      # print(pop_arr, total, s2-s1, diff, cnt)
      
      if total >= s2 - s1:
        # enough to fill the gap, increase the count and done
        if total == s2 - s1:
          count += cnt
        else:
          base = (s2 - s1) // diff
          count += base + (0 if (s2-s1)%diff == 0 else 1)
          
        break
        
      # we need more
      if pop_arr == 2:
        s2 -= total
      else:
        s1 += total
        
      count += cnt
        
    return count
  
