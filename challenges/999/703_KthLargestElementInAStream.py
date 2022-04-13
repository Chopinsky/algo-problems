'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
 

Constraints:

1 <= k <= 10^4
0 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
-10^4 <= val <= 10^4
At most 10^4 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
'''

from typing import List
from heapq import heappushpop, heappush


class KthLargest:
  def __init__(self, k: int, nums: List[int]):    
    self.heap = sorted(nums)[-k:] if nums else []
    self.k = k
    # print(self.heap, sorted(nums)[-k:][:5], len(self.heap), len(nums), min(nums))
        

  def add(self, val: int) -> int:
    # print(len(self.heap), self.heap[:5], self.k)
    
    if self.k == 1:
      if not self.heap:
        self.heap.append(val)
      else:
        self.heap[0] = max(self.heap[0], val)
        
      return self.heap[0]
      
    if len(self.heap) < self.k:
      heappush(self.heap, val)
    elif val > self.heap[0]:
      # print(val, self.heap[:5])
      heappushpop(self.heap, val)
      
    # print(val, self.heap[0])
    return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)