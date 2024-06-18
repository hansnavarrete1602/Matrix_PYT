from Matrix_PYT import Matrix as M


def main():
    filas = int(input('Ingrese el tamaño de las filas: '))
    columnas = int(input('Ingrese el tamaño de las columnas: '))
    nombre = input('Ingrese el nombre de la Matriz: ')
    m1 = M([filas,columnas],nombre)
    M.dataMatrix(m1)

    filas = int(input('Ingrese el tamaño de las filas: '))
    columnas = int(input('Ingrese el tamaño de las columnas: '))
    nombre = input('Ingrese el nombre de la Matriz: ')
    m2 = M([filas,columnas],nombre)
    M.dataMatrix(m2)

    resultado = m1.add(m2)
    resultado2 = m1.product(m2)
    m1.show()
    print('\n')
    m2.show()
    print('\n')
    print('Suma:')
    print(resultado)
    print('\n')
    print('Multiplicacion:')
    print(resultado2)


main()
