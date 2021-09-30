def gcd(a: int, b: int) -> int:
  if a > b:
    a, b = b, a
    
  while b:
    a, b = b, a%b

  return a
