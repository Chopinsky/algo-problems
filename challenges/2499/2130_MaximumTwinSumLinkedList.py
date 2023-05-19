'''
2130. Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Example 1:


Input: head = [5,4,2,1]
Output: 6
Explanation:
Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
There are no other nodes with twins in the linked list.
Thus, the maximum twin sum of the linked list is 6. 
Example 2:

Input: head = [4,2,2,3]
Output: 7
Explanation:
The nodes with twins present in this linked list are:
- Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
- Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 
Example 3:

Input: head = [1,100000]
Output: 100001
Explanation:
There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

Constraints:

The number of nodes in the list is an even integer in the range [2, 10^5].
1 <= Node.val <= 10^5
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    lst = []
    curr = head
    
    while curr:
      lst.append(curr)
      curr = curr.next
      
    i, j = 0, len(lst)-1
    val = 0
    
    while i < j:
      val = max(val, (lst[i].val+lst[j].val))
      i += 1
      j -= 1
      
    return val
        

  def pairSum(self, head: Optional[ListNode]) -> int:
    fast, slow, prev = head, head, None
    max_val = 0
    
    while fast and fast.next:
      fast = fast.next.next
      nxt = slow.next
      prev, prev.next = slow, prev
      slow = nxt
      
    if fast:
      slow = slow.next
      
    while prev and slow:
      max_val = max(max_val, prev.val + slow.val)  
      prev = prev.next
      slow = slow.next
      
    return max_val
    
  
  def pairSum(self, head: Optional[ListNode]) -> int:
    stack = []
    curr = head
    
    while curr:
      stack.append(curr.val)
      curr = curr.next
      
    i, j = 0, len(stack)-1
    max_val = 0
    
    while i < j:
      max_val = max(max_val, stack[i]+stack[j])
      i += 1
      j -= 1
    
    return max_val
    