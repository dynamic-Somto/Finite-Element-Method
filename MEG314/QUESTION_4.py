from sympy import symbols, Function, Eq, dsolve

# Define the variable and function
x = symbols('x')
y = Function('y')(x)

# Define the differential equation
diff_eq = Eq(y.diff(x) + y/2, 3/2)

# Solve the differential equation
solution = dsolve(diff_eq, y)

# Display the solution
print("Solution:")
print(solution)
