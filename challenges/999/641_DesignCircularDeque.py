'''
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
 
Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4

Constraints:

1 <= k <= 1000
0 <= value <= 1000
At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
'''


class MyCircularDeque:
  def __init__(self, k: int):
    self.cap = k
    self.len = 0
    self.vals = [0]*k
    self.l = 0
    self.r = 0

  def insertFront(self, value: int) -> bool:
    if self.isFull():
      return False
    
    if self.len > 0:
      self.l = (self.l + self.cap - 1) % self.cap
    
    self.vals[self.l] = value
    self.len += 1
    
    return True

  def insertLast(self, value: int) -> bool:
    if self.isFull():
      return False
    
    if self.len > 0:
      self.r = (self.r + 1) % self.cap
    
    self.vals[self.r] = value
    self.len += 1
    
    return True

  def deleteFront(self) -> bool:
    if self.isEmpty():
      return False
    
    self.l = (self.l + 1) % self.cap
    self.len -= 1
    
    if self.len == 0:
      self.r = self.l
    
    return True

  def deleteLast(self) -> bool:
    if self.isEmpty():
      return False
      
    self.r = (self.r - 1 + self.cap) % self.cap
    self.len -= 1
    
    if self.len == 0:
      self.r = self.l
    
    return True

  def getFront(self) -> int:
    if self.isEmpty():
      return -1

    return self.vals[self.l]
  
  def getRear(self) -> int:
    if self.isEmpty():
      return -1
      
    # print('rear:', self.vals, (self.l, self.r))
    return self.vals[self.r]

  def isEmpty(self) -> bool:
    return self.len == 0

  def isFull(self) -> bool:
    return self.len == self.cap
  

class MyCircularDeque0:
  def __init__(self, k: int):
    self.q = [0] * k
    self.l = 0
    self.r = 0
    self.count = 0
    

  def insertFront(self, value: int) -> bool:
    if self.count == len(self.q):
      return False
    
    nxt = self.l - 1
    if nxt < 0:
      nxt += len(self.q)
      
    self.q[nxt] = value
    self.count += 1
    self.l = nxt
    
    return True
    

  def insertLast(self, value: int) -> bool:
    if self.count == len(self.q):
      return False
    
    self.q[self.r] = value
    self.count += 1
    
    nxt = self.r + 1
    if nxt >= len(self.q):
      nxt -= len(self.q)

    self.r = nxt
    return True
    

  def deleteFront(self) -> bool:
    if not self.count:
      return False
    
    self.l += 1
    if self.l >= len(self.q):
      self.l -= len(self.q)
    
    self.count -= 1
    return True


  def deleteLast(self) -> bool:
    if not self.count:
      return False
    
    self.r -= 1
    if self.r < 0:
      self.r += len(self.q)
      
    self.count -= 1
    return True


  def getFront(self) -> int:
    if not self.count:
      return -1
    
    return self.q[self.l]


  def getRear(self) -> int:
    if not self.count:
      return -1
    
    pos = self.r - 1
    if pos < 0:
      pos += len(self.q)
      
    return self.q[pos]


  def isEmpty(self) -> bool:
    return self.count == 0


  def isFull(self) -> bool:
    return self.count == len(self.q)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()