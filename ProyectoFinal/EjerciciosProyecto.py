import poseAbdominales 
import poseElevacionPiernas 
import poseMancuerna
import posePolichinela 
import poseSentadilla

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1: Ejercicio de Abdominales', accion1),
        '2': ('Opción 2: Ejercicio de Elevacion de Piernas', accion2),
        '3': ('Opción 3: Ejercicios de Brazos con Mancuerna', accion3),
        '4': ('Opción 4: Ejercicios de Polichinelas', accion4),
        '5': ('Opción 5: Ejercicios de Sentadillas', accion5),
        '6': ('Salir', salir)
    }

    generar_menu(opciones, '6')


def accion1():
    print('Has elegido la opción 1 - Ejercicio de Abdominales')
    poseAbdominales.abdominales()


def accion2():
    print('Has elegido la opción 2 - Ejercicio de Elevacion de Piernas')
    poseElevacionPiernas.elevacion()


def accion3():
    print('Has elegido la opción 3 - Ejercicios de Brazos con Mancuerna')
    poseMancuerna.mancuernas()

def accion4():
    print('Has elegido la opción 4 - Ejercicios de Polichinelas')
    posePolichinela.polichinelas()

def accion5():
    print('Has elegido la opción 5 - Ejercicios de Sentadillas')
    poseSentadilla.sentadillas()


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()