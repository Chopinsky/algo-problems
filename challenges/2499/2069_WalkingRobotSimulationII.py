'''
A width x height grid is on an XY-plane with the bottom-left cell at (0, 0) and the top-right cell at (width - 1, height - 1). The grid is aligned with the four cardinal directions ("North", "East", "South", and "West"). A robot is initially at cell (0, 0) facing direction "East".

The robot can be instructed to move for a specific number of steps. For each step, it does the following.

Attempts to move forward one cell in the direction it is facing.
If the cell the robot is moving to is out of bounds, the robot instead turns 90 degrees counterclockwise and retries the step.
After the robot finishes moving the number of steps required, it stops and awaits the next instruction.

Implement the Robot class:

Robot(int width, int height) Initializes the width x height grid with the robot at (0, 0) facing "East".
void step(int num) Instructs the robot to move forward num steps.
int[] getPos() Returns the current cell the robot is at, as an array of length 2, [x, y].
String getDir() Returns the current direction of the robot, "North", "East", "South", or "West".

Example 1:

example-1
Input
["Robot", "step", "step", "getPos", "getDir", "step", "step", "step", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
Output
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

Explanation
Robot robot = new Robot(6, 3); // Initialize the grid and the robot at (0, 0) facing East.
robot.step(2);  // It moves two steps East to (2, 0), and faces East.
robot.step(2);  // It moves two steps East to (4, 0), and faces East.
robot.getPos(); // return [4, 0]
robot.getDir(); // return "East"
robot.step(2);  // It moves one step East to (5, 0), and faces East.
                // Moving the next step East would be out of bounds, so it turns and faces North.
                // Then, it moves one step North to (5, 1), and faces North.
robot.step(1);  // It moves one step North to (5, 2), and faces North (not West).
robot.step(4);  // Moving the next step North would be out of bounds, so it turns and faces West.
                // Then, it moves four steps West to (1, 2), and faces West.
robot.getPos(); // return [1, 2]
robot.getDir(); // return "West"

Constraints:

2 <= width, height <= 100
1 <= num <= 10^5
At most 10^4 calls in total will be made to step, getPos, and getDir.
'''

from typing import List


class Robot:
  def __init__(self, width: int, height: int):
    self.x, self.y = 0, 0
    self.w = width
    self.h = height
    self.curr = 1
    self.dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    

  def turn(self):
    self.curr -= 1
    if self.curr < 0:
      self.curr += 4
      
      
  def move(self, d: int):
    dx, dy = self.dirs[self.curr]
    self.x += d * dx
    self.y += d * dy 

    
  def step(self, num: int) -> None:
    ln = 2 * (self.w + self.h - 2)
    num = num % ln
    
    while num > 0:
      if self.curr == 1:
        d = min(num, self.w-self.x-1)
        
      elif self.curr == 3:
        d = min(num, self.x)
        
      elif self.curr == 0:
        d = min(num, self.h-self.y-1)
        
      else:
        d = min(num, self.y)
        
      self.move(d)
      if d < num:
        self.turn()
      
      num -= d

    if self.y == 0 and 1 <= self.x:
      self.curr = 1
      
    elif self.x == self.w-1 and 1 <= self.y:
      self.curr = 0
      
    elif self.y == self.h-1 and self.x < self.w-1:
      self.curr = 3
      
    else:
      self.curr = 2

      
  def getPos(self) -> List[int]:
    return [self.x, self.y]


  def getDir(self) -> str:
    if self.curr == 0:
      return 'North'
    
    if self.curr == 1:
      return 'East'
    
    if self.curr == 2:
      return 'South'
    
    return 'West'
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()