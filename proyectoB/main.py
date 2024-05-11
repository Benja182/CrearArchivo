from funciones import *


def menu():
    cadena = '=' * 100 + '\n' + \
             'Menu de Opciones\n' + \
             '1. Cargar datos de deptos en archivo.\n' + \
             '2. Mostrar datos de archivo.\n' + \
             '3. Generar vector a base del archivo.\n' + \
             '4. Buscar un nombre.\n' + \
             '5. Crear arreglo de montos por archivo binario.\n' + \
             'Ingrese la opcion que desea realizar: '

    return int(input(cadena))


def main():
    opcion = -1
    deptos = []
    archivo = 'deptos.aed'

    while opcion != 0:
        if opcion != -1:
            t.sleep(2)
        opcion = menu()

        if opcion == 1:
            crear_archivo(archivo)

        elif os.path.exists(archivo):

            if opcion == 2:
                mostrar_archivo(archivo)

            elif opcion == 3:
                deptos = importar_a_vector(archivo)

            elif opcion == 4:
                busqueda(archivo)

            elif len(deptos) != 0:

                if opcion == 5:
                    generar_matriz(deptos)

            else:
                print('No se ha cargado nada en la opcion 4.')

        else:
            print('Todavia no se cargo ningun dato en la opcion 1.')


if __name__ == '__main__':
    main()
