"""
Recursion

the principle or technique of a function calling itself, in the code of f1 it calls f1
 it could make an endless loop if we're not carefull causing a stack overflow error
 you want to be a little cautios but very useful
"""

# FACTORIAL
# 9! = 9*8*7*6*5*4*3*2*1 = 362880
# 9! = 9*8! = 9*8*7! = ... = 362880

n = 7

def factorial_iterative(n):
    factorial = 1
    for i in range(2, n+1):
        factorial *= i
    return factorial

print(factorial_iterative(n))

fact = 1
while n > 0:
    fact = fact*n
    n -= 1

print(fact)

def factorial_recursive(n):
    if n < 1:
        return 1
    else:
        number = n*factorial_recursive(n-1)
        return number

print(factorial_recursive(7))


"""
Recursion is not necessarily faster than the iterative version
"""

# FIBONACCI
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

print(fibonacci(350))

def fibonacci2(n):
    if n <= 1:
        return n
    return (fibonacci2(n-1) + fibonacci2(n-2))

print(fibonacci2(350))

# RecursionError: maximum recursion depth exceeded in comparison - StackOverflow
#  it's an exponential runtime complexity, takes forever

# n = 350: 6254449428820551641549772190170184190608177514674331726439961915653414425
# recursive one slow af