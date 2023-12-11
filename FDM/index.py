import numpy as np
import matplotlib
import scipy.linalg as lin
import matplotlib.pyplot as plt


class FDMSteadyFlow2D:
    def __init__(self, Nx, Ny, h_top, h_bottom, h_left, h_right):
        """
        Initialize the FDM object.

        Parameters:
        - Nx (int): Number of grid points in the x-direction.
        - Ny (int): Number of grid points in the y-direction.
        - h_top (float): Height of the top boundary.
        - h_bottom (float): Height of the bottom boundary.
        - h_left (float): Height of the left boundary.
        - h_right (float): Height of the right boundary.
        """
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

        Returns:
        A (numpy.ndarray): The coefficient matrix A
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

        Returns:
        b (numpy.ndarray): The right hand side vector b
        '''
        b = np.zeros((self.Nx - 1)**2)
        b[-self.Nx+1:] += -self.h_top
        b[:self.Nx-1] += -self.h_bottom
        b[::self.Nx-1] += -self.h_left
        b[self.Nx-2::self.Nx-1] += -self.h_right

        return b

    def solveLinearSystem(self, A, b):
        '''
        Solves the final linear system Ax = b and concatenates the
        boundary conditions (BCs) to the solution

        Parameters:
            A (ndarray): Coefficient matrix of the linear system
            b (ndarray): Right-hand side vector of the linear system

        Returns:
            ndarray: The solution of the linear system with boundary conditions
        '''
        # Solve for h vector and reshape array to 2D
        h = lin.solve(A, b)
        h = h.reshape((self.Nx - 1, self.Ny - 1))

        # Create empty 2D array with all nodes and insert BCs ans solution
        h2D = np.zeros((self.Nx + 1, self.Ny + 1))
        h2D[0] = self.h_top         # Insert top BC
        h2D[-1] = self.h_bottom     # Insert bottom BC
        h2D[:, 0] += self.h_left     # Insert left BC
        h2D[:, -1] += self.h_right   # Insert right BC
        h2D[1:-1, 1:-1] = h[::-1]    # Insert solution (::-1 => inverted)

        return h2D

    def plotSolution(self, h2D):
        '''
        Plots the color plot of the solution on a 2D meshgrid

        Parameters:
        - h2D: 2D array of the solution values

        Returns:
        None
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
        plt.xlabel(r'$x$ [$\mathrm{m}$]')
        plt.ylabel(r'$y$ [$\mathrm{m}$]')
        plt.show()


if __name__ == "__main__":
    # For 100 equations, we need a Nx = Ny = 11 grid with Nx - 1 = Ny - 1 = 10 unknowns
    fdm = FDMSteadyFlow2D(Nx=4, Ny=4, h_top=100, h_bottom=0, h_left=75, h_right=50)
    A = fdm.buildCoeffMatrix()
    print("Coefficient Matrix = \n", A)
    b = fdm.buildRHSVector()
    print("RHS Vector = \n", b)
    h = fdm.solveLinearSystem(A, b)
    print("Solution = \n", h)
    fdm.plotSolution(h)