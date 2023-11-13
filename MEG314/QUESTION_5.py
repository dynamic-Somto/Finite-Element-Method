# Import necessary libraries
from sympy import symbols, Function, Eq, dsolve

# Define the variable and function
time = symbols('t')
position = Function('x')(time)

# Define the differential equation
differential_eq = Eq(position.diff(time, time) + 196 * position, 0)

# Solve the differential equation
solution = dsolve(differential_eq, position)

# Display the solution
print("The solution to the differential equation is:")
print(solution)
