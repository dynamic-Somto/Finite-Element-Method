# Import necessary libraries
from sympy import symbols, Function, Derivative, dsolve

# Define the variable and function
x = symbols('x')
y = Function('y')(x)

# Define the differential equation: 5y' + 2x - 3 = 0
diff_eq = 5 * Derivative(y, x) + 2 * x - 3

# Solve the differential equation
solution = dsolve(diff_eq, y)

# Display the general solution
print("General solution:")
print(solution)

# Substitute the initial condition y(2) = 1.4 into the general solution to find the constant value
constant_value = solution.subs({y.subs(x, 2): 1.4}).rhs

# Display the constant value
print("\nConstant value:")
print("C =", constant_value)

# Substitute the constant into the general solution to get the particular solution
particular_solution = solution.subs({'C1': constant_value})

# Display the particular solution
print("\nParticular solution:")
print(particular_solution)
