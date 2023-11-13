# Import necessary libraries
from sympy import symbols, Function, Derivative, Eq, cos, dsolve

# Define the independent variable and the dependent function
x = symbols('x')
y = Function('y')(x)

# Define the differential equation
diff_eq = Eq(Derivative(y, x), cos(4*x) - 2*x)

# Solve the differential equation
solution = dsolve(diff_eq, y)

# Display the solution
print("The solution to the differential equation is:")
print(solution)
