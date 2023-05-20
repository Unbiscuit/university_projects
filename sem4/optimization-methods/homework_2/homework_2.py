import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
import pandas as pd

L = 15.06250253103967 # found with findL
eps = 1/np.power(10, 6) 
delta = 0.25

def function(x: float) -> float:
    fi = 1/14*np.abs(4 - x)*(1/2*np.abs(x + 2) - 1)*(3*np.abs(1/4*x + 5) + 1)
    return fi


def findL(a, b): 
    x = a
    maxy = derivative(function, x)
    while x <= b:
        x += eps
        y = derivative(function, x)
        if y > maxy:
            maxy = y

    return maxy


def broken_lines_method(left_boundary: float, right_boundary: float) -> float:
    xn = []
    po = []
    thing = []
    lx = []
    rx = []
    pn = []

    x0 = 1/(2*L) * (function(left_boundary) - function(right_boundary) + L*(left_boundary + right_boundary))
    p = 1/2 * (function(left_boundary) + function(right_boundary) + L*(left_boundary-right_boundary))

    delta = 1/(2*L)*(function(x0) - p)
    while 2*L*delta > eps:
        xn.append(x0)
        po.append(p)
        thing.append(2*L*delta)
        x1 = x0 - delta
        lx.append(x1)
        x2 = x0 + delta
        rx.append(x2)

        if function(x1) < function(x2):
            x0 = x1
        else:
            x0 = x2

        p = (1/2)*(function(x0) + p)
        pn.append(p)
        delta = 1/(2*L)*(function(x0) - p)

    df = pd.DataFrame({'xn': xn,
                   "p*n": po,
                   '2*L*DELTA': thing,
                   "x'n": lx,
                   "x''n": rx,
                   "pn": pn})
    df.to_excel('/home/uncookie/Documents/university_projects/sem4/optimization-methods/homework_2/broken_lines.xlsx', index=True)


    return x0


def phi(x):
    it = ((x-4)**2 - 1)*((x+3)**2 + 1)
    return it


def dxphi(x):
    it = x**4 - 2*x**3 - 23*x**2 + 10*x + 150
    return it


def dxdxphi(x):
    it = 4*x**3 - 6*x**2 - 23*x + 10
    return it


def newton_raphson_method():
    xn = []
    dxfoo = []
    dxdxfoo = []
    alpha = []

    x = 10
    a = 1
    while (phi(x) > eps):
        xn.append(x)
        dxfoo.append(dxphi(x))
        dxdxfoo.append(dxdxphi(x))
        p = -dxphi(x)/dxdxphi(x)
        while (phi(x + a*p) > phi(x) + delta*a*p*dxphi(x)): a /= 2
        alpha.append(a)
        x = x + a*p 

    df = pd.DataFrame({'xn': xn,
                   "f'": dxfoo,
                   'f''': dxdxfoo,
                   'a': alpha})
    df.to_excel('/home/uncookie/Documents/university_projects/sem4/optimization-methods/homework_2/newton.xlsx', index=True)

    return x


def main():
    a = -20
    b = 10

    x = broken_lines_method(a, b)
    y = phi(x)

    print(f'x = {x}, y = {y}')

    c = -10
    d = 10
    
    x = np.arange(a, b, 0.1)
    plt.plot(x, phi(x))
    plt.show()

if __name__ == "__main__":
    main()
