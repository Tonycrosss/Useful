def fib(num):
  a = 0
  b = 1
  for _ in range(num):
    a, b = b, a + b
  return a

print(fib(10))