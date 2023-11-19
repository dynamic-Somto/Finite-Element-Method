import sympy as sp

# Constants
c = 12.5
m = 68.1
g = 9.81

#Symbols
t = sp.symbols('t')
v = sp.Function('v')('t')

# Differential Equation
diff_eq = sp.Eq(g - sp.Rational(c, m) * v, v.diff(t))

# Solved general solution
general_solution = sp.dsolve(diff_eq)

print('General Solution:\n')
sp.pprint((sp.simplify(general_solution.n())))

# Solved particular solution
particular_solution = sp.dsolve(diff_eq, ics = {v.subs(t, 0) : 0})

print('Particular Solution:\n')
sp.pprint((sp.simplify(particular_solution.n())))

#To get the velocity after 10s, substitute for t = 10s
velocity_10 = particular_solution.rhs.subs(t, 10)

print(f"Velocity at t = 10seconds is {velocity_10.round(2)}𝑚/𝑠")

#To get the acceleration after 10s, differentiate the 
# general equation w.r.t {t} and substitute for t = 10s
acc_10 = particular_solution.rhs.diff(t).subs(t, 10)

print(f"Acceleration at t = 10seconds is {acc_10.round(2)}𝑚/𝑠2")

# Terminal Velocity
terminal_velocity = g * m / c
print(f"Terminal velocity is {round(terminal_velocity, 2)}𝑚/𝑠")

# Plotting the graph
solutions = []
t_range = (t, 0, 30)
solutions.append(particular_solution.rhs)
sp.plot(*solutions, t_range)