import sympy as sp

# Constant
P = 50000

# Define symbols
t = sp.symbols('t')
N = sp.Function('N')

# Solved general solution
diff_eq = sp.Eq(N(t).diff(t, t) + N(t).diff(t) + 5*N(t)/4, 5*P/4)

general_solution = sp.dsolve(diff_eq)

print("\nGeneral Solution:")
sp.pprint(general_solution)

# Solved particular solution
particular_solution = sp.dsolve(diff_eq, N(t), ics= {N(t).subs(t, 0): 1/5, N(t).diff(t).subs(t, 0): 1/20})

print("\nParticular Solution:")
sp.pprint(particular_solution)

# Plotting the graph
sp.plot(particular_solution.rhs, (t, 0, 30))