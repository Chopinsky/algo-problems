class Solution8:
  def test(self):
    print("Testing problem 8:")

    assert self.solve("42") == 42, "Test case 1 failed"
    assert self.solve("   -42") == -42, "Test case 2 failed"
    assert self.solve("4193 with words") == 4193, "Test case 3 failed"
    assert self.solve("words and 987") == 0, "Test case 4 failed"
    assert self.solve("-91283472332") == -2147483648, "Test case 5 failed"

    print("All passed")


  def solve(self, s: str) -> int:
    if len(s) == 0:
      return 0

    s = s.strip()
    sign = 1
    ans = 0

    upper = 2 ** 31 - 1
    lower = -2 ** 31


    for i, ch in enumerate(s):
      if i == 0 and (ch == '+' or ch == '-'):
        sign = -1 if (ch == '-') else 1
        continue

      # illegal case
      if ch < '0' or ch > '9':
        break

      # print(int(ch))
      ans = ans * 10 + int(ch)

      if sign * ans < lower:
        return lower

      if sign * ans > upper:
        return upper

    return sign * ans