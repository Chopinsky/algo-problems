'''
3295-report-spam-message
'''

from typing import List


class Solution:
  def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
    count = 0
    banned = set(bannedWords)

    for w in message:
      if w in banned:
        count += 1

      if count >= 2:
        return True

    return False
        