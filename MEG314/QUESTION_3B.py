from sympy import symbols, Function, Eq, dsolve

# Define the variable and function
x = symbols('x')
y = Function('y')(x)

# Define the differential equation
diff_eq = Eq(2*x*y.diff(x), 3 - x**3)

# Solve the differential equation
solution = dsolve(diff_eq, y)

# Display the solution
print("Solution:")
print(solution)
