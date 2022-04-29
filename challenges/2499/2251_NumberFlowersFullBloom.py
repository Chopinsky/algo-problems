'''
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array persons of size n, where persons[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

Example 1:

Input: flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
Example 2:

Input: flowers = [[1,10],[3,3]], persons = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

Constraints:

1 <= flowers.length <= 5 * 10^4
flowers[i].length == 2
1 <= starti <= endi <= 10^9
1 <= persons.length <= 5 * 10^4
1 <= persons[i] <= 10^9
'''

from typing import List


class Solution:
  def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
    evt = []
    
    for s, e in flowers:
      evt.append((s, 0, 1))
      evt.append((e, 2, -1))
      
    for i, t in enumerate(persons):
      evt.append((t, 1, i))
      
    evt.sort()
    # print(evt)
    f = 0
    cnt = 0
    ans = [0] * len(persons)
    
    for _, typ, data in evt:
      if typ != 1:
        f += data
        continue
        
      ans[data] = f
      cnt += 1
      if cnt == len(persons):
        break
          
    return ans
  