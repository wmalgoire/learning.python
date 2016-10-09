''' Demo of different syntax to import standard library module/function '''

# 1: import module
# 2: from module import function
# 3: from module import function as alias

from math import sqrt as sqroot

print(sqroot(81))
