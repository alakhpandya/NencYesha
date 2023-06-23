def func1():
    """This will do ______ things"""
    pass

# Some useful built-in function

# sum
"""
l1 = [12, 13, 15, 21, 32, -50, 20]
print(sum(l1))
"""
# abs
"""
x = -5
print(abs(x))
y = 10
print(abs(y))
"""
# any & all
"""
l1 = [3 < 5, 4 >= 6, 12 > 10, 11 < 8]
print(l1)
print(any(l1))
print(all(l1))
"""
# chr - returns character corresponding to the ascii code
'''
s = """
print(chr(98))
print(chr(66))
print(s.upper())
"""
'''
# eval
"""
s = 'print("Hello World!")'
print(s)
eval(s)
"""

# round
"""
a = 25.3
print(round(a))
b = 33.8
print(round(b))
pi = 3.141596
print(round(pi, 2))
"""

# zip
"""
l1 = ["a", "b", "c"]
l2 = [1, 2, 3]
l3 = ["p", "q", "r"]
a = zip(l1, l2, l3)
print(list(a))
"""

# lambda functions
'''
def python():
    print("""Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.""")
'''
'''
python = lambda : print("""Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation via the off-side rule.""")

python()
'''
"""
def power5(x):
    return x ** 5

power5 = lambda x : x ** 5
y = power5(4)
print(y)
"""
"""
def avg(a, b):
    return (a + b)/2

avg = lambda a, b : (a + b)/2
print(avg(10, 20))
"""

# We can convert a function to a lambda function only if it is a 'one-liner' function

# map
def factorial(a):
    f = 1
    for i in range(1, a+1):
        f = f * i
    return f

# print(factorial(5))
num = [2, 4, 5, 8, 9, 6]
num_fact