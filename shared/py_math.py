def fib(self, n: int) -> int:
  if n <= 1:
    return n

  a, b = 0, 1
  n -= 2
  while n >= 0:
    a, b = b, a+b
    n -= 1

  return b


def reverse(x):
    ans = 0

    while x:
      ans = 10 * ans + x % 10
      x //= 10

    return ans


def is_palin(x):
    return x == reverse(x)