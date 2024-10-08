'''
725. Split Linked List in Parts

Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

Example 1:

Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].

Example 2:

Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.

Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50
'''

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    n = 0
    curr = head
    ans = []
    
    while curr:
      n += 1
      curr = curr.next
      
    cnt, mod = divmod(n, k)
    
    def split(curr, c: int):
      if not curr:
        return curr, None
      
      head = curr
      prev = None
      
      while c > 0 and curr:
        prev = curr
        curr = curr.next
        c -= 1
        
      if prev:
        prev.next = None
        
      return head, curr
    
    curr = head
    for i in range(k):
      h0, curr = split(curr, cnt+(1 if i < mod else 0))
      ans.append(h0)
      
    return ans
        
  def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    def get_len(curr):
      ln = 0
      while curr:
        ln += 1
        curr = curr.next
        
      return ln
    
    ans = [None for _ in range(k)]
    ln = get_len(head)
    c0 = ln // k
    rem = ln % k
    curr = head
    prev = None
    
    for i in range(k):
      ans[i] = curr
      c1 = c0 + (1 if i < rem else 0)
      # print('add', i, c1)
      
      while c1 > 0 and curr:
        prev = curr
        curr = curr.next
        c1 -= 1
        
      if prev:
        prev.next = None
    
    return ans
      
  def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    ans = [None for _ in range(k)]
    if not head:
      return ans
    
    if k == 1:
      ans[0] = head
      return ans
    
    l = 0
    curr = head
    
    while curr:
      l += 1
      curr = curr.next
      
    cnt = l // k
    extra = l - cnt*k
    curr = head
    
    def split(c: ListNode, n: int) -> ListNode:
      cnt = 0
      while c and cnt < n:
        cnt += 1
        
        if cnt < n:
          c = c.next
        else:
          nxt = c.next
          c.next = None
          c = nxt
      
      return c
    
    for i in range(k):
      ans[i] = curr
      curr = split(curr, cnt + (1 if i < extra else 0))  
        
    return ans
    