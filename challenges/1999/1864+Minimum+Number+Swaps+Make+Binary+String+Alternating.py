'''
1864. Minimum Number of Swaps to Make the Binary String Alternating

Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.

The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.

Any two characters may be swapped, even if they are not adjacent.

Example 1:

Input: s = "111000"
Output: 1
Explanation: Swap positions 1 and 4: "111000" -> "101010"
The string is now alternating.
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating, no swaps are needed.
Example 3:

Input: s = "1110"
Output: -1
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
'''

class Solution:
  def minSwaps(self, s: str) -> int:
    n = len(s)
    pos = set(i for i in range(n) if s[i] == '1')
    ones = len(pos)
    zeros = n - ones
    
    if abs(ones-zeros) > 1:
      return -1

    # print('init:', pos)
    def count(i: int):
      swaps = 0
      for j in range(i, n, 2):
        if j not in pos:
          swaps += 1
          
      return swaps
    
    if ones == zeros:
      return min(count(0), count(1))
    
    return count(0) if ones > zeros else count(1)
        