'''
1716. Calculate Money in Leetcode Bank

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
 
Constraints:

1 <= n <= 1000
'''


class Solution:
  def totalMoney(self, n: int) -> int:
    w, d = divmod(n, 7)
    prefix = [i for i in range(1, 8)]
    for i in range(1, 7):
      prefix[i] += prefix[i-1]
    
    total = 0
    # print(w, d, prefix)
    
    for i in range(1, w+1):
      total += prefix[-1] + (i-1)*7
    
    if d > 0:
      total += w*d + prefix[d-1]
    
    return total
        