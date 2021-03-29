def PointFixe (g,x0,epsilon,Nitermax): 
    xold = x0
    xnew = g(xold)
    n = 1

    while abs (xnew - xold) > epsilon and n < Nitermax :
        xold = xnew
        xnew = g(xold)
        n = n+1
    return xnew, n, abs(xnew - xold)
   
from math import sin

def g1(x):
    return (x ** 4 - 9) / 3