def fib(self, n: int) -> int:
  if n <= 1:
    return n

  a, b = 0, 1
  n -= 2
  while n >= 0:
    a, b = b, a+b
    n -= 1

  return b