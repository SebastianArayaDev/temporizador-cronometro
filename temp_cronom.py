import time

def temporizador(num_seg):
    while num_seg:
        m, s = divmod(num_seg, 60)
        min_seg_format = '{:02d}:{:02d}'.format(m, s)
        print(min_seg_format, end='\r')
        time.sleep(1)
        num_seg -= 1

    print('Temporizador Finalizado.\n')


def cronometro():
    inicio = time.time()

    input('Presiona ENTER para detener el cronómetro...\n')

    fin = time.time()
    tiempo_transcurrido = fin - inicio

    mins, secs = divmod(tiempo_transcurrido, 60)
    tiempo_formato = '{:02d}:{:05.2f}'.format(int(mins), secs)
    print('Tiempo transcurrido:', tiempo_formato, "\n")


def menu():
    while True:
        print("====================")
        print("|       MENU       |")
        print("====================\n")
        print("")
        print("[1] Temporizador  |  [2] Cronometro  |  [3] Salir\n")
        print("")
        opcion = int(input("Ingrese la opcion a elegir: "))
        if opcion == 1:
            op = input("\nIngrese los segundos para el temporizador: ")
            print("")
            temporizador(int(op))
        elif opcion == 2:
            print("")
            cronometro()
        elif opcion == 3:
            break
        else:
            print("Opcion invalida.")

menu()