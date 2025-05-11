# Keyword arguments
def calculate(n, **kwargs):
  n += kwargs["add"]
  n *= kwargs["multiply"]
  print(n)
  # print(kwargs)
  # for key,value in kwargs.items():
  #   print(key)



calculate(2, add=3, multiply=5)