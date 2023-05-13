import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.misc import derivative

x_i = (0, 1, 2, 3, 4)
y_i = (0, -1, -2, -3, -4)

global_a = 100
global_b = -100

def foo1(a, b):
    equation = 0
    for i in range(5):
        equation += np.power(a*x_i[i] + b - y_i[i], 2)
    return equation

from scipy.misc import derivative

def partial_derivative(func, var=0, point=[]):
    args = point[:]
    def wraps(x):
        args[var] = x
        return func(*args)
    return derivative(wraps, point[var], dx = 1e-6)


def dxfoo1(z):
    a, b = z
    equation = 60*a + 20*b + 60
    return equation


def dyfoo1(z):
    a, b = z
    equation = 10*b + 20*a + 20
    return equation


def dxdxfoo1():
    return 60


def dydyfoo1():
    return 10


def dxdyfoo1():
    return 20

def vectorized_foo1(z):
    a, b = z
    equation = 0
    for i in range(5):
        equation += np.power(a*x_i[i] + b - y_i[i], 2)
    return equation


def foo1_fixed1(a):
    return foo1(a=a, b=global_b)


def foo1_fixed2(b):
    return foo1(a=global_a, b=b)


def fii1(gamma):
    global a0, g1
    equation = vectorized_foo1(a0 - gamma*g1)
    return equation


def foo2(a, b):
    equation = 0
    for i in range(5):
        equation += np.abs(a*x_i[i] + b - y_i[i])
    return equation


def vectorized_foo2(z):
    a, b = z
    equation = 0
    for i in range(5):
        equation += np.abs(a*x_i[i] + b - y_i[i])
    return equation


def fii2(gamma):
    global a0, g1
    equation = vectorized_foo2(a0 - gamma*g1)
    return equation


def dxfoo2(z):
    x, y = z
    equation = ((((x+y+1)*np.abs(2*x+y+2)+(4*x+2*y+4)*np.abs(x+y+1))*np.abs(3*x+y+3)+(9*x+3*y+9)*np.abs(x+y+1)*np.abs(2*x+y+2))*np.abs(4*x+y+4)+(16*x+4*y+16)*np.abs(x+y+1)*np.abs(2*x+y+2)*np.abs(3*x+y+3))/(np.abs(x+y+1)*np.abs(2*x+y+2)*np.abs(3*x+y+3)*np.abs(4*x+y+4))
    return equation


def dyfoo2(z):
    x, y = z
    equation = ((((y*np.abs(y+x+1)+(y+x+1)*np.abs(y))*np.abs(y+2*x+2)+(y+2*x+2)*np.abs(y)*np.abs(y+x+1))*np.abs(y+3*x+3)+(y+3*x+3)*np.abs(y)*np.abs(y+x+1)*np.abs(y+2*x+2))*np.abs(y+4*x+4)+(y+4*x+4)*np.abs(y)*np.abs(y+x+1)*np.abs(y+2*x+2)*np.abs(y+3*x+3))/(np.abs(y)*np.abs(y+x+1)*np.abs(y+2*x+2)*np.abs(y+3*x+3)*np.abs(y+4*x+4))
    return equation


def foo2_fixed1(a):
    return foo2(a=a, b=global_b)


def foo2_fixed2(b):
    return foo2(a=global_a, b=b)


def findLfor_foo2(a, b, eps): 
    x = a
    maxa = dxfoo2(x)
    while x <= b:
        x += eps
        y = derivative(function, x)
        if y > maxy:
            maxy = y

    maxy = derivative(function, x)
    while x <= b:
        x += eps
        y = derivative(function, x)
        if y > maxy:
            maxy = y

    return maxy



def dichotomy_method(func, left_edge, right_edge, epsilon):
    middle_point = (left_edge + right_edge)/2
    delta = epsilon
    step_left = func(middle_point - delta)
    step_right = func(middle_point + delta)
    distance = np.abs(right_edge - left_edge)
    
    if distance < epsilon:
        return middle_point
    elif step_left < step_right:
        return dichotomy_method(func, left_edge, middle_point, epsilon)
    else:
        return dichotomy_method(func, middle_point, right_edge, epsilon)


