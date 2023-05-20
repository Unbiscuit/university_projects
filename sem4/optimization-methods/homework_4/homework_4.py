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


def fii1(gamma):
    global a0, g1
    equation = foo1(*(a0 - gamma*g1))
    return equation


def foo1_fixed1(a):
    return foo1(a=a, b=global_b)


def foo1_fixed2(b):
    return foo1(a=global_a, b=b)


def foo2(a, b):
    equation = 0
    for i in range(5):
        equation += np.abs(a*x_i[i] + b - y_i[i])
    return equation


def foo2_fixed1(a):
    return foo2(a=a, b=global_b)


def foo2_fixed2(b):
    return foo2(a=global_a, b=b)


def partial_derivative(func, var=0, point=[]):
    args = point[:]
    def wraps(x):
        args[var] = x
        return func(*args)
    return derivative(wraps, point[var], dx = 1e-6)


def lipschitz_constant_2d(f, x_range, y_range):
    x_min, x_max = x_range
    y_min, y_max = y_range
    
    # Generate a grid of points within the given ranges
    x = np.linspace(x_min, x_max, 100)
    y = np.linspace(y_min, y_max, 100)
    X, Y = np.meshgrid(x, y)
    
    # Compute the function values at the grid points
    Z = f(X, Y)
    
    # Compute the maximum absolute difference between adjacent grid points
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    max_diff = np.max(np.abs(np.diff(Z, axis=0))) / dx + np.max(np.abs(np.diff(Z, axis=1))) / dy
    
    return max_diff


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
    xn = []
    norm_xnew_xold = []
    func_xnew = []
    abs_funcnew_funcold = []

    f_prev = f(a=global_a, b=global_b)
    f_new = f_prev + 1
    distance = eps + 1
    while distance > eps:
        xn_old = np.array([global_a, global_b])
        global_a = dichotomy_method(f1_fixed, left_edge, right_edge, eps)
        global_b = dichotomy_method(f2_fixed, left_edge, right_edge, eps)
        xn_new = np.array([global_a, global_b])
        f_prev = f_new
        f_new = f(global_a, global_b)
        distance = np.abs(f_new - f_prev)

        norm_xnew_xold.append(np.linalg.norm(xn_new - xn_old))
        xn.append(f'{global_a}, {global_b}')
        func_xnew.append(f_new)
        abs_funcnew_funcold.append(np.abs(distance))
    """
    df = pd.DataFrame({'xn': xn,
                   '||xn - x(n-1)||': norm_xnew_xold,
                   'f(xn)': func_xnew,
                   '|f(xn) - f(x(n-1))|': abs_funcnew_funcold})
    df.to_excel('/home/uncookie/Documents/university_projects/sem4/optimization-methods/homework_4/coordinate_desc_foo2.xlsx', index=True)
    """
    

    return global_a, global_b


def grad_with_line_search(func, l, e, eps):
    xn = []
    fxn = []
    grad_norm = []

    coord = [-10, 10]
    xn.append(f'{coord[0]}, {coord[1]}')
    f_prev = func(*coord)
    fxn.append(f_prev)
    grad = np.array([partial_derivative(func, var=0, point=coord), partial_derivative(func, var=1, point=coord)])
    grad_norm.append(np.linalg.norm(grad))
    f_new = f_prev - 1
    distance = np.abs(f_new - f_prev)
    while distance > eps:
        possible_grad = np.array([partial_derivative(func, var=0, point=coord), partial_derivative(func, var=1, point=coord)])
        possible_coord = coord - l*possible_grad
        if func(*possible_coord) <= func(*coord) - e*l*np.abs(func(*coord)):
            grad = np.array([partial_derivative(func, var=0, point=coord), partial_derivative(func, var=1, point=coord)])
            grad_norm.append(np.linalg.norm(grad))
            coord = coord - l*grad
            xn.append(f'{coord[0]}, {coord[1]}')
            f_prev = f_new
            f_new = func(coord[0], coord[1])
            fxn.append(f_new)
            distance = np.abs(f_new - f_prev)
        else:
            l = l/2

    """
    df = pd.DataFrame({'xn': xn[::10],
                   'fxn': fxn[::10],
                   '||grad(fxn)||': grad_norm[::10]})
    df.to_excel('/home/uncookie/Documents/university_projects/sem4/optimization-methods/homework_4/line_search.xlsx', index=True)
    """

    return coord


