import sympy as sp

P = 50000
# Define symbols
t = sp.symbols('t')
N = sp.Function('N')

# Write the ODE
diff_eq = sp.Eq(N(t).diff(t, t) + N(t).diff(t) + 5*N(t)/4, 5*P/4)

general_solution = sp.dsolve(diff_eq)
sp.pprint(general_solution)

# Initial conditions
initial_conditions = {N(t).subs(t, 0): 1/5, N(t).diff(t).subs(t, 0): 1/20}

# Solve the ODE
solution = sp.dsolve(diff_eq, N(t), ics=initial_conditions)

# Output the solution
print("Solution:")
sp.pprint(solution)

sp.plot(solution.rhs, (t, 0, 30), title='Population vs Time', xlabel='Time (t)', ylabel='Population (N)', legend=True)