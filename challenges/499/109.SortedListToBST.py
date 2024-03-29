'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [0]
Output: [0]

Example 4:

Input: head = [1,3]
Output: [3,1]

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-10^5 <= Node.val <= 10^5
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:
  def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    stack = []
    curr = head
    
    while curr:
      stack.append(curr.val)
      curr = curr.next
      
    def build_tree(i: int, j: int):
      if i > j:
        return None
      
      m = (i + j) // 2
      root = TreeNode(stack[m])

      if i <= m-1:
        root.left = build_tree(i, m-1)

      if j >= m+1:
        root.right = build_tree(m+1, j)
      
      return root
    
    return build_tree(0, len(stack)-1)


  def sortedListToBST(self, head: ListNode) -> TreeNode:
    if not head:
      return None

    if not head.next:
      return TreeNode(head.val)

    s, f = head, head.next
    last = None

    while f:
      last = s
      s = s.next
      f = f.next

      if not f:
        break

      f = f.next

    root = TreeNode(s.val)
    root.right = self.sortedListToBST(s.next)

    if last:
      last.next = None

    root.left = self.sortedListToBST(head)
    return root
