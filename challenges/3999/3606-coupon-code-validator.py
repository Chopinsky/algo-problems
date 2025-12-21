'''
3606-coupon-code-validator
'''

from typing import List


class Solution:
  def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
    allowed_line = set(['electronics', 'grocery', 'pharmacy', 'restaurant'])

    def is_valid_code(s: str) -> bool:
      if not s:
        return False

      for ch in s:
        if '0' <= ch <= '9' or 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or ch == '_':
          continue

        return False

      return True

    def is_valid_bl(l: str) -> bool:
      return l in allowed_line

    ans = []
    for i in range(len(code)):
      if is_valid_code(code[i]) and is_valid_bl(businessLine[i]) and isActive[i]:
        ans.append((businessLine[i], code[i]))

    return [t[1] for t in sorted(ans)]
        