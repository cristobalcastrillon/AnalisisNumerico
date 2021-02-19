#found in: https://stackoverflow.com/questions/52996211/bisection-method-in-python
import math

def root11(x):
    return f = lambda x: (math.cos(x)**2)-x**2
    # return((x**3)-(2*x**2)+(4/3)*x-(8/27))

def bisection_method(f, a, b, tol):
    if f(a)*f(b) >= 0:
        #end function, no root.
        print("No root found.")
    else:
        iter = 0
        while (b - a)/2.0 > tol:
            midpoint = (a + b)/2.0

            if f(a)*f(midpoint) < 0: # Increasing but below 0 case
                b = midpoint
            else:
                a = midpoint

            iter += 1
        return(midpoint, iter)

answer, iterations = bisection_method(root11, -1, 2, 10**-8)
print("Answer:", answer, "\nfound in", iterations, "iterations")

# import math
# answer, iterations = bisection_method(math.cos, 0, 2, 0.0001)
# print("Answer:", answer, "\nfound in", iterations, "iterations")