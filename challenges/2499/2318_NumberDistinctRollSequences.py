'''
You are given an integer n. You roll a fair 6-sided dice n times. Determine the total number of distinct sequences of rolls possible such that the following conditions are satisfied:

The greatest common divisor of any adjacent values in the sequence is equal to 1.
There is at least a gap of 2 rolls between equal valued rolls. More formally, if the value of the ith roll is equal to the value of the jth roll, then abs(i - j) > 2.
Return the total number of distinct sequences possible. Since the answer may be very large, return it modulo 109 + 7.

Two sequences are considered distinct if at least one element is different.

Example 1:

Input: n = 4
Output: 184
Explanation: Some of the possible sequences are (1, 2, 3, 4), (6, 1, 2, 3), (1, 2, 3, 1), etc.
Some invalid sequences are (1, 2, 1, 3), (1, 2, 3, 6).
(1, 2, 1, 3) is invalid since the first and third roll have an equal value and abs(1 - 3) = 2 (i and j are 1-indexed).
(1, 2, 3, 6) is invalid since the greatest common divisor of 3 and 6 = 3.
There are a total of 184 distinct sequences possible, so we return 184.
Example 2:

Input: n = 2
Output: 22
Explanation: Some of the possible sequences are (1, 2), (2, 1), (3, 2).
Some invalid sequences are (3, 6), (2, 4) since the greatest common divisor is not equal to 1.
There are a total of 22 distinct sequences possible, so we return 22.

Constraints:

1 <= n <= 10^4
'''

class Solution:
  '''
  the hidden trick is that for each roll # >= 4, only 66 valid states exist for the 
  last 4 rolls of all valid rolls, and each valid tail-rolls-state can lead to at most
  2 ~ 5 other valid tail-rolls-state, hence we can update the state space with sort of
  the brutal force method -- check each state, and update the state counts for the next
  state. Run time is O(66 * n)

  there's a faster algorith that runs at O(66 * log(n)), as we can build the state 
  transition matrix (i.e. a 66x66 matrix), and then use power-multiply to get the total
  transition matrix (i.e. something like pow(mat, n-4, mod), but you might need
  to implement the matrix version of it), and then multiply the final matrix with the 
  base case with tail-rolls-state at roll #4 to obtain the final state numbers, sum the 
  state numbers to get the final answer.

  this algo is not trivial to implement though, since we need to map tail-rolls-state
  to a state array, create the states-transition-matrix, then implement the power-multiply
  algo to do the matrix power-multiplications. Worth at least a full day of work if you'd 
  want to do it right, i.e. only if you're getting paid to do it :) 
  '''
  def distinctSequences(self, n: int) -> int:
    mod = 10**9 + 7
    roll = {
      1: [2,3,4,5,6],
      2: [1,3,5],
      3: [1,2,4,5],
      4: [1,3,5],
      5: [1,2,3,4,6],
      6: [1,5],
    }
    
    stack, nxt = {(1,):1, (2,):1, (3,):1, (4,):1, (5,):1, (6,):1}, {}
    r = 1
    
    # keep rolling
    while r < n:
      for curr_roll, cnt in stack.items():
        for dice in roll[curr_roll[-1]]:
          if dice in curr_roll:
            continue
            
          nxt_roll = (curr_roll[1:] if len(curr_roll) >= 2 else curr_roll) + (dice, )
          nxt[nxt_roll] = (nxt.get(nxt_roll, 0) + cnt) % mod
      
      stack, nxt = nxt, stack
      nxt.clear()
      r += 1
      
    return sum(stack.values()) % mod
    