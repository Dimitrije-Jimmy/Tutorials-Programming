def bisection_method(func, a, b, error_accept):
    """
    This function solves for an unknown root of a non-linear function given the function, 
    the initial root boundaries, and an acceptable level of error
    
    Parameters:
    ------------------------
    :param func: The user defined function, which needs to be entered as a string.
    :param a: The initial lower root boundary.
    :param b: The initial upper root boundary.
    :param error_accept: The user's acceptable level of error.
    
    Returns:
    ------------------------
    :return The root boundaries and the error at the final iteration. 
    """
    
    def f(x):
        f = eval(func)
        return f
    
    error = abs(b - a)
    
    while error > error_accept:
        c = (b + a) / 2
        
        if f(a) * f(b) >= 0:
            print("No root or multiple roots present, therefore, the bisection method will not work!")
            quit()
            
        elif f(c) * f(a) < 0:
            b = c
            error = abs(b - a)
            
        elif f(c) * f(b) < 0:
            a = c
            error = abs(b - a)
            
        else:
            print("something went wrong")
            quit()
            
    print(f"The error is {error}")
    print(f"The lower boundary, a, is {a} and the upper boundary, b, is {b}")
    

# to call our functions description
print(bisection_method.__doc__)

bisection_method("(4*x ** 3) + 3*x - 3", 0, 1, 0.05)

bisection_method("(3*x ** 2) - 4", -2, 0, 0.05)

