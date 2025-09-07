'''
3677-count-binary-palindromic-numbers
'''


class Solution:
  def countBinaryPalindromes(self, n: int) -> int:
    if n == 0:
      return 1

    count = 1
    arr = [int(i) for i in bin(n)[2:]]
    n = len(arr)

    # all pal that's smaller than n-len
    for k in range(1, n):
      count += 1 << ((k+1)//2 - 1)

    half = (n+1) // 2
    for i in range(1, half):
      if arr[i] == 1:
        count += 1 << (half-i-1)

    # n is pal
    if arr[:half][::-1] <= arr[-half:]:
      count += 1

    return count
    

