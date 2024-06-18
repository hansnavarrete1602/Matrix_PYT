import os

def dimension(name):
    try:
        size = int(input('Dimensión del vector {%s}: '%name))
    except ValueError:
        print('no pudo convertirse a <int> el valor ingresado..')
        quit()
    try:
        if size <= 0:
            raise Exception('la dimensión debe ser positiva..')
    except Exception as x:
        print(x)
        quit()
    return size

def createVector(size):
    L = [0]*size
    return L

def data(q, name):
    print('Ingrese los datos del vector: {%s}'%name)
    lg = len(q)
    for i in range(lg):
        while True:
            try:
                q[i] = float(input(name + '(' + str(i) + '):  '))
            except ValueError:
                print('valor ingresado inválido, ingrese nuevamente..')
                continue
            break

def norma(q):
    sumatoria = 0.0
    for i in range(len(q)):
        sumatoria += q[i] ** 2
    return sumatoria ** (1/2)

def add(q,r):
    s = []
    try:
        if len(q) != len(r):
            raise Exception('Los vectores son de diferentes dimensiones')
    except Exception as x:
        print(x)
        quit()
    for i in range(len(q)):
        valor = q[i] + r[i]
        s.append(valor)
    return s

def punto(q,r):
    sumatoria = 0.0
    try:
        if len(q) != len(r):
            raise Exception('No es posible calcular el producto PUNTO..')
    except Exception as x:
        print(x)
        quit()
    for i in range(len(q)):
        sumatoria += q[i] * r[i]
    return sumatoria

def dimensiones(name):
    try:
        filas = int(input('Ingrese filas de la Matriz {%s}:\n'%name))
        columnas = int(input('Ingrese columnas de la Matriz {%s}:\n'%name))
    except ValueError:
        print('Dimensiones inválidas...')
        quit()
    try:
        if filas <= 0 or columnas <= 0:
            raise Exception('Las dimensiones de la Matriz deben ser positivas')
    except Exception as x:
        print(x)
        quit()
    return filas, columnas

def createMatrix(filas, columnas):
    M = []
    for i in range(filas):
        M.append([0]*columnas)
    return M

def dataMatrix(M,name):
    filas = len(M)
    columnas = len(M[0])
    for i in range(filas):
        for j in range(columnas):
            while True:
                try:
                    M[i][j] = float (input(name + '[' + str(i) + ',' + str(j) + ']:\n'))
                except ValueError:
                    print('Valor invalido, vuelva a ingresar el dato...')
                    continue
                break
            os.system('cls')

def addMatrix(A,B):
    pass