import os
import time as t
import pickle as p
import random as r
import registro as reg


def crear_archivo(nombre_archivo):
    nombres = ['Rami', 'Benja', 'Bruno', 'Fiama', 'Cami', 'Lauti', 'Juan', 'Jose', 'Sofi', 'Cande', 'Leo', 'Lucas', 'Tomi', 'Leandro', 'Mateo', 'Ezequiel', 'Matias', 'Gonzalo', 'Lucia', 'Azul', 'Anto', 'Ludmila', 'Luz', 'Monica', 'Gabi', 'Vale']

    n = int(input('Ingrese cuantos registros desea agregar: '))
    m = open(nombre_archivo, 'ab')

    for i in range(n):
        p.dump(reg.Depto(r.randint(500, 999), r.choice(nombres), r.randint(1, 12), r.randint(0, 4), r.randint(1000, 3000)), m)

    m.close()

    print('Los datos fueron agregados con exito al archivo')


def mostrar_archivo(nombre_archivo):
    m = open(nombre_archivo, 'rb')
    t = os.path.getsize(nombre_archivo)

    texto = '-' * 118 + '\n' + \
            '|{:^20}\t|{:^20}\t|{:^20}\t|{:^20}\t|{:^20}|\n'.format('Numero Ident', 'Nombre', 'Piso', 'Codigo', 'Monto') + \
            '-' * 118 + '\n'

    while m.tell() < t:
        texto += reg.to_string(p.load(m))

    m.close()

    print(texto)


def importar_a_vector(nombre_archivo):
    vector = []
    m = open(nombre_archivo, 'rb')
    t = os.path.getsize(nombre_archivo)

    while m.tell() < t:
        add_in_order(p.load(m), vector)

    print('El vector fue creado con exito.')
    return vector


def add_in_order(registro, vector):
    izq, der = 0, len(vector) - 1
    pos = -1

    while izq < der:
        c = (izq + der) // 2
        if registro.num_ident == vector[c].num_ident:
            pos = c
            break

        if registro.num_ident < vector[c].num_ident:
            der = c - 1

        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vector[pos:pos] = [registro]


def busqueda(nombre_archivo):
    filtrar = input('Ingrese el nombre que desea filtrar: ')
    filtro = []
    m = open(nombre_archivo, 'rb')
    t = os.path.getsize(nombre_archivo)

    while m.tell() < t:
        registro = p.load(m)
        if registro.nombre == filtrar:
            filtro.append(registro)

    print(mostrar_vector(filtro))


def mostrar_vector(vector):
    texto = '-' * 118 + '\n' + \
            '|{:^20}\t|{:^20}\t|{:^20}\t|{:^20}\t|{:^20}|\n'.format('Numero Ident', 'Nombre', 'Piso', 'Codigo', 'Monto') + \
            '-' * 118 + '\n'

    for registro in vector:
        texto += reg.to_string(registro)

    return texto


def generar_matriz(vector):
    matriz = [[0] * 12 for i in range(5)]
    for registro in vector:
        fila = registro.codigo
        columna = registro.piso - 1
        matriz[fila][columna] += registro.monto

    mostrar_matriz(matriz)


def mostrar_matriz(matriz):
    for fila in range(len(matriz)):
        print()
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] != 0:
                print(f'Para el codigo {fila}, el piso {columna + 1} junta {matriz[fila][columna]} pesos.')
