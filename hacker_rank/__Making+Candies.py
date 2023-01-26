'''
Making Candies

Karl loves playing games on social networking sites. His current favorite is CandyMaker, where the goal is to make candies.

Karl just started a level in which he must accumulate  candies starting with  machines and  workers. In a single pass, he can make  candies. After each pass, he can decide whether to spend some of his candies to buy more machines or hire more workers. Buying a machine or hiring a worker costs  units, and there is no limit to the number of machines he can own or workers he can employ.

Karl wants to minimize the number of passes to obtain the required number of candies at the end of a day. Determine that number of passes.

For example, Karl starts with  machine and  workers. The cost to purchase or hire,  and he needs to accumulate  candies. He executes the following strategy:

Make  candies. Purchase two machines.
Make  candies. Purchase  machines and hire  workers.
Make  candies. Retain all  candies.
Make  candies. With yesterday's production, Karl has  candies.
It took  passes to make enough candies.

Function Description

Complete the minimumPasses function in the editor below. The function must return a long integer representing the minimum number of passes required.

minimumPasses has the following parameter(s):

m: long integer, the starting number of machines
w: long integer, the starting number of workers
p: long integer, the cost of a new hire or a new machine
n: long integer, the number of candies to produce
Input Format

A single line consisting of four space-separated integers describing the values of , , , and , the starting number of machines and workers, the cost of a new machine or a new hire, and the the number of candies Karl must accumulate to complete the level.

Constraints

Output Format

Return a long integer denoting the minimum number of passes required to accumulate at least  candies.

Sample Input

3 1 2 12
Sample Output

3
Explanation

Karl makes three passes:

In the first pass, he makes  candies. He then spends  of them hiring another worker, so  and he has one candy left over.
In the second pass, he makes  candies. He spends  of them on another machine and another worker, so  and  and he has  candies left over.
In the third pass, Karl makes  candies. Because this satisfies his goal of making at least  candies, we print the number of passes (i.e., ) as our answer.
'''

import math

class Solution:
  '''
  the core idea is to: 1) find the sweet spot for (m, w), and 2) when to save and when to spend;

  the optimal answer is: 1) m and w needs to be as close to each other, aka balanced, as possible,
  to generate the maximum product of m*w; 2) we shall spend as early as possible, since m*w will 
  recoup the spending faster;

  with these 2 ideas, we will craft the solution: 1) if we don't have enough candies to upgrade,
  build candies until we can; 2) spend all the candies for upgrades, and distribute the upgrades
  evenly --> making value of `m` and value of `w` as close as possible; 3) repeat step 1 and 2 
  until we make enough candies;
  '''
  def minimumPasses(m, w, p, n):
    days = 0
    candies = 0
    min_days = math.ceil(n / (m * w))

    while days < min_days:
      # save candies to invest
      if p > candies:
        save_mode_days = math.ceil((p - candies) / (m * w))
        candies += save_mode_days * m * w
        days += save_mode_days

      # not gonna find a better solution, stop early
      if days >= min_days:
        break
        
      # find the middle ground to maximum production
      # efficiency
      diff = abs(m - w)
      total_upgrades = candies // p
      init_buy = min(diff, total_upgrades)

      # make (m, w) as balance as possible
      if m <= w:
        m += init_buy
      else:
        w += init_buy

      # distribute the rest evenly between m and w
      extra = total_upgrades - init_buy
      if extra > 0:
        m += extra // 2
        w += extra - (extra//2)
          
      # remaining candies = gain - cost, it could be a smaller
      # amount when we spend more to upgrade
      candies += m*w - total_upgrades*p
      days += 1
      
      # check the days to reach the target if we halt the upgrades,
      # i.e., we keep the m*w production/day rates
      min_days = min(min_days, days + math.ceil(max(n-candies, 0) / (m*w)))
    
    return min_days
