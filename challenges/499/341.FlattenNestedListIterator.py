'''
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.


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
The values of the integers in the nested list is in the range [-106, 106].
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
  def __init__(self, nestedList: [NestedInteger]):
    self._list = nestedList
    self._stack = []

    self.updateStack(self._list.pop(0))
    # print(self._stack)


  def next(self) -> int:
    tail = self._stack.pop()
    idx = len(self._stack)-1

    while idx >= 0 and len(self._stack[idx]) == 0:
      self._stack.pop()
      idx -= 1

    if len(self._stack) > 0:
      curr = self._stack[idx].pop(0)
    elif len(self._list) > 0:
      curr = self._list.pop(0)
    else:
      curr = None

    if curr is not None:
      self.updateStack(curr)

    return tail


  def hasNext(self) -> bool:
    return len(self._stack) > 0


  def updateStack(self, curr: NestedInteger):
    while not curr.isInteger():
      nextList = curr.getList()

      if len(nextList) == 0:
        if len(self._stack) == 0:
          if len(self._list) == 0:
            return

          curr = self._list.pop(0)
          continue

        else:
          nextList = self._stack.pop()
          while len(nextList) == 0 and len(self._stack) > 0:
            nextList = self._stack.pop()

          if len(nextList) == 0:
            if len(self._list) == 0:
              return

            curr = self._list.pop(0)
            continue

      curr = nextList.pop(0)

      # if len(nextList) > 0:
      self._stack.append(nextList)

    self._stack.append(curr)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())