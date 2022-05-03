'''
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5

Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
'''

from collections import defaultdict
from bisect import bisect_right


class SnapshotArray:
  def __init__(self, length: int):
    self.store = defaultdict(list)
    self.sid = defaultdict(list)
    
    self.len = length
    self.id = 0
    

  def set(self, index: int, val: int) -> None:
    if index >= self.len:
      return
    
    if self.sid[index] and self.sid[index][-1] == self.id:
      self.store[index][-1] = val
    else:
      self.sid[index].append(self.id)
      self.store[index].append(val)


  def snap(self) -> int:
    self.id += 1
    return self.id - 1


  def get(self, index: int, snap_id: int) -> int:
    if index >= self.len:
      return -1
    
    if not self.store[index] or snap_id < self.sid[index][0]:
      return 0
    
    j = bisect_right(self.sid[index], snap_id) - 1
    if j < 0:
      return 0
    
    return self.store[index][j]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)