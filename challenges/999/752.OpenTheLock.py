'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.

Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1

Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.
target and deadends[i] consist of digits only.
'''

from typing import List

class Solution:
  def openLock(self, deadends: List[str], target: str) -> int:
    curr, nxt = ['0000'], []
    seen = set(curr)
    dead = set(deadends)
    
    if '0000' in dead:
      return -1
    
    if '0000' == target:
      return 0
    
    def to_string(d, prefix, suffix):
      return prefix + chr(ord('0') + d) + suffix
      
    def rotate(s: str, add_to: List):
      for i in range(4):
        d = int(s[i])
        s0 = to_string((d+1) % 10, s[:i], s[i+1:])
        s1 = to_string((d+9) % 10, s[:i], s[i+1:])
        
        if s0 == target or s1 == target:
          return True
        
        if s0 not in seen and s0 not in dead:
          seen.add(s0)
          add_to.append(s0)
        
        if s1 not in seen and s1 not in dead:
          seen.add(s1)
          add_to.append(s1)
      
      return False
    
    steps = 0
    while curr:
      steps += 1
      for s in curr:
        if rotate(s, nxt):
          return steps
        
      curr, nxt = nxt, curr
      nxt.clear()
      # print(steps, len(curr))
    
    return -1
        
  def openLock(self, deadends: List[str], target: str) -> int:
    d = set(deadends)
    if target in d or '0000' in d:
      return -1

    if target == '0000':
      return 0

    stack, temp = [target], []
    seen = set(stack)
    steps = 0

    def check(nums, temp):
      t = "".join(nums)

      if t == '0000':
        return True, temp

      if t in d:
        return False, temp

      if t not in seen:
        seen.add(t)
        temp.append(t)

      return False, temp

    while len(stack) > 0:
      steps += 1

      for num in stack:
        nums = list(num)
        pairs = ['0', '0']

        # print(nums)

        for i in range(4):
          src = nums[i]

          if src == '0':
            pairs[0] = '1'
            pairs[1] = '9'
          elif src == '9':
            pairs[0] = '8'
            pairs[1] = '0'
          else:
            pairs[0] = chr(ord(src)-1)
            pairs[1] = chr(ord(src)+1)

          for p in pairs:
            nums[i] = p
            done, temp = check(nums, temp)
            if done:
              return steps

          nums[i] = src

      stack, temp = temp, stack
      temp.clear()

      # print("round", steps, stack)

    return -1
