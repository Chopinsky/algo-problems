'''
1904. The Number of Full Rounds You Have Played

You are participating in an online chess tournament. There is a chess round that starts every 15 minutes. The first round of the day starts at 00:00, and after every 15 minutes, a new round starts.

For example, the second round starts at 00:15, the fourth round starts at 00:45, and the seventh round starts at 01:30.
You are given two strings loginTime and logoutTime where:

loginTime is the time you will login to the game, and
logoutTime is the time you will logout from the game.
If logoutTime is earlier than loginTime, this means you have played from loginTime to midnight and from midnight to logoutTime.

Return the number of full chess rounds you have played in the tournament.

Note: All the given times follow the 24-hour clock. That means the first round of the day starts at 00:00 and the last round of the day starts at 23:45.

Example 1:

Input: loginTime = "09:31", logoutTime = "10:14"
Output: 1
Explanation: You played one full round from 09:45 to 10:00.
You did not play the full round from 09:30 to 09:45 because you logged in at 09:31 after it began.
You did not play the full round from 10:00 to 10:15 because you logged out at 10:14 before it ended.
Example 2:

Input: loginTime = "21:30", logoutTime = "03:00"
Output: 22
Explanation: You played 10 full rounds from 21:30 to 00:00 and 12 full rounds from 00:00 to 03:00.
10 + 12 = 22.

Constraints:

loginTime and logoutTime are in the format hh:mm.
00 <= hh <= 23
00 <= mm <= 59
loginTime and logoutTime are not equal.
'''


class Solution:
  def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
    in_hh, in_mm = int(loginTime[:2]), int(loginTime[3:])
    out_hh, out_mm = int(logoutTime[:2]), int(logoutTime[3:])
    
    if out_hh < in_hh or (out_hh == in_hh and out_mm < in_mm):
      out_hh += 24
      
    # print(in_hh, in_mm, out_hh, out_mm)
    cnt = 0
    
    if in_hh < out_hh:
      # if we go across the hour line
      if in_mm > 0:
        cnt += (60 - in_mm) // 15
        in_hh += 1

      if out_mm > 0:
        cnt += out_mm // 15

      cnt += 4 * (out_hh - in_hh)
      
    elif (out_mm - in_mm) >= 15:
      # if we stay in the same hour, but only care intervals longer
      # than the 15-min game length
      cnt = out_mm//15 - (4-(60-in_mm)//15)
    
    return cnt
    