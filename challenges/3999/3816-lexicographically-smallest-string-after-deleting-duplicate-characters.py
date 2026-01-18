'''
3816-lexicographically-smallest-string-after-deleting-duplicate-characters
'''


class Solution:
  def lexSmallestAfterDeletion(self, s: str) -> str:
    rem = [0]*26
    cnt = [0]*26
    stack = []

    for ch in s:
      rem[ord(ch) - ord('a')] += 1

    # print('init:', rem)

    for ch in s:
      idx = ord(ch) - ord('a')
      rem[idx] -= 1

      while stack:
        prev = stack[-1]
        pdx = ord(prev) - ord('a')

        # can pop and get smaller string
        if prev > ch and (rem[pdx] > 0 or cnt[pdx] > 1):
          cnt[pdx] -= 1
          stack.pop()
        else:
          break

      # push to the stack
      stack.append(ch)
      cnt[idx] += 1

    # pop tail chars because empty "char" is always
    # smaller than with a char
    while stack:
      idx = ord(stack[-1]) - ord('a')

      # can pop and still have 1 char left in the string
      if cnt[idx] > 1:
        cnt[idx] -= 1
        stack.pop()
      else:
        break

    return "".join(stack)

  def lexSmallestSequence(self, s: str, l: int) -> str:
    """
    Find the lexicographically smallest subsequence of length l from string s.
    
    Args:
      s: Input string
      l: Desired length of the subsequence
    
    Returns:
      Lexicographically smallest subsequence of length l
    """
    if l <= 0:
      return ""

    if l >= len(s):
      return s
    
    stack = []
    n = len(s)
    
    for i, ch in enumerate[int, str](s):
      # While we can still form a sequence of length l and current char is smaller
      # than top of stack, pop from stack
      # We can pop if: remaining chars (n - i) + current stack size >= l
      while stack and ch < stack[-1] and (n - i) + len(stack) > l:
        stack.pop()
      
      # Push current character if we haven't reached the desired length
      if len(stack) < l:
        stack.append(ch)
    
    # Return the first l characters (in case we have more than l)
    return "".join(stack[:l])