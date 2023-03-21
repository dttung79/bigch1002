# Data type
a = 5    # int
b = 5.1234  # float
c = '5'  # str
d = True # bool
print(a, b, c, d, sep='----')
print(type(a), type(b), type(c), type(d), sep='----')

s = 'Hello World'
print(f'|{s:25}|')
print(f'|{a:25}|')
print(f'|{s:>25}|')
print(f'|{a:<25}|')
print(f'|{a:^25}|')
print(f'|{b:<25.2f}|')

print('|{0:>25}|'.format(s))
print('|{0:>25.2f}|'.format(b))


# Arithmetic operators: +, -, *, /, //, %, **
a = 4
b = 2
print(f'{a} + {b} = {a + b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b}')       # true division
print(f'{a} // {b} = {a // b}')     # floor division
print(f'{a} % {b} = {a % b}')       # modulus
print(f'{a}^{b} = {a ** b}')        # exponent
print(f'sqrt({a}) = {a ** 0.5}')    # square root

# Comparison operators: ==, !=, >, <, >=, <=

# Boolean operators: and, or, not
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)

# Conditional statements: if, elif, else
a = int(input('Enter a: '))
if a > 0:
    print('a is positive')
elif a < 0:
    print('a is negative')
else:
    print('a is zero')

print('a is positive' if a > 0 else 'a is negative' if a < 0 else 'a is zero')

a = 5
b = 10
if a > b:
    m = a
else:
    m = b

m = a if a > b else b # m = a > b ? a : b (Java/C#)