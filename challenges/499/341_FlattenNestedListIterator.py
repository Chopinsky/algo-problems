'''
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.

Example 1:

Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
 

Constraints:

1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-10^6, 10^6].
'''

from typing import List


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
  def isInteger(self) -> bool:
      """
      @return True if this NestedInteger holds a single integer, rather than a nested list.
      """

  def getInteger(self) -> int:
      """
      @return the single integer that this NestedInteger holds, if it holds a single integer
      Return None if this NestedInteger holds a nested list
      """

  def getList(self) -> List["NestedInteger"]:
      """
      @return the nested list that this NestedInteger holds, if it holds a nested list
      Return None if this NestedInteger holds a single integer
      """


class NestedIterator:
  def __init__(self, nestedList: List["NestedInteger"]):
    self.stack = []
    if not nestedList:
      return 
    
    curr, lst = nestedList[0], nestedList[1:]
    if lst:
      self.stack.append(lst)
    
    while curr and not curr.isInteger():
      lst = curr.getList()
      if not lst:
        if not self.stack:
          return
        
        lst = self.stack.pop()
        curr, lst = lst[0], lst[1:]
        if lst:
          self.stack.append(lst)
          
        continue
        
      curr, lst = lst[0], lst[1:]
      if lst:
        self.stack.append(lst)

    if curr:
      self.stack.append(curr)
      
    # print('init', self.stack)
    

  def next(self) -> int:
    if not self.stack:
      return -1
    
    top = self.stack.pop()
    val = top.getInteger()
    
    if self.stack:
      p = self.stack.pop()
      curr, p = p[0], p[1:]
      if p:
        self.stack.append(p)
        
      while curr and not curr.isInteger():
        lst = curr.getList()
        if not lst:
          if not self.stack:
            return val

          lst = self.stack.pop()
          curr, lst = lst[0], lst[1:]
          if lst:
            self.stack.append(lst)
            
          continue
          
        curr, lst = lst[0], lst[1:]
        if lst:
          self.stack.append(lst)
    
      if curr:
        self.stack.append(curr)
        
    return val
    

  def hasNext(self) -> bool:
    return len(self.stack) > 0
  

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())