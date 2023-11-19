from sympy import symbols, Function, Derivative, dsolve

# Define the variable and function
x = symbols('x')
y = Function('y')(x)

# Define the differential equation
diff_eq = 5 * y.diff(x) + 2 * x - 3

# Solve the differential equation
solution = dsolve(diff_eq, y, ics={y.subs(x, 2): 1.4})

# Display the general solution
print("General solution:")
print(solution)

# Substitute the initial condition y(2) = 1.4 into the general solution
constant_value = solution.subs({y.subs(x, 2): 1.4}).rhs

# Display the constant value
print("\nConstant value:")
print("C =", constant_value)

# Substitute the constant into the general solution
particular_solution = solution.subs({'C1': constant_value})

# Display the particular solution
print("\nParticular solution:")
print(particular_solution)
