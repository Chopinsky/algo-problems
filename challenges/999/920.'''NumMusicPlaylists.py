'''
Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

Every song is played at least once.
A song can only be played again only if k other songs have been played.
Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.

Example 1:

Input: n = 3, goal = 3, k = 1
Output: 6
Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
Example 2:

Input: n = 2, goal = 3, k = 0
Output: 6
Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
Example 3:

Input: n = 2, goal = 3, k = 1
Output: 2
Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].

Constraints:

0 <= k < n <= goal <= 100
'''


from functools import lru_cache


class Solution:
  '''
  idea is to build the counter from (rem, unique) pair and up -> i.e. a bottom
  up approach, and for the next song, it can be: a song that's been played
  for the last time and kicked out of the playlist, or it is played again in the future.
  '''
  def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
    mod = 10**9 + 7
    
    @lru_cache(None)
    def dp(rem: int, not_played: int) -> int:
      if rem == 0:
        return 1 if not_played == 0 else 0
      
      if rem == not_played:
        cnt = 1
        while rem > 1:
          cnt = (cnt * rem) % mod
          rem -= 1
          
        return cnt
        
      if rem < not_played:
        return 0
        
      # play a song from the `not_played` list
      cnt = (not_played * dp(rem-1, not_played-1)) % mod
      
      # choose a song from the played list
      if n - not_played > k:
        cnt = (cnt + (n - not_played - k) * dp(rem-1, not_played)) % mod
      
      return cnt

    return dp(goal, n)
        
  