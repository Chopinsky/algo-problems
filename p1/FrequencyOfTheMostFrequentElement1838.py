class Solution1838:
  def test(self):
    cases = [
      [[1,2,4], 5, 3,],
      [[1,4,8,13], 5, 2,],
      [[3,9,6], 2, 1],
    ]

    print("Testing problem 1838:\n")
    template = "Expected: {};\nGet:      {};"

    for _, c in enumerate(cases):
      ans = self.solve(c)
      print("Test case: {}, {}".format(c[0], c[1]))
      print(template.format(c[2], ans) + "\n")

    print("Done!\n")


  def solve(self, case) -> int:
    [src, k, _] = case
    src.sort()
    # print(src, k)

    count = 1
    if k == 0 or len(src) <= 1:
      return min(len(src), count)

    l, r = 0, 0
    while l < len(src):
      while k >= 0 and r < len(src)-1:
        r += 1
        k -= (src[r] - src[r-1]) * (r - l)

        if k >= 0 and r-l+1 > count:
          count = r-l+1

      k += src[r] - src[l]
      l += 1

      if k >= 0 and r-l+1 > count:
        count = r-l+1

    return count
