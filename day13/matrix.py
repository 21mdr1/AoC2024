class Matrix:
    # this will only handle 2x2 and 1x2 matrices, which is all we need
    def __init__(self, matrix):
        if len(matrix) != 2:
            raise ValueError
        
        self.isSquare = len(matrix[0]) == 2

        if self.isSquare:
            self.a, self.b = matrix[0]
            self.c, self.d = matrix[1]
        else:
            self.a = matrix[0][0]
            self.b = matrix[1][0]

    def determinant(self):
        if not self.isSquare:
            return None
        return self.a*self.d - self.b*self.c
    
    def isInvertible(self):
        det = self.determinant()
        return det is not None and det != 0
    
    def inverse(self):
        if not self.isInvertible():
            return None

        det = self.determinant()

        matrix = [
            [ self.d, -1 * self.b ],
            [ -1 * self.c, self.a ]
        ]

        return Matrix(matrix) / det
    
    def inverse_without_det(self):
        if not self.isInvertible():
            return None

        matrix = [
            [ self.d, -1 * self.b ],
            [ -1 * self.c, self.a ]
        ]

        return Matrix(matrix)

    def isInt(self):
        if self.isSquare:
            return int(self.a) == self.a and int(self.b) == self.b and int(self.c) == self.c and int(self.d) == self.d
        return int(self.a) == self.a and int(self.b) == self.b
    
    def __mul__(self, other):
        if isinstance(other, int):
            if self.isSquare:
                return Matrix([[self.a * other, self.b * other], [self.c * other, self.d * other]])
            return Matrix([[self.a * other], [self.b * other]])

        if isinstance(other, Matrix):
            if not self.isSquare:
                raise ValueError
            
            return Matrix([
                [ self.a * other.a + self.b * other.b ],
                [ self.c * other.a + self.d * other.b ]
            ])
        
        else:
            raise TypeError
    
    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            if self.isSquare:
                return Matrix([[self.a * other, self.b * other], [self.c * other, self.d * other]])
            return Matrix([[self.a * other], [self.b * other]])

        if isinstance(other, Matrix):
            if not other.isSquare or self.isSquare:
                raise ValueError
            
            return Matrix([
                [ other.a * self.a + other.b * self.b ],
                [ other.c * self.a + other.d * self.b ]
            ])
        
        else:
            raise TypeError

    def __truediv__(self, other):
        # maybe I'll implement mult by inverse as matrix div but idk if that's worth it
        if not isinstance(other, int) and not isinstance(other, float):
            raise TypeError
        
        return Matrix([
            [self.a / other, self.b / other],
            [self.c / other, self.d / other]
        ]) if self.isSquare else Matrix([
            [self.a / other],
            [self.b / other]
        ])
    
    def __floordiv__(self, other):
        if not isinstance(other, int) and not isinstance(other, float):
            raise TypeError
        
        return Matrix([
            [self.a // other, self.b // other],
            [self.c // other, self.d // other]
        ]) if self.isSquare else Matrix([
            [self.a // other],
            [self.b // other]
        ])

    def __repr__(self):
        if self.isSquare:
            return f'Matrix([[{self.a}, {self.b}], [{self.c}, {self.d}]])'
        return f'Matrix([[{self.a}], [{self.b}]])'

    def __str__(self):
        if self.isSquare:
            return f'{self.a} {self.b}\n{self.c} {self.d}'
        return f'{self.a}\n{self.b}'