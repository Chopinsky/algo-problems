'''
Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array stones, where stones[i] is the value of the ith stone.

Alice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

Assuming both players play optimally, return true if Alice wins and false if Bob wins.

 

Example 1:

Input: stones = [2,1]
Output: true
Explanation: The game will be played as follows:
- Turn 1: Alice can remove either stone.
- Turn 2: Bob removes the remaining stone. 
The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.
Example 2:

Input: stones = [2]
Output: false
Explanation: Alice will remove the only stone, and the sum of the values on the removed stones is 2. 
Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.
Example 3:

Input: stones = [5,1,2,4,3]
Output: false
Explanation: Bob will always win. One possible way for Bob to win is shown below:
- Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
- Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
- Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
- Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
- Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.

Constraints:

1 <= stones.length <= 10^5
1 <= stones[i] <= 10^4
'''

from functools import lru_cache
from typing import List, Tuple


class Solution:
  def stoneGameIX(self, stones: List[int]) -> bool:
    res = [0] * 3 # resource
    for value in stones:
      res[value % 3] += 1

    majority = max(res[1], res[2])
    minority = min(res[1], res[2])

    if majority-minority <= 2 and res[0] % 2 == 1:
      return False
    
    if minority == 0 and res[0] % 2 == 0:
      return False

    return True
      

  def stoneGameIX0(self, stones: List[int]) -> bool:
    counter = [0] * 3
    for s in stones:
      counter[s%3] += 1
    
    # print('original:', counter)
      
    # only 3s, alice is doomed
    if (not counter[1] and not counter[2]) or sum(counter) <= 1:
      return False
    
    if sum(counter) == 2:
      return True if (counter[1] == 1 and counter[2] == 1) else False
    
    @lru_cache(None)
    def dp(curr: int, rem: Tuple[int, int, int]) -> bool:
      rem = list(rem)
      print('src', curr, rem)
      
      # if a draws 3, b also draws 3 if possible, as 3 is a free-pass
      if rem[0] >= 2:
        rem[0] %= 2
    
      # if a draws 1/2, b follows with a 2/1 if possible, this is resetting 
      # and doesn't affecting the end results
      if rem[1] > 0 and rem[2] > 0:
        low = min(rem[1], rem[2])
        rem[1] -= low
        rem[2] -= low
        
      # print('reduced:', curr, rem)

      # whatever the remaining stone is, alice will lose -- by either 
      # get a 3, or running out of the stones
      if sum(rem) <= 1:
        return False
      
      # edge case -- only 2 stones left, the only way for a to win is to
      # have 2 remaining stones with the color of the running sum
      if sum(rem) == 2:
        return True if (rem[curr] == 2) or (rem[0] == 1 and rem[3-curr] == 1) else False
      
      # now considering edge cases
      one = False
      two = False
      
      # running sum is 1
      if curr == 1:
        # a takes 1 but b doesn't have 3 to take, or a takes 3 but b 
        # doesn't have 1 to take, b loses
        if (rem[1] > 0 and not rem[0]) or (not rem[1] and rem[0] > 0):
          return True
        
        # a takes either 1 or 3, and b takes 3 or 1 as a response
        one = dp(2, (rem[0]-1, rem[1]-1, rem[2]))
        
      # running sum is 2
      else:
        # a takes 2 but b doesn't have 3 to take, or a takes 3 but a
        # doesn't have 2 to take, b loses
        if (rem[2] > 0 and not rem[0]) or (not rem[2] and rem[0] > 0):
          return True
        
        # a takes either 2 or 3, and b takes 3 or 2 as a response
        two = dp(1, (rem[0]-1, rem[1], rem[2]-1))
        
      return one or two
    
    # init case
    one = False
    two = False

    # a takes 1
    if counter[1]:
      # b doesn't have a solution 
      if not counter[0] and counter[1] == 1:
        return True
      
      # b takes 1 as well
      if counter[1] > 1:
        one = one or dp(2, (counter[0], counter[1]-2, counter[2]))

      # b takes 3
      if counter[0] > 0 and not one:
        one = one or dp(1, (counter[0]-1, counter[1]-1, counter[2]))

    # a takes 2
    if counter[2]:
      # b doesn't have a solution 
      if not counter[0] and counter[2] == 1:
        return True
      
      # b takes 2 as well
      if counter[2] > 1:
        two = two or dp(1, (counter[0], counter[1], counter[2]-2))
        
      # b takes 3
      if counter[0] > 0 and not two:
        two = two or dp(2, (counter[0]-1, counter[1], counter[2]-1))

    # print("final:", one, two)
    return (one or two)
  