'''
Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.


In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.

For example, to add the letter 's', Alice has to press '7' four times. Similarly, to add the letter 'k', Alice has to press '5' twice.
Note that the digits '0' and '1' do not map to any letters, so Alice does not use them.
However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.

For example, when Alice sent the message "bob", Bob received the string "2266622".
Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.

Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: pressedKeys = "22233"
Output: 8
Explanation:
The possible text messages Alice could have sent are:
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae", and "ce".
Since there are 8 possible messages, we return 8.

Example 2:

Input: pressedKeys = "222222222222222222222222222222222222"
Output: 82876089
Explanation:
There are 2082876103 possible text messages Alice could have sent.
Since we need to return the answer modulo 109 + 7, we return 2082876103 % (109 + 7) = 82876089.

Constraints:

1 <= pressedKeys.length <= 10^5
pressedKeys only consists of digits from '2' - '9'.
'''


class Solution:
  def countTexts(self, keys: str) -> int:
    n = len(keys)
    dp = [0] * n
    p = { 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 4, 8: 3, 9: 4, }  
    mod = 10**9 + 7
    
    for i in range(n):
      d = int(keys[i])
      dp[i] = dp[i-1] if i > 0 else 1
      # print(i, keys[i], p[d])
      
      for j in range(1, p[d]):
        k = i-j
        if k < 0 or keys[k] != keys[i]:
          break
          
        dp[i] += dp[k-1] if k > 0 else 1
          
      dp[i] = dp[i] % mod
    
    # print(dp)
    return dp[-1]
  