# The sign outside reads: Name no one man.

# "Escape. We must escape." Staring at the locked door of his cage, Beta Rabbit, spy and brilliant mathematician, has a
# revelation. "Of course! Name no one man - it's a palindrome! Palindromes are the key to opening this lock!"

# To help Beta Rabbit crack the lock, write a function answer(n) which returns the smallest positive integer base b, at least 2, in
# which the integer n is a palindrome. The input n will satisfy "0 <= n <= 1000."


# Test cases
# ==========

# smallest positive integer base b, at least 2, integer n is palindrome

# Inputs:
#     (int) n = 0
# Output:
#     (int) 2
#
# Inputs:
#     (int) n = 42
# Output:
#     (int) 4


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

