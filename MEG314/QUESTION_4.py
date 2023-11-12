# import necessary functions from sympy library
from sympy import symbols, Function, Eq, dsolve, Derivative

# Define the independent variable and the dependent function
x = symbols('x')
y = Function('y')(x)

# Define the differential equation
diff_eq = Eq(Derivative(y, x) + y/2, 3/2)

# Solve the differential equation
solution = dsolve(diff_eq, y)

# Display the solution
print("The solution to the differential equation:")
print(solution)
