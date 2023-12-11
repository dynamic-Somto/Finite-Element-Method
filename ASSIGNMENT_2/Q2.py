import sympy as sp

# Constants
drag_coefficient = 12.5
mass = 68.1
gravitational_acceleration = 9.81

# Symbols
time = sp.symbols('t')
velocity = sp.Function('v')(time)

# Differential Equation
differential_eq = sp.Eq(gravitational_acceleration - sp.Rational(drag_coefficient, mass) * velocity, velocity.diff(time))

# Solved general solution
general_solution = sp.dsolve(differential_eq)

print('\nGeneral Solution:\n')
sp.pprint(sp.simplify(general_solution))

# Solved particular solution
particular_solution = sp.dsolve(differential_eq, ics={velocity.subs(time, 0): 0})

print('\nParticular Solution:\n')
sp.pprint(sp.simplify(particular_solution))

# Calculate velocity at t = 10 seconds
velocity_10 = particular_solution.rhs.subs(time, 10)

print(f"\nVelocity at t = 10 seconds is {velocity_10.round(2)} m/s")

# Calculate acceleration at t = 10 seconds
acceleration_10 = particular_solution.rhs.diff(time).subs(time, 10)

print(f"\nAcceleration at t = 10 seconds is {acceleration_10.round(2)} m/s^2")

# Calculate terminal velocity
terminal_velocity = gravitational_acceleration * mass / drag_coefficient
print(f"\nTerminal velocity is {round(terminal_velocity, 2)} m/s")

# Plot the graph
sp.plot(particular_solution.rhs, (time, 0, 30))
