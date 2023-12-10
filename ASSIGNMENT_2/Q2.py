import sympy as sp

# Constants
c = 12.5  #Drag Coefficient
m = 68.1  #Mass
g = 9.81  #Gravitational acceleration

# Symbols
t = sp.symbols('t')
v = sp.Function('v')('t')

# Differential Equation
diff_eq = sp.Eq(g - sp.Rational(c, m) * v, v.diff(t))

# Solved general solution
general_solution = sp.dsolve(diff_eq)

print('\nGeneral Solution:')
sp.pprint((sp.simplify(general_solution.n())))

# Solved particular solution
particular_solution = sp.dsolve(diff_eq, ics = {v.subs(t, 0) : 0})

print('\nParticular Solution:')
sp.pprint((sp.simplify(particular_solution.n())))

# To get the velocity after 10s, substitute for t = 10s
velocity_10 = particular_solution.rhs.subs(t, 10)

print(f"\nVelocity at t = 10seconds is {velocity_10.round(2)}𝑚/𝑠")

# To get the acceleration after 10s, differentiate the 
# general equation w.r.t {t} and substitute for t = 10s
acc_10 = particular_solution.rhs.diff(t).subs(t, 10)

print(f"\nAcceleration at t = 10seconds is {acc_10.round(2)}𝑚/𝑠2")

# Terminal Velocity
terminal_velocity = g * m / c
print(f"\nTerminal velocity is {round(terminal_velocity, 2)}𝑚/𝑠")

# Plotting the graph
sp.plot(particular_solution.rhs, (t, 0, 30))