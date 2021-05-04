'''
A certain bug's home is on the x-axis at position x. Help them get there from position 0.

The bug jumps according to the following rules:

It can jump exactly a positions forward (to the right).
It can jump exactly b positions backward (to the left).
It cannot jump backward twice in a row.
It cannot jump to any forbidden positions.
The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.

Example 1:

Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.

Example 2:

Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
Output: -1

Example 3:

Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
Output: 2
Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.

Constraints:

1 <= forbidden.length <= 1000
1 <= a, b, forbidden[i] <= 2000
0 <= x <= 2000
All the elements in forbidden are distinct.
Position x is not forbidden.
'''

class Solution:
  def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
    if x == 0:
      return 0

    dp = [math.inf] * (max(x, max(forbidden)) + a + b + 1)
    dp[0] = 0

    for pos in forbidden:
      dp[pos] = -1

    stack = deque([0])

    while len(stack) > 0:
      pos = stack.popleft()
      step = dp[pos]

      # at home, done
      if pos == x:
        continue

      # if we won't get home with a better solution, done.
      if dp[x] > 0 and step >= dp[x]:
        continue

      # we can reach the target with 1 more back jump, done.
      if pos-b == x and dp[x] > step+1:
        dp[x] = step+1
        continue

      # if jump forward won't land on a forbidden node
      if pos+a < len(dp) and dp[pos+a] > dp[pos] + 1:
        stack.append(pos+a)
        dp[pos+a] = dp[pos] + 1

      # jump back is tricky: only legal case is jump back and then jump
      # forward as well, then all future jumps can be legal.
      # !!important!! both nodes in the path -- `pos-b` and `pos-b+1` must
      # all be reachable, meaning they should not be a forbidden node, and
      # the steps to reach them shall be higher than the current path.
      if pos-b > 0 and pos-b+a < len(dp) and dp[pos-b] > dp[pos] + 1 and dp[pos-b+a] > dp[pos] + 2:
        stack.append(pos-b+a)
        dp[pos-b+a] = dp[pos] + 2

    return dp[x] if dp[x] < math.inf else -1
