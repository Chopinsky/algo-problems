'''
Design a queue that supports push and pop operations in the front, middle, and back.

Implement the FrontMiddleBack class:

FrontMiddleBack() Initializes the queue.
void pushFront(int val) Adds val to the front of the queue.
void pushMiddle(int val) Adds val to the middle of the queue.
void pushBack(int val) Adds val to the back of the queue.
int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].

Example 1:

Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)
 

Constraints:

1 <= val <= 10^9
At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront, popMiddle, and popBack.
'''


class FrontMiddleBackQueue:
  def __init__(self):
    self.left = []
    self.right = []
    

  def pushFront(self, val: int) -> None:
    if len(self.left) > len(self.right):
      last = self.left.pop()
      self.right = [last] + self.right
      
    self.left = [val] + self.left


  def pushMiddle(self, val: int) -> None:
    if len(self.left) > len(self.right):
      last = self.left.pop()
      self.right = [last] + self.right
      self.left.append(val)
    else:
      self.left.append(val)


  def pushBack(self, val: int) -> None:
    self.right.append(val)
    
    if len(self.left) < len(self.right):
      front, self.right = self.right[0], self.right[1:]
      self.left.append(front)
      

  def popFront(self) -> int:
    if not self.left:
      return -1
    
    if len(self.left) == len(self.right):
      front, self.right = self.right[0], self.right[1:]
      self.left.append(front)
      
    val, self.left = self.left[0], self.left[1:]
    return val


  def popMiddle(self) -> int:
    if not self.left:
      return -1
    
    val = self.left.pop()
    if len(self.left) < len(self.right):
      front, self.right = self.right[0], self.right[1:]
      self.left.append(front)
      
    return val


  def popBack(self) -> int:
    if not self.right and not self.left:
      return -1
        
    if len(self.left) > len(self.right):
      last = self.left.pop()
      self.right = [last] + self.right
      
    return self.right.pop()


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()