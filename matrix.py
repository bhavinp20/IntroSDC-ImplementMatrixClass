import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 3:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        
        # Calculate the determinant of the square 1x1 matrix.
        if self.h == 1:
            matrixDeterminant = self[0][0]
        
        # Calculate the determinant of the sqyare 2x2 matrix.
        # Formula for |A| = a*d - b*c
        elif self.h == 2:
            a = self[0][0]
            b = self[0][1]
            c = self[1][0]
            d = self[1][1]
            
            matrixDeterminant = a*d - b*c
      
        # Calculate the determinant of the sqyare 2x2 matrix.
        # Formula for |A| = a(ei - fh) − b(di − fg) + c(dh − eg)
        elif self.h == 3:
            a = self[0][0]
            b = self[0][1]
            c = self[0][2]
            d = self[1][0]
            e = self[1][1]
            f = self[1][2]
            g = self[2][0]
            h = self[2][1]
            i = self[2][2]
            
            matrixDeterminant = (a*(e*i - f*h)) - (b*(d*i - f*g)) + (c*(d*h - e*g))
            
        return matrixDeterminant
            
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        matrixTrace = 0

        for i in range(self.h):
            matrixTrace += self[i][i]
        
        return matrixTrace
        

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        matrixInv = []
        
        # Calling identity function
        matrixI = identity(self.h)
        
        # Calculate the inverse of the square 1x1 matrix.
        if self.h == 1:
            matrixInv.append([1/self[0][0]])
            
        elif self.h == 2:
            # If the matrix is 2x2, check that the matrix is invertible
            if ((self[0][0] * self[1][1]) == (self[0][1] * self[1][0])):
                raise ValueError('The matrix is non-invertible')
                
            # Calculate the inverse of the square 2x2 matrix.
            else:
                
                # Calling determinante function
                det = self.determinant()
        
                # Calling trace function
                trc = self.trace()
                
                # Formula for inversing 2x2 matrix
                # invA = 1/det(A) * [trace(A)*I - A]
                
                for i in range(self.h):
                    new_row = []
                    for j in range(self.w):
                        inv = (1/det) * (trc * matrixI[i][j] - self[i][j])
                        new_row.append(inv)
                    matrixInv.append(new_row)
                
        return Matrix(matrixInv)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrixT = []
        
        # Loop through columns on outside loop
        for i in range(self.w):
            new_row = []
            # Loop through rows on inner loop
            for j in range(self.h):
                # Column values will be filled by what were each row before
                new_row.append(self[j][i])
            matrixT.append(new_row)
        
        return Matrix(matrixT)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        matrixSum = []
        
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                matrix_sum = self[i][j] + other[i][j]
                new_row.append(matrix_sum)
            matrixSum.append(new_row)
        
        return Matrix(matrixSum)
                

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        matrixNeg = []
        
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                matrix_neg = -1 * self[i][j]
                new_row.append(matrix_neg)
            matrixNeg.append(new_row)
            
        return Matrix(matrixNeg)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        matrixSub = []
        
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                matrix_sub = self[i][j] - other[i][j]
                new_row.append(matrix_sub)
            matrixSub.append(new_row)
        
        return Matrix(matrixSub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        matrixMul = []
        
        # Calculating matrix multiplication
        for i in range(self.h):
            new_row = []
            for j in range(len(other[0])):
                result = 0
                for k in range(self.w):
                    result += self[i][k] * other[k][j]
                new_row.append(result)
            matrixMul.append(new_row)
                
        return Matrix(matrixMul)


    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            matrixRmul = []
            
            for i in range(self.h):
                new_row = []
                for j in range(self.w):
                    result = other * self[i][j]
                    new_row.append(result)
                matrixRmul.append(new_row)
            return Matrix(matrixRmul)
                
            