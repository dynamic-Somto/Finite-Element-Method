'''
NOTE
Reference/Code_Sample From:
Yared W. Bekele
https://github.com/yaredwb/FDM2D
'''

import numpy as np
import matplotlib
import scipy.linalg as lin
import matplotlib.pyplot as plt


class FDMSteadyFlow2D:
    def __init__(self, Nx, Ny, h_top, h_bottom, h_left, h_right):
        self.Nx = Nx
        self.Ny = Ny
        self.h_top = h_top
        self.h_bottom = h_bottom
        self.h_left = h_left
        self.h_right = h_right

    def buildCoeffMatrix(self):
        '''
        Constructs the coefficient matrix A of the final linear
        system of equations of the form Ax = b
        '''
        # Create the diagonal, upper and lower components of B
        Ddiag = -4 * np.eye(self.Nx - 1)
        Dupper = np.diag([1] * (self.Nx - 2), 1)
        Dlower = np.diag([1] * (self.Nx - 2), -1)

        # Add components to create B
        D = Ddiag + Dupper + Dlower

        # Create a block matrix where the diagonals are each B
        Ds = [D] * (self.Nx - 1)
        A = lin.block_diag(*Ds)

        # Create the identity diagonals
        I = np.ones((self.Nx - 1) * (self.Nx - 2))
        Iupper = np.diag(I, self.Nx - 1)
        Ilower = np.diag(I, -self.Nx + 1)

        # Add the identity diagonal to A to complete it
        A += Iupper + Ilower

        return A

    def buildRHSVector(self):
        '''
        Constructs the right hand side vector b of the final linear
        system of equations of the form Ax = b
        '''
        b = np.zeros((self.Nx - 1)**2)
        
        # Sets the inital values for the top boundaries in the result
        b[-self.Nx+1:] = -self.h_top
        
        #NOTE: The modification of Yared W. Bekele's buildRHSVector function starts here
        
        # Sets the inital values for the bottom boundaries in the result
        b[:self.Nx-1] = -self.h_bottom
        
        # To add up the values for the left and right boundaries,
        # we're iterating through the values of the list and adding 
        # the values for the left and right boundaries since the have 
        # no definite position unlike the top and bottom boundaries
        for i in range(0, len(b), 1):
            
            # The left boundary points are located where i % (self.Nx - 1) == 0
            if(i % (self.Nx - 1) == 0):
                b[i] += (-self.h_left)
            
            # The right boundary points are located where i % (self.Nx - 1) == self.Nx - 2
            if(i % (self.Nx - 1) == self.Nx - 2):
                b[i] += (-self.h_right)
        return b

    def solveLinearSystem(self, A, b):
        '''
        Solves the final linear system Ax = b and concatenates the
        boundary conditions (BCs) to the solution
        '''
        # Solve for h vector and reshape array to 2D
        h = lin.solve(A, b)
        h = h.reshape((self.Nx - 1, self.Ny - 1))

        # Create empty 2D array with all nodes and insert BCs ans solution
        h2D = np.zeros((self.Nx + 1, self.Ny + 1))
        h2D[0] = self.h_top         # Insert top BC
        h2D[1:-1, 1:-1] = h[::-1]    # Insert solution (::-1 => inverted)

        return h2D

    def plotSolution(self, h2D):
        '''
        Plots the color plot of the solution on a 2D meshgrid
        '''
        # Create 1D arrays with number of nodes
        x = np.linspace(0, 1, self.Nx + 1)
        y = np.linspace(1, 0, self.Ny + 1)

        # Create 2D mesh grid
        X, Y = np.meshgrid(x, y)

        # Plot solution on mesh grid
        matplotlib.rcParams['figure.figsize'] = 6.2, 5
        plt.contourf(X, Y, h2D, 10)
        plt.colorbar()
        plt.show()


if __name__ == "__main__":
    # Setting grid number of 11 will generate 100 equations [(grid_number-1)**2]
    fdm = FDMSteadyFlow2D(Nx=11, Ny=11, h_top=100, h_bottom=0, h_left=75, h_right=50)
    A = fdm.buildCoeffMatrix()
    print('\nLHS 10 by 10 coefficient matrix:')
    print(A)
    b = fdm.buildRHSVector()
    print('\nRHS Vector:')
    print(b)
    h = fdm.solveLinearSystem(A, b)
    print('\nFinal Solution:')
    print(h)
    fdm.plotSolution(h)