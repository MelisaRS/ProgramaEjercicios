import cv2
import poseAbdominales 
import poseElevacionPiernas 
import poseMancuerna
import posePolichinela 
import poseSentadilla

def menu_principal():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    print("Seleccione el ejercicios que desea realizar:")
    print("1. Abdominales")
    print("2. Elevacion de piernas")
    print("3. Brazos con Mancuerna")
    print("4. Polichinelas")
    print("5. Sentadillas")
    print("ESC. Salir")

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        # Dibujar el menú en la imagen
        cv2.rectangle(frame, (50, 75), (550, 350), (255, 255, 0), -1)
        cv2.putText(frame, "Escoja el ejercicio que desea realizar", (70, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (128, 0, 250), 2)
        cv2.putText(frame, "1. Abdominales", (70, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (128, 0, 250), 2)
        cv2.putText(frame, "2. Elevacion de Piernas", (70, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (128, 0, 250), 2)
        cv2.putText(frame, "3. Brazos con Mancuernas", (70, 220), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (128, 0, 250), 2)
        cv2.putText(frame, "4. Polichinelas", (70, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (128, 0, 250), 2)
        cv2.putText(frame, "5. Sentadillas", (70, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (128, 0, 250), 2)
        cv2.putText(frame, "Esc. Salir", (70, 340), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (128, 0, 250), 2)
        
        cv2.imshow("Camara para hacer Ejercicios", frame)
               

        key = cv2.waitKey(1)
        if key == 49:  # Tecla "1"
            cv2.destroyAllWindows()
            cap.release()
            poseAbdominales.abdominales()
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        elif key == 50:  # Tecla "2"
            cv2.destroyAllWindows()
            cap.release()
            poseElevacionPiernas.elevacion()
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        elif key == 51:  # Tecla "3"
            cv2.destroyAllWindows()
            cap.release()
            poseMancuerna.mancuernas()
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        elif key == 52:  # Tecla "4"
            cv2.destroyAllWindows()
            cap.release()
            posePolichinela.polichinelas()
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        elif key == 53:  # Tecla "5"
            cv2.destroyAllWindows()
            cap.release()
            poseSentadilla.sentadillas()
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        elif key == 27:  # Tecla "ESC"
                    break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    menu_principal()