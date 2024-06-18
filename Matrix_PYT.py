import os
import numpy as np


class Matrix:

    def __init__(self, size, name):
        self.size = size
        self.name = name
        self.q = self.createMatrix()
        print(f'{self.name}: {self.q}')

    def createMatrix(self):
        M = []
        for i in range(self.size[0]):
            M.append([0] * self.size[0])
        return M

    def dataMatrix(self):
        filas = len(self.q)
        columnas = len(self.q[1])
        for i in range(filas):
            for j in range(columnas):
                while True:
                    try:
                        self.q[i][j] = float(input(self.name + '[' + str(i) + ',' + str(j) + ']:\n'))
                    except ValueError:
                        print('Valor invalido, vuelva a ingresar el dato...')
                        continue
                    break
                os.system('cls')
        return self.q

    def add(self, S):
        try:
            if self.size != S.size:
                raise Exception('Matriz: las Matrices son de tamaño diferente...')
        except Exception as x:
            print(x)
            quit()
        return np.array(self.q) + np.array(S.q)

    def product(self, S):
        try:
            if self.size != S.size:
                raise Exception('Matriz: las Matrices son de tamaño diferente...')
        except Exception as x:
            print(x)
            quit()
        return np.array(self.q) * np.array(S.q)

    def show(self):
        print(self.name)
        for i in range(len(self.q)):
            print(f'{self.q[i]}')
