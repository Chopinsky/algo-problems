'''
273. Integer to English Words
'''

class Solution:
  def numberToWords(self, num: int) -> str:
    if num == 0:
      return 'Zero'
    
    ans = ''
    curr = 0
    suffix = ['', 'Thousand', 'Million', 'Billion', 'Trillion']
    base = [
      '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
      'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
      'Seventeen', 'Eighteen', 'Nineteen',
    ]
    tens = [
      '', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety',
    ]
    
    def convert(val: int) -> str:
      div, rem = divmod(val, 100)
      res = ''
      
      if div > 0:
        res = base[div] + ' ' + 'Hundred'
        
      if rem >= 20:
        t = rem // 10
        r = rem % 10
        # print('20:', t, r)
        res += (' ' if res else '') + tens[t] + (' ' if r > 0 else '') + base[r]
      elif rem > 0:
        res += (' ' if res else '') + base[rem]
      
      return res
      
    while num > 0:
      div, rem = divmod(num, 1000)
      if rem > 0:
        ans = convert(rem) + (' ' if curr > 0 else '') + suffix[curr] + (' ' if ans else '') + ans
        
      curr += 1
      num = div
      # print(div, rem)
    
    return ans
        