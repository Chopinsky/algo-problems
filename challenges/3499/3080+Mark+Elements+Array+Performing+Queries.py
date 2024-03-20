'''
Mark Elements on Array by Performing Queries

You are given a 0-indexed array nums of size n consisting of positive integers.

You are also given a 2D array queries of size m where queries[i] = [indexi, ki].

Initially all elements of the array are unmarked.

You need to apply m queries on the array in order, where on the ith query you do the following:

Mark the element at index indexi if it is not already marked.
Then mark ki unmarked elements in the array with the smallest values. If multiple such elements exist, mark the ones with the smallest indices. And if less than ki unmarked elements exist, then mark all of them.
Return an array answer of size m where answer[i] is the sum of unmarked elements in the array after the ith query.

Example 1:

Input: nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]

Output: [8,3,0]

Explanation:

We do the following queries on the array:

Mark the element at index 1, and 2 of the smallest unmarked elements with the smallest indices if they exist, the marked elements now are nums = [1,2,2,1,2,3,1]. The sum of unmarked elements is 2 + 2 + 3 + 1 = 8.
Mark the element at index 3, since it is already marked we skip it. Then we mark 3 of the smallest unmarked elements with the smallest indices, the marked elements now are nums = [1,2,2,1,2,3,1]. The sum of unmarked elements is 3.
Mark the element at index 4, since it is already marked we skip it. Then we mark 2 of the smallest unmarked elements with the smallest indices if they exist, the marked elements now are nums = [1,2,2,1,2,3,1]. The sum of unmarked elements is 0.
Example 2:

Input: nums = [1,4,2,3], queries = [[0,1]]

Output: [7]

Explanation: We do one query which is mark the element at index 0 and mark the smallest element among unmarked elements. The marked elements will be nums = [1,4,2,3], and the sum of unmarked elements is 4 + 3 = 7.

Constraints:

n == nums.length
m == queries.length
1 <= m <= n <= 10^5
1 <= n <= 10^5
queries[i].length == 2
0 <= indexi, ki <= n - 1
'''

from typing import List

class Solution:
  def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    s0 = sum(nums)
    n = len(nums)
    cand = sorted((val, i) for i, val in enumerate(nums))
    cdx = 0
    marked = set()
    ans = []
    
    for idx, c0 in queries:
      if idx not in marked:
        marked.add(idx)
        s0 -= nums[idx]
      
      while cdx < len(cand) and c0 > 0:
        v0, jdx = cand[cdx]
        cdx += 1
        
        if jdx in marked:
          continue
          
        # print('pop:', jdx, v0)
        s0 -= v0
        c0 -= 1
        marked.add(jdx)
        
      ans.append(s0)
      # print(marked)
    
    return ans
        