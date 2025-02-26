'''
3403-find-the-lexicographically-largest-string-from-the-box-i
'''


class Solution:
  def answerString(self, word: str, numFriends: int) -> str:
    n = len(word)
    m = n - numFriends + 1
    if numFriends == 1:
      return word

    return max(word[i:i+m] for i in range(n))
