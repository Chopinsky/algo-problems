'''
2343. Query Kth Smallest Trimmed Number

You are given a 0-indexed array of strings nums, where each string is of equal length and consists of only digits.

You are also given a 0-indexed 2D integer array queries where queries[i] = [ki, trimi]. For each queries[i], you need to:

Trim each number in nums to its rightmost trimi digits.
Determine the index of the kith smallest trimmed number in nums. If two trimmed numbers are equal, the number with the lower index is considered to be smaller.
Reset each number in nums to its original length.
Return an array answer of the same length as queries, where answer[i] is the answer to the ith query.

Note:

To trim to the rightmost x digits means to keep removing the leftmost digit, until only x digits remain.
Strings in nums may contain leading zeros.
 

Example 1:

Input: nums = ["102","473","251","814"], queries = [[1,1],[2,3],[4,2],[1,2]]
Output: [2,2,1,0]
Explanation:
1. After trimming to the last digit, nums = ["2","3","1","4"]. The smallest number is 1 at index 2.
2. Trimmed to the last 3 digits, nums is unchanged. The 2nd smallest number is 251 at index 2.
3. Trimmed to the last 2 digits, nums = ["02","73","51","14"]. The 4th smallest number is 73.
4. Trimmed to the last 2 digits, the smallest number is 2 at index 0.
   Note that the trimmed number "02" is evaluated as 2.
Example 2:

Input: nums = ["24","37","96","04"], queries = [[2,1],[2,2]]
Output: [3,0]
Explanation:
1. Trimmed to the last digit, nums = ["4","7","6","4"]. The 2nd smallest number is 4 at index 3.
   There are two occurrences of 4, but the one at index 0 is considered smaller than the one at index 3.
2. Trimmed to the last 2 digits, nums is unchanged. The 2nd smallest number is 24.
 
Constraints:

1 <= nums.length <= 100
1 <= nums[i].length <= 100
nums[i] consists of only digits.
All nums[i].length are equal.
1 <= queries.length <= 100
queries[i].length == 2
1 <= ki <= nums.length
1 <= trimi <= nums[i].length

Follow up: Could you use the Radix Sort Algorithm to solve this problem? What will be the complexity of that solution?
'''

from typing import List


class Solution:
  '''
  using Radix Sort to solve the problem
  '''
  def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
    ans = [-1] * len(queries)
    q = sorted((state[1], state[0], i) for i, state in enumerate(queries))
    curr = [[(nums[i], i) for i in range(len(nums))]] + [list() for _ in range(9)]
    nxt = [list() for _ in range(10)]
    
    def sort(lvl: int):
      for lst in nxt:
        lst.clear()

      for i in range(10):
        for val, j in curr[i]:
          nxt[int(val[-lvl])].append((val, j))
      
      # print(lvl, nxt)
      return nxt, curr
      
    def get_kth(k: int) -> int:
      cnt = 1
      
      for i in range(10):
        for _, idx in curr[i]:
          if cnt == k:
            return idx
          
          cnt += 1
        
      return -1
      
    idx = 0
    for c, k, i in q:
      # print(c, k, i)
      while idx < c:
        idx += 1
        curr, nxt = sort(idx)
      
      ans[i] = get_kth(k)
      # print('assign:', k, get_kth(i, idx))
      
    return ans
  
  
  def smallestTrimmedNumbers0(self, nums: List[str], queries: List[List[int]]) -> List[int]:
    ans = [-1] * len(queries)
    q = sorted([(state[1], state[0], i) for i, state in enumerate(queries)], reverse=True)
    curr = sorted((val, i) for i, val in enumerate(nums))
    # print(curr, q)
    
    for c, idx, j in q:
      if c < len(curr[0][0]):
        curr = sorted((val[-c:], i) for val, i in curr)
        # print(c, curr)
        
      # print(c, idx, j)
      ans[j] = curr[idx-1][1]
    
    return ans
        