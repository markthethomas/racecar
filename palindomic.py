import string
digs = string.digits + string.lowercase

def int2base(x, base):
  if x < 0: sign = -1
  elif x==0: return '0'
  else: sign = 1
  x *= sign
  digits = []
  while x:
    digits.append(digs[x % base])
    x /= base
  if sign < 0:
    digits.append('-')
  digits.reverse()
  return int(''.join(digits))


def palinDromada(n):
    for base in range(2,32,1):
        convertedInt = int2base(n, base)
        if str(convertedInt) == str(convertedInt)[::-1]:
            return base


palinDromada(2)