def grad_decent(func, l, eps):
    xn = []
    fxn = []
    grad_norm = []

    coord = [-10, 10]
    xn.append(f'{coord[0]}, {coord[1]}')
    f_prev = func(*coord)
    fxn.append(f_prev)
    grad = np.array([partial_derivative(func, var=0, point=coord), partial_derivative(func, var=1, point=coord)])
    grad_norm.append(np.linalg.norm(grad))
    f_new = f_prev - 1
    distance = np.abs(f_new - f_prev)
    while distance > eps:
        grad = np.array([partial_derivative(func, var=0, point=coord), partial_derivative(func, var=1, point=coord)])
        grad_norm.append(np.linalg.norm(grad))
        coord = coord - l*grad
        xn.append(f'{coord[0]}, {coord[1]}')
        f_prev = f_new
        f_new = func(*coord)
        fxn.append(f_new)
        distance = np.abs(f_new - f_prev)
    """
    df = pd.DataFrame({'xn': xn[::10],
                   'fxn': fxn[::10],
                   '||grad(fxn)||': grad_norm[::10]})
    df.to_excel('/home/uncookie/Documents/university_projects/sem4/optimization-methods/homework_4/grad_decent_search.xlsx', index=True)
    """

    return coord


def fastest_dive(function, lessd_func, left_edge, right_edge, eps):
    xn = []
    fxn = []
    grad_norm = []

    global a0, g1
    coord = [-10, 10]
    xn.append(f'{coord[0]}, {coord[1]}')
    f_prev = function(coord[0], coord[1])
    fxn.append(f_prev)
    g1 = np.array([partial_derivative(function, var=0, point=coord), partial_derivative(function, var=1, point=coord)])
    grad_norm.append(np.linalg.norm(g1))
    f_new = f_prev - 1
    distance = np.abs(f_new - f_prev)
    while distance > eps:
        a0 = coord
        g1 = np.array([partial_derivative(function, var=0, point=coord), partial_derivative(function, var=1, point=coord)])
        grad_norm.append(np.linalg.norm(g1))
        alpha = dichotomy_method(lessd_func, left_edge, right_edge, eps)
        grad = g1
        coord = coord - alpha*grad
        xn.append(f'{coord[0]}, {coord[1]}')
        f_prev = f_new
        f_new = function(coord[0], coord[1])
        fxn.append(f_new)
        distance = np.abs(f_new - f_prev)
    """
    df = pd.DataFrame({'xn': xn,
                   'fxn': fxn,
                   '||grad(fxn)||': grad_norm})
    df.to_excel('/home/uncookie/Documents/university_projects/sem4/optimization-methods/homework_4/fastest_dive_search.xlsx', index=True)
    """

    return coord

def coordinate_main(func, fixed1, fixed2):

    left_edge = -2
    right_edge = 2
    eps = 1/np.power(10, 6)

    coord = coordinate_descent(func, fixed1, fixed2, left_edge, right_edge, eps)
    return coord


def line_search_main():

    eps = 1/np.power(10, 6)
    alpha = (1 - eps)/lipschitz_constant_2d(foo1, [-1, 1], [-1, 1])
    e = 0.5

    coord = grad_with_line_search(foo1, alpha, e, eps)
    return coord


def grad_decent_main():

    eps = 1/np.power(10, 6)
    alpha = (1 - eps)/lipschitz_constant_2d(foo1, [-1, 1], [-1, 1])

    coord = grad_decent(foo1, alpha, eps)
    return coord


def fastest_dive_main():

    left_edge = -2
    right_edge = 2
    eps = 1/np.power(10, 6)

    coord = fastest_dive(foo1, fii1, left_edge, right_edge, eps)
    return coord

if __name__ == "__main__":

    x = np.linspace(-10, 10, 500)
    y = np.linspace(-10, 10, 500)
    X, Y = np.meshgrid(x, y)

    # Compute the function values for each (x, y) pair
    Z = foo1(X, Y)
    print(np.min(Z))
    
    # Create the plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    coord = fastest_dive_main()
    ax.scatter(coord[0], coord[1], foo1(*coord), color='r')
    print(f'мои x1 = {coord[0]}, x2 = {coord[1]}, y = {foo1(*coord)}')
    plt.show()