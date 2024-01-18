'''
1562. Find Latest Group of Size M

Given an array arr that represents a permutation of numbers from 1 to n.

You have a binary string of size n that initially has all its bits set to zero. At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1.

You are also given an integer m. Find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1's such that it cannot be extended in either direction.

Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.

Example 1:

Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation: 
Step 1: "00100", groups: ["1"]
Step 2: "00101", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "11101", groups: ["111", "1"]
Step 5: "11111", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.
Example 2:

Input: arr = [3,1,5,4,2], m = 2
Output: -1
Explanation: 
Step 1: "00100", groups: ["1"]
Step 2: "10100", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "10111", groups: ["1", "111"]
Step 5: "11111", groups: ["11111"]
No group of size 2 exists during any step.
 
Constraints:

n == arr.length
1 <= m <= n <= 10^5
1 <= arr[i] <= n
All integers in arr are distinct.
'''

from typing import List

class Solution:
  def findLatestStep(self, arr: List[int], m: int) -> int:
    seen = set()
    n = len(arr)
    g = [i for i in range(n)]
    seg = {}
    last = -1
    
    def find(x: int) -> int:
      while g[x] != x:
        x = g[x]
        
      return x
    
    def union(x: int, y: int):
      x0, y0 = find(x), find(y)
      if x0 <= y0:
        g[y0] = x0
      else:      
        g[x0] = y0
        
    for i, num in enumerate(arr):
      idx = num-1
      left, right = idx, idx
      
      if idx > 0 and idx-1 in seen:
        left = find(idx-1)
        
      if idx+1 < n and idx+1 in seen:
        right = idx+1
        
      # merge right to left, and self to left
      g[right] = left
      g[idx] = left
      
      # update segment size
      right_bound = seg[right] if right in seg else idx
      size_left, size_right = -1, -1
      
      # the left segment is merged but had the right size, mark
      # the last step it existed
      if left in seg:
        size_left = seg[left] - left + 1
      
      # the right segment is merged but had the right size, mark
      # the last step it existed
      if right in seg:
        size_right = seg[right] - right + 1
      
      if size_left == m or size_right == m:
        last = max(last, i)
          
      seg[left] = max(seg.get(left, left), right_bound)
      size = seg[left] - left + 1
      # print((i, num), (left, seg[left]), size)
      
      if size == m:
        last = i+1
      
      seen.add(idx)
        
    return last   
      