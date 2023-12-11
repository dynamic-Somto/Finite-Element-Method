import sympy as sp

# Define the constant
P = 50000

# Define the symbols
t = sp.symbols('t')
N = sp.Function('N')

# Define the differential equation
diff_eq = sp.Eq(N(t).diff(t, t) + N(t).diff(t) + 5*N(t)/4, 5*P/4)

# Solve the general solution
general_solution = sp.dsolve(diff_eq)

# Print the general solution
print("\nGeneral Solution:")
sp.pprint(general_solution)

# Solve the particular solution with initial conditions
particular_solution = sp.dsolve(diff_eq, N(t), ics={N(0): 1/5, N(t).diff(t).subs(t, 0): 1/20})

# Print the particular solution
print("\nParticular Solution:")
sp.pprint(particular_solution)

# Plot the graph
sp.plot(particular_solution.rhs, (t, 0, 30))