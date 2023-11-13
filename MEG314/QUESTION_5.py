from sympy import symbols, Function, Eq, dsolve

# Define the variable and function
t = symbols('t')
x = Function('x')(t)

# Define the differential equation
diff_eq = Eq(x.diff(t, t) + 196 * x, 0)

# Solve the differential equation
solution = dsolve(diff_eq, x)

# Display the solution
print("Solution:")
print(solution)
