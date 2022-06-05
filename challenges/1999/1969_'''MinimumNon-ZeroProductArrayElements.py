class Solution:
  '''
  this is just a math problem -- we need to make all the pairs to be (1, 2**p-2), that will 
  minimize the final products
  '''
  def minNonZeroProduct(self, p: int) -> int:
    return (pow(2**p - 2, 2**(p-1) - 1, 10**9 + 7) * (2**p - 1)) % (10**9 + 7)
