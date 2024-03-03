'''
3072. Distribute Elements Into Two Arrays II

You are given a 1-indexed array of integers nums of length n.

We define a function greaterCount such that greaterCount(arr, val) returns the number of elements in arr that are strictly greater than val.

You need to distribute all the elements of nums between two arrays arr1 and arr2 using n operations. In the first operation, append nums[1] to arr1. In the second operation, append nums[2] to arr2. Afterwards, in the ith operation:

If greaterCount(arr1, nums[i]) > greaterCount(arr2, nums[i]), append nums[i] to arr1.
If greaterCount(arr1, nums[i]) < greaterCount(arr2, nums[i]), append nums[i] to arr2.
If greaterCount(arr1, nums[i]) == greaterCount(arr2, nums[i]), append nums[i] to the array with a lesser number of elements.
If there is still a tie, append nums[i] to arr1.
The array result is formed by concatenating the arrays arr1 and arr2. For example, if arr1 == [1,2,3] and arr2 == [4,5,6], then result = [1,2,3,4,5,6].

Return the integer array result.

Example 1:

Input: nums = [2,1,3,3]
Output: [2,3,1,3]
Explanation: After the first 2 operations, arr1 = [2] and arr2 = [1].
In the 3rd operation, the number of elements greater than 3 is zero in both arrays. Also, the lengths are equal, hence, append nums[3] to arr1.
In the 4th operation, the number of elements greater than 3 is zero in both arrays. As the length of arr2 is lesser, hence, append nums[4] to arr2.
After 4 operations, arr1 = [2,3] and arr2 = [1,3].
Hence, the array result formed by concatenation is [2,3,1,3].
Example 2:

Input: nums = [5,14,3,1,2]
Output: [5,3,1,2,14]
Explanation: After the first 2 operations, arr1 = [5] and arr2 = [14].
In the 3rd operation, the number of elements greater than 3 is one in both arrays. Also, the lengths are equal, hence, append nums[3] to arr1.
In the 4th operation, the number of elements greater than 1 is greater in arr1 than arr2 (2 > 1). Hence, append nums[4] to arr1.
In the 5th operation, the number of elements greater than 2 is greater in arr1 than arr2 (2 > 1). Hence, append nums[5] to arr1.
After 5 operations, arr1 = [5,3,1,2] and arr2 = [14].
Hence, the array result formed by concatenation is [5,3,1,2,14].
Example 3:

Input: nums = [3,3,3,3]
Output: [3,3,3,3]
Explanation: At the end of 4 operations, arr1 = [3,3] and arr2 = [3,3].
Hence, the array result formed by concatenation is [3,3,3,3].

Constraints:

3 <= n <= 10^5
1 <= nums[i] <= 10^9
'''

from typing import List, Dict

class Solution:
  def resultArray(self, nums: List[int]) -> List[int]:
    t1 = {}
    t2 = {}
    
    def build_trees(arr):
      if not arr:
        return -1
      
      mid = len(arr) // 2
      val = arr[mid]
      left_node = build_trees(arr[:mid])
      right_node = build_trees(arr[mid+1:])

      # tree node structure: [left_node_val, right_node_val, equal_count, greater_count]
      t1[val] = [left_node, right_node, 0, 0]
      t2[val] = [left_node, right_node, 0, 0]
      
      return val
    
    def update(tree: Dict, root: int, val: int):
      while root > 0:
        node = tree[root]
        if val == root:
          node[2] += 1
          return

        if val < root:
          root = node[0]
        else:
          # val > root
          node[3] += 1
          root = node[1]
    
    def query(tree: Dict, root: int, val: int) -> int:
      count = 0
      
      while root > 0:
        node = tree[root]
        if val == root:
          count += node[3] # add all numbers > val
          break
          
        if val < root:
          count += node[2] + node[3] # add all numbers >= root > val
          root = node[0]
        else:
          # val > root
          root = node[1]
        
      return count
    
    arr = sorted(set(nums))
    if len(arr) == 1:
      return nums
    
    root = build_trees(arr)
    left = [nums[0]]
    update(t1, root, nums[0])
    right = [nums[1]]
    update(t2, root, nums[1])
    # print('tree:', t1, t2, root)
    
    def check(val: int) -> int:
      lc = query(t1, root, val)
      rc = query(t2, root, val)
      
      if lc != rc:
        return 0 if lc > rc else 1
      
      lc = len(left)
      rc = len(right)
      
      if lc != rc:
        return 0 if lc < rc else 1
      
      return 0
    
    for val in nums[2:]:
      t0 = check(val)
      if t0 == 0:
        update(t1, root, val)
        left.append(val)
      else:
        update(t2, root, val)
        right.append(val)
    
    return left + right
        