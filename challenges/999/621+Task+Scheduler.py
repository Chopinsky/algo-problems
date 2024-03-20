'''
621. Task Scheduler

You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100

## Test cases 

["A","A","A","B","B","B"]
2
["A","C","A","B","D","B"]
1
["A","A","A", "B","B","B"]
3
["A","A","B","B","C","C","D","D","E","E","F","F","G","G","H","H","I","I","J","J","K","K","L","L","M","M","N","N","O","O","P","P","Q","Q","R","R","S","S","T","T","U","U","V","V","W","W","X","X","Y","Y","Z","Z"]
2
["A","A","A","B","B","B","C","D","E","F","G","H","I","J","K"]
7
["A","B"]
2
'''

from typing import List
from collections import Counter

class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    if n == 0:
      return len(tasks)
    
    last = {}
    c = Counter(tasks)
    t = 1
    
    while c:
      cand = sorted((cnt, ch) for ch, cnt in c.items())
      while cand:
        _, ch = cand.pop()
        if ch not in last or t-last[ch] > n:
          c[ch] -= 1
          last[ch] = t
          if not c[ch]:
            del c[ch]
            
          # print('iter:', (ch, t))
          break
      
      t += 1
      
    return t-1
      
        