# Incorrect function
# len(12345)
data_string = "12345"
# Correct function
print("Length: " + str(len(data_string)))

# Type checking
print("Type: " + str(type(data_string)))

# Type conversion
print("Conversion to int: " + str(type(int(data_string))))

## Printing different types
print("Printing different types")

# Integer
print(type(12345))

# Float
print(type(123.45))

# String
print(type("12345"))

# Boolean
print(type(True))

# List
print(type([1, 2, 3]))

# Tuple
print(type((1, 2, 3)))

# Dictionary
print(type({1: "one", 2: "two", 3: "three"}))

# Set
print(type({1, 2, 3}))

# None
print(type(None))

# Complex
print(type(1 + 2j))

# Bytes
print(type(b"12345"))

# Bytearray
print(type(bytearray(5)))

# Memoryview
print(type(memoryview(bytes(5))))
