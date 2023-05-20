import numpy as np
import pandas as pd

np.random.seed(400)

x_i = (0, 1, 2, 3, 4)
y_i = (0, -1, -2, -3, -4)

a0 = np.random.uniform(-1, 1) # 0.33745781766834937
b0 = np.random.uniform(-1, 1) # -0.5480030598030905
g1 = 1/np.sqrt(2)
g2 = 1/np.sqrt(2)

data_for_excel = [[i for i in range(26)],[],[],[],[],[],[],[]]

def foo1(a, b):
    equation = 0
    for i in range(5):
        equation += np.power(a*x_i[i] + b - y_i[i], 2)
    return equation

def foo2(a, b):
    equation = 0
    for i in range(5):
        equation += np.abs(a*x_i[i] + b - y_i[i])
    return equation

def fii1(gamma):
    equation = foo1(a0 + gamma*g1, b0 + gamma*g2)
    return equation

def fii2(gamma):
    equation = foo2(a0 + gamma*g1, b0 + gamma*g2)
    return equation

def dichotomy_method(func, left_edge, right_edge, epsilon):
    middle_point = (left_edge + right_edge)/2
    delta = epsilon
    step_left = func(middle_point - delta)
    step_right = func(middle_point + delta)
    distance = np.abs(right_edge - left_edge)
    if distance < epsilon:
        """
        data_for_excel[1].append(left_edge)
        data_for_excel[2].append(right_edge)
        data_for_excel[3].append((right_edge - left_edge)/2)
        data_for_excel[4].append(step_left)
        data_for_excel[5].append(step_right)
        data_for_excel[6].append(func(step_left))
        data_for_excel[7].append(func(step_right))
        """
        return middle_point
    elif step_left < step_right:
        """
        data_for_excel[1].append(left_edge)
        data_for_excel[2].append(right_edge)
        data_for_excel[3].append((right_edge - left_edge)/2)
        data_for_excel[4].append(step_left)
        data_for_excel[5].append(step_right)
        data_for_excel[6].append(func(step_left))
        data_for_excel[7].append(func(step_right))
        """
        return dichotomy_method(func, left_edge, middle_point, epsilon)
    else:
        """
        data_for_excel[1].append(left_edge)
        data_for_excel[2].append(right_edge)
        data_for_excel[3].append((right_edge - left_edge)/2)
        data_for_excel[4].append(step_left)
        data_for_excel[5].append(step_right)
        data_for_excel[6].append(func(step_left))
        data_for_excel[7].append(func(step_right))
        """
        return dichotomy_method(func, middle_point, right_edge, epsilon)
    
def golden_section_method(func, left_edge, right_edge, epsilon):
    gr = (np.sqrt(5) - 1)/2
    shift = gr * (right_edge - left_edge)
    c = left_edge + shift
    d = right_edge - shift
    distance = np.abs(right_edge - left_edge)
    if distance < epsilon:
        """
        data_for_excel[1].append(left_edge)
        data_for_excel[2].append(right_edge)
        data_for_excel[3].append((right_edge - left_edge)/2)
        data_for_excel[4].append(c)
        data_for_excel[5].append(d)
        data_for_excel[6].append(func(c))
        data_for_excel[7].append(func(d))
        """
        return (right_edge + left_edge)/2
    if func(c) >func(d):
        """
        data_for_excel[1].append(left_edge)
        data_for_excel[2].append(right_edge)
        data_for_excel[3].append((right_edge - left_edge)/2)
        data_for_excel[4].append(c)
        data_for_excel[5].append(d)
        data_for_excel[6].append(func(c))
        data_for_excel[7].append(func(d))
        """
        return golden_section_method(func, left_edge, c, epsilon)
    else:
        """
        data_for_excel[1].append(left_edge)
        data_for_excel[2].append(right_edge)
        data_for_excel[3].append((right_edge - left_edge)/2)
        data_for_excel[4].append(c)
        data_for_excel[5].append(d)
        data_for_excel[6].append(func(c))
        data_for_excel[7].append(func(d))
        """
        return golden_section_method(func, d, right_edge, epsilon)

def main():
    left_edge = -10
    right_edge = 10
    epsilon = 1/np.power(10, 6)

    print(golden_section_method(fii1, left_edge, right_edge, epsilon))
    print(dichotomy_method(fii1, left_edge, right_edge, epsilon))

    print(golden_section_method(fii2, left_edge, right_edge, epsilon))
    print(dichotomy_method(fii2, left_edge, right_edge, epsilon))
    """
    df = pd.DataFrame(data_for_excel[1:],
                index=['a', 'b', '|b-a|/2', 'c', 'd', 'func(c)', 'func(d)'], columns=data_for_excel[0])
    
    df.to_excel('dichotomy_absolute.xlsx', sheet_name='dichotomy_absolute')
    """

if __name__ == "__main__":
    main()