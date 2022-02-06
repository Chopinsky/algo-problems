'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
'''


from typing import List, Optional
from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
      return None
    
    heap = []
    head = ListNode()
    curr = head
    
    for i, h in enumerate(lists):
      if h:
        heappush(heap, (h.val, i))
      
    # print(heap)
    while heap:
      _, i = heappop(heap)
      
      node = lists[i]
      nxt = node.next
      
      curr.next = node
      node.next = None
      curr = curr.next
      
      lists[i] = nxt
      if nxt:
        heappush(heap, (nxt.val, i))
    
    return head.next
    