def coordinate_descent(f, f1_fixed, f2_fixed, left_edge, right_edge, eps):
    global global_a, global_b
    f_prev = f(a=global_a, b=global_b)
    f_new = f_prev + 1
    distance = eps + 1
    while distance > eps:
        global_a = dichotomy_method(f1_fixed, left_edge, right_edge, eps)
        global_b = dichotomy_method(f2_fixed, left_edge, right_edge, eps)
        f_prev = f_new
        f_new = f(global_a, global_b)
        print(f'x = {global_a}, y = {global_b}, z = {f_new}')
        distance = np.abs(f_new - f_prev)


def grad_with_line_search(func, dx, dy, l, e, eps):
    coord = np.array([-10, 10])
    f_prev = func(coord)
    grad = np.array([dx(coord), dy(coord)])
    coord = coord - l*grad
    f_new = func(coord)
    distance = np.abs(f_new - f_prev)
    while distance > eps:
        if func(coord - l*derivative(func, coord)) <= func(coord) - e*l*np.abs(derivative(func, coord))**2:
            grad = np.array([dx(coord), dy(coord)])
            coord = coord - l*grad
            f_prev = f_new
            f_new = func(coord)
            distance = np.abs(f_new - f_prev)
        else:
            l = l/2

    return coord


def grad_decent(func, dx, dy, l, eps):
    coord = np.array([-10, 10])
    f_prev = func(coord)
    grad = np.array([dx(coord), dy(coord)])
    coord = coord - l*grad
    f_new = func(coord)
    distance = np.abs(f_new - f_prev)
    while distance > eps:
        grad = np.array([dx(coord), dy(coord)])
        coord = coord - l*grad
        f_prev = f_new
        f_new = func(coord)
        distance = np.abs(f_new - f_prev)

    return coord


def fastest_dive(function, lessd_func, dx, dy, left_edge, right_edge, eps):
    global a0, g1
    coord = np.array([-10, 10])
    f_prev = function(coord)
    f_new = f_prev - 1
    distance = np.abs(f_new - f_prev)
    while distance > eps:
        a0 = coord
        g1 = np.array([dx(coord), dy(coord)])
        alpha = dichotomy_method(lessd_func, left_edge, right_edge, eps)
        grad = g1
        coord = coord - alpha*grad
        f_prev = f_new
        f_new = function(coord)
        distance = np.abs(f_new - f_prev)

    return coord

def main():
    left_edge = -1
    right_edge = 1

    a = np.array([left_edge, left_edge])
    b = np.array([right_edge, right_edge])
    """
    # Generate x and y values
    x = np.linspace(-10, 10, 500)
    y = np.linspace(-10, 10, 500)
    X, Y = np.meshgrid(x, y)

    # Compute the function values for each (x, y) pair
    Z = foo2(X, Y)
    
    # Create the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    
    print(np.min(Z))
    """
    """
    eps = 1/np.power(10, 6)
    L = findL(vectorized_foo2, a, b, eps)
    print(L)
    """
    """
    f_mat = np.array([[dxdxfoo1(), dxdyfoo1()], [dxdyfoo1(), dydyfoo1()]])
    eigenvalues, _ = np.linalg.eig(f_mat)
    l = 2*(1-eps)/np.max(eigenvalues)
    e = 0.1
    coord = fastest_dive(vectorized_foo2, fii2, dxfoo2, dyfoo2, left_edge, right_edge, eps)


    print(f'мои x1 = {coord[0]}, x2 = {coord[1]}, y = {vectorized_foo2(coord)}')
    ax.scatter(coord[0], coord[1], vectorized_foo2(coord), color='r')
    plt.show()
    """

    print(partial_derivative(foo1, var=1, point=[1, 1]))
    

if __name__ == "__main__":
    main()