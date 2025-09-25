'''
166-fraction-to-recurring-decimal
'''


class Solution:
  def fractionToDecimal(self, numerator: int, denominator: int) -> str:
    if numerator == '0':
      return '0'

    if denominator == '1':
      return numerator

    vn = int(numerator)
    vd = int(denominator)
    is_neg = False

    if (vn < 0 and vd > 0) or (vn > 0 and vd < 0):
      is_neg = True

    vn = abs(vn)
    vd = abs(vd)
    d = vn // vd
    r = vn % vd
    stack = []
    seen = {}

    while r > 0 and r not in seen:
      seen[r] = len(stack)
      r *= 10
      # print('stack:', r, vd, r%vd)

      if r % vd == 0:
        stack.append(str(r//vd))
        r = 0
        break

      if r < vd:
        stack.append('0')
        continue

      val = r//vd
      r = r%vd
      stack.append(str(val))
      
    if not stack:
      frac = ''
    elif r > 0 and r in seen:
      frac = '.' + ''.join(stack[:seen[r]]) + '(' + ''.join(stack[seen[r]:]) + ')' 
    else:
      frac = '.' + ''.join(stack)

    return ('-' if is_neg else '') + str(d) + frac
