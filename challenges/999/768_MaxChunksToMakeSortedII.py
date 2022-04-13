'''
You are given an integer array arr.

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.

Constraints:

1 <= arr.length <= 2000
0 <= arr[i] <= 10^8
'''

from typing import List
from collections import defaultdict


class Solution:
  def maxChunksToSorted(self, arr: List[int]) -> int:
    seg_top = []

    for val in arr:
      curr_max = val

      # merge all segments that has to be 1 due to `val`
      while seg_top and seg_top[-1] > val:
        last_top = seg_top.pop()
        curr_max = max(curr_max, last_top)

      # push the new segment that
      seg_top.append(curr_max)

    return len(seg_top)


  def maxChunksToSorted(self, arr: List[int]) -> int:
    sa = sorted(arr)
    pos = defaultdict(list)
    
    for i, val in enumerate(sa):
      pos[val].append(i)
      
    last = -1
    count = 0
    
    for i, val in enumerate(arr):
      p = pos[val][0]
      pos[val] = pos[val][1:]
      last = max(last, p)
      
      if last == i:
        count += 1
        last = -1
        
    return count
    