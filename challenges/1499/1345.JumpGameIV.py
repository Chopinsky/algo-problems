'''
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.

Constraints:

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8
'''


from typing import List
from collections import defaultdict


class Solution:
  def minJumps(self, arr: List[int]) -> int:
    group = defaultdict(list)
    for i, val in enumerate(arr):
      group[val].append(i)
      
    curr, nxt = set([0]), set()
    seen = set([0])
    steps = 0
    end = len(arr)-1
    # print(group)
    
    while curr:
      if end in curr:
        return steps
      
      for pos in curr:
        if pos-1 not in seen and pos-1 >= 0:
          nxt.add(pos-1)
          seen.add(pos-1)
          
        if pos+1 not in seen and pos+1 <= end:
          if pos+1 == end:
            return steps+1
          
          nxt.add(pos+1)
          seen.add(pos+1)
          
        val = arr[pos]
        for nxt_pos in group[val]:
          if nxt_pos not in seen:
            if nxt_pos == end:
              return steps + 1
            
            nxt.add(nxt_pos)
            seen.add(nxt_pos)
        
        group.pop(val, None)
      
      curr, nxt = nxt, curr
      nxt.clear()
      steps += 1
      
    return end
  