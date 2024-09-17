from math import *
import numpy as np
from sympy import *
import os

def clear(): os.system("cls")

class Zadanie():
    # MATRIX
    def z1(self):
        a = np.array([
            [3, 2, 0],
            [1, -1, 0],
            [0, 5, 1]
        ])
        b = np.array([2, 4, -1])
        return np. linalg.solve(a,b)
    def z2(self):
        A = Matrix([[3, 2, 0],
            [1, -1, 0],
            [0, 5, 1]])
        b = Matrix([2, 4, -1])
        return A.inv()*b
    def z3(self):
        A = Matrix([
            [1,-2,4],
            [1,-2,1],
            [-3,6,-12]
        ])
        return A.rank()
    # INTEGRAL
    def z4(self):
        x = Symbol("x")
        dx = Symbol("dx")
        a = diff(atan(1/x),x)
        return dx*a
    def z5(self):
        x = symbols("x")
        return integrate(6*x**5, x)
    def z6(self):
        x = symbols("x")
        return integrate(x/(x+2),(x,1,3))
    def z7(self):
        x = symbols("x")
        return integrate(x**(-4),(x,1,inf))
    def z8(self):
        x = symbols("x")
        y = symbols("y")
        return integrate(y**2*x-2*x*y,(y,x,2))

def app():
    z = Zadanie()
    zList = [
        z.z1, z.z2, z.z3, z.z4,
        z.z5, z.z6, z.z7, z.z8,
    ]
    for i in range(len(zList)):
        print(f"Задание{i}: {zList[i]()}")

if __name__ == "__main__":
    clear()
    app()