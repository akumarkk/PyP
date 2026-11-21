def add(a, b):
    return a + b

def subs(a,b):
  return a-b

def mul(a,b):
   print(a,b)
   if a == 0 or b == 0:
       return 0
   return a*b

print(add(2, 3))
print(subs(5, 2))
print(mul(3, 4))