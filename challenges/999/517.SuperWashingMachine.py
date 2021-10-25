'''
You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.

For each move, you could choose any m (1 <= m <= n) washing machines, and pass one dress of each washing machine to one of its adjacent washing machines at the same time.

Given an integer array machines representing the number of dresses in each washing machine from left to right on the line, return the minimum number of moves to make all the washing machines have the same number of dresses. If it is not possible to do it, return -1.

Example 1:

Input: machines = [1,0,5]
Output: 3
Explanation:
1st move:    1     0 <-- 5    =>    1     1     4
2nd move:    1 <-- 1 <-- 4    =>    2     1     3
3rd move:    2     1 <-- 3    =>    2     2     2

Example 2:

Input: machines = [0,3,0]
Output: 2
Explanation:
1st move:    0 <-- 3     0    =>    1     2     0
2nd move:    1     2 --> 0    =>    1     1     1

Example 3:

Input: machines = [0,2,0]
Output: -1
Explanation:
It's impossible to make all three washing machines have the same number of dresses.

Constraints:

n == machines.length
1 <= n <= 10^4
0 <= machines[i] <= 10^5
'''


class Solution:
  def findMinMoves(self, machines: List[int]) -> int:
    total = sum(machines)
    n = len(machines)
    if total % n != 0:
      return -1
    
    target = total // n
    cnt = 0
    steps = 0
    
    for machine in machines:
      diff = machine - target
      cnt += diff
      steps = max(steps, abs(cnt), abs(diff))
      
    return steps
  
  
  def findMinMoves1(self, machines: List[int]) -> int:
    total = sum(machines)
    n = len(machines)
    if total % n != 0:
      return -1
    
    target = total // n
    steps, carryover, takers = 0, 0, 0
    
    for i, val in enumerate(machines):
      if val == target:
        continue
        
      # section ends here, let's check how many steps are needed
      # to fill this section, with carryovers, providers, and offerings
      # from next sections
      if val > target:
        providers = val - target
        # print(i, val, providers, takers, carryover)
        
        if carryover >= 0:
          # left section(s) has more to offer, we need to let
          # these extra offers to fill the openings in this 
          # section first, and spill over to the next section
          # with anything left
          
          if carryover >= takers:
            # spill over is destined, whatever from the left after
            # filling the openings from the curren sector, plus
            # what the section provider offers
            steps = max(steps, providers+carryover-takers)
            
          elif providers+carryover <= takers:
            # carryover can't fill all the openings, but the providers
            # won't be able to fill the remainder, need offerings from
            # next sections, i.e. whichever is larger, the carryover
            # portion, or the portion from the provider and offerings
            # from the next sections
            steps = max(steps, takers-carryover, carryover)
            
          else:
            # carryover can't fill all the openings, but the providers
            # has more to offer than needed for the remainder openings.
            # then the steps are the whichever needs more steps to finish,
            # the carryover portion or the provider portion
            steps = max(steps, carryover, providers)
          
        else:
          # easier case -- more to the left that we need to provide
          # from the current provider or beyond in this section, just
          # check which is larger: the openings to the left, or the 
          # amount we need to offer from the current provider
          steps = max(steps, takers-carryover, providers)
        
        carryover += providers - takers
        providers, takers = 0, 0
        # print(i, carryover, steps)
      
      else:
        takers += target - val
        
    return steps
    
