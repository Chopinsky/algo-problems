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
    def calc_fact(m: int) -> int:
      f = m
      for i in range(2, m):
        f = (f * i) % mod

      return f
    
    @lru_cache(None)
    def dp(rem: int, unique: int) -> int:
      if unique > rem:
        return 0
      
      if rem == 0:
        return 1
      
      if rem == unique:
        return calc_fact(rem)
      
      # if the song is played only this once in the future, it will
      # no longer be part of the future playlist again
      count = dp(rem-1, unique-1) * unique
      
      # if the song can be played again in the future, assuming
      # there're k-songs that will play next, then for each k-song
      # list, we have only `unique - k` choices available, this song
      # will remain in the future playlist
      if unique > k:
        count += dp(rem-1, unique) * (unique - k)
        
      return count % mod
      
    return dp(goal, n)
  