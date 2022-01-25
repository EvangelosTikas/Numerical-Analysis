# Numerical-Analysis
Exercises using Numerical Analysis Methods with python, numpy, sci-py, sympy and more packages for solving, printing and plotting functions and Numerical
Analysis methods. Based on the subject Numerical Analysis of Aristotle University of Thessaloniki, Dept. of Physics (B.Sc.) .





## Runge-Kutta 4th Order Method to Solve Differential Equation
Difficulty Level : Medium
Last Updated : 21 Jan, 2022
Given following inputs, 

> An ordinary differential equation that defines value of dy/dx in the form x and y.

> Initial value of y, i.e., y(0)
Thus we are given below.

\frac{\mathrm{dy} }{\mathrm{d} x} = f(x, y),y(0)= y_o      
The task is to find value of unknown function y at a given point x.
The Runge-Kutta method finds approximate value of y for a given x. Only first order ordinary differential equations can be solved by using the Runge Kutta 4th order method.
Below is the formula used to compute next value yn+1 from previous value yn. The value of n are 0, 1, 2, 3, ….(x – x0)/h. Here h is step height and xn+1 = x0 + h
. Lower step size means more accuracy.
K_1 = hf(x_n, y_n)\\ K_2 = hf(x_n+\frac{h}{2}, y_n+\frac{k_1}{2})\\ K_3 = hf(x_n+\frac{h}{2}, y_n+\frac{k_2}{2})\\ K_4 = hf(x_n+h, y_n+k_3)\\ y_{n+1} = y_n + k_1/6 + k_2/3 + k_3/3 + k_4/6 + O(h^{5})

The formula basically computes next value yn+1 using current yn plus weighted average of four increments. 

> k1 is the increment based on the slope at the beginning of the interval, using y

> k2 is the increment based on the slope at the midpoint of the interval, using y + hk1/2.

> k3 is again the increment based on the slope at the midpoint, using using y + hk2/2.

> k4 is the increment based on the slope at the end of the interval, using y + hk3.

> The method is a fourth-order method, meaning that the local truncation error is on the order of O(h5), while the total accumulated error is order O(h4).
Source: https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods


## Euler Method for solving differential equation
Difficulty Level : Easy
Given a differential equation dy/dx = f(x, y) with initial condition y(x0) = y0. Find its approximate solution using Euler method.
Euler Method : 
In mathematics and computational science, the Euler method (also called forward 
Euler method) is a first-order numerical procedurefor solving ordinary differential 
equations (ODEs) with a given initial value. 
Consider a differential equation dy/dx = f(x, y) with initialcondition y(x0)=y0 
then successive approximation of this equation can be given by: 
 

> y(n+1) = y(n) + h * f(x(n), y(n)) 
where h = (x(n) – x(0)) / n 
h indicates step size. Choosing smaller 
values of h leads to more accurate results 
and more computation time. 
 

Example : 
 

    Consider below differential equation
            dy/dx = (x + y + xy)
    with initial condition y(0) = 1 
    and step size h = 0.025.
    Find y(0.1).
   
    Solution:
    f(x, y) = (x + y + xy)
    x0 = 0, y0 = 1, h = 0.025
    Now we can calculate y1 using Euler formula
    y1 = y0 + h * f(x0, y0)
    y1 = 1 + 0.025 *(0 + 1 + 0 * 1)
    y1 = 1.025
    y(0.025) = 1.025.
    Similarly we can calculate y(0.050), y(0.075), ....y(0.1).
    y(0.1) = 1.11167
