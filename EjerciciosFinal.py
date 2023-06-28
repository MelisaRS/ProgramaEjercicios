# Importamos librerias
from tkinter import *
from PIL import Image, ImageTk
import cv2
import imutils
import mediapipe as mp
import numpy as np
from math import acos, degrees

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose



# Funcion Visualizar
def visualizar():
    up = False
    down = False
    count = 0

    global pantalla, frame, squats, dumbbells, elevations, polychinellas, abdominals 
    # Leemos la videocaptura
    if cap is not None:
        ret, frame = cap.read()

        # Si es correcta
        if ret == True:

            if (squats == 1 and dumbbells == 0 and elevations == 0 and polychinellas == 0 and abdominals == 0):
                with mp_pose.Pose(static_image_mode=False) as pose:
                    frame = cv2.flip(frame, 1)
                    height, width, _ = frame.shape
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    results = pose.process(frame_rgb)

                    if results.pose_landmarks is not None:
                        x1 = int(results.pose_landmarks.landmark[24].x * width)
                        y1 = int(results.pose_landmarks.landmark[24].y * height)

                        x2 = int(results.pose_landmarks.landmark[26].x * width)
                        y2 = int(results.pose_landmarks.landmark[26].y * height)

                        x3 = int(results.pose_landmarks.landmark[28].x * width)
                        y3 = int(results.pose_landmarks.landmark[28].y * height)

                        p1 = np.array([x1, y1])
                        p2 = np.array([x2, y2])
                        p3 = np.array([x3, y3])

                        l1 = np.linalg.norm(p2 - p3)
                        l2 = np.linalg.norm(p1 - p3)
                        l3 = np.linalg.norm(p1 - p2)

                        # Calcular el ángulo
                        angle = degrees(acos((l1**2 + l3**2 - l2**2) / (2 * l1 * l3)))
                        if angle >= 160:
                                up = True
                        if up == True and down == False and angle <= 100:
                                down = True
                        if up == True and down == True and angle >= 160:
                                count += 1
                                up = False
                                down = False

                        #print("count: ", count)
                        # Visualización
                        aux_image = np.zeros(frame.shape, np.uint8)
                        cv2.line(aux_image, (x1, y1), (x2, y2), (255, 255, 0), 20)
                        cv2.line(aux_image, (x2, y2), (x3, y3), (255, 255, 0), 20)
                        cv2.line(aux_image, (x1, y1), (x3, y3), (255, 255, 0), 5)
                        contours = np.array([[x1, y1], [x2, y2], [x3, y3]])
                        cv2.fillPoly(aux_image, pts=[contours], color=(128, 0, 250))

                        output = cv2.addWeighted(frame, 1, aux_image, 0.8, 0)

                        cv2.circle(output, (x1, y1), 6, (0, 255, 255), 4)
                        cv2.circle(output, (x2, y2), 6, (128, 0, 250), 4)
                        cv2.circle(output, (x3, y3), 6, (255, 191, 0), 4)
                        cv2.rectangle(output, (0, 0), (60, 60), (255, 255, 0), -1)
                        cv2.putText(output, str(int(angle)), (x2 + 30, y2), 1, 1.5, (128, 0, 250), 2)
                        cv2.putText(output, str(count), (10, 50), 1, 3.5, (128, 0, 250), 2)
                        cv2.imshow("output", output)


            elif (squats == 0 and dumbbells == 1 and elevations == 0 and polychinellas == 0 and abdominals == 0):
                # Color HSV
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            elif (squats == 0 and dumbbells == 0 and elevations == 1 and polychinellas == 0 and abdominals == 0):
                # Color GRAY
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            elif (squats == 0 and dumbbells == 0 and elevations == 0 and polychinellas == 1 and abdominals == 0):
                # Color GRAY
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            elif (squats == 0 and dumbbells == 0 and elevations == 0 and polychinellas == 0 and abdominals == 1):
                # Color GRAY
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Rendimensionamos el video
            frame = imutils.resize(frame, width=640)

            # Convertimos el video
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            # Mostramos en el GUI
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(10, visualizar)

        else:
            cap.release()

# Para elegir el ejercicio adecuado
def squatsF():
    global squats, dumbbells, elevations, polychinellas, abdominals
    # Ejercicios
    squats = 1
    dumbbells = 0
    elevations = 0
    polychinellas = 0
    abdominals = 0

def dumbbellsF():
    global squats, dumbbells, elevations, polychinellas, abdominals
    # Ejercicios
    squats = 0
    dumbbells = 1
    elevations = 0
    polychinellas = 0
    abdominals = 0

# GRAY
def elevationsF():
    global squats, dumbbells, elevations, polychinellas, abdominals
    # Ejercicios
    squats = 0
    dumbbells = 0
    elevations = 1
    polychinellas = 0
    abdominals = 0

def polychinellasF():
    global squats, dumbbells, elevations, polychinellas, abdominals
    # Ejercicios
    squats = 0
    dumbbells = 0
    elevations = 0
    polychinellas = 1
    abdominals = 0

def abdominalsF():
    global squats, dumbbells, elevations, polychinellas, abdominals
    # Ejercicios
    squats = 0
    dumbbells = 0
    elevations = 0
    polychinellas = 0
    abdominals = 1

# Funcion iniciar
def iniciar():
    global cap
    # Elegimos la camara
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    visualizar()
    print("Estamos iniciando la camara")

# Funcion finalizar
def finalizar():
    cap.release()
    cv2.DestroyAllWindows()
    print("FIN")


# Variables
cap = None
squats = 1
dumbbells = 0
elevations = 0
polychinellas = 0
abdominals = 0


#  Ventana Principal
# Pantalla
pantalla = Tk()
pantalla.title("Ejercicios")
pantalla.geometry("1280x720")  # Asignamos la dimension de la ventana

# Fondo
imagenF = PhotoImage(file="Fondo.png")
background = Label(image = imagenF, text = "Fondo")
background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

# Interfaz
texto1 = Label(pantalla, text="VIDEO EN TIEMPO REAL: ")
texto1.place(x = 580, y = 10)

texto2 = Label(pantalla, text="CONVERSION DE COLOR: ")
texto2.place(x = 1010, y = 100)

texto3 = Label(pantalla, text="DETECCION DE COLOR: ")
texto3.place(x = 110, y = 100)

# Botones
# Iniciar Video
imagenBI = PhotoImage(file="Inicio.png")
inicio = Button(pantalla, text="Iniciar", image=imagenBI, height="40", width="200", command=iniciar)
inicio.place(x = 100, y = 580)

# Finalizar Video
imagenBF = PhotoImage(file="Finalizar.png")
fin = Button(pantalla, text="Finalizar", image= imagenBF, height="40", width="200", command=finalizar)
fin.place(x = 980, y = 580)

# HSV
imagenBH = PhotoImage(file="hsv.png")
bhsv = Button(pantalla, text="Sentadillas", image= imagenBH, height="40", width="200", command=squatsF)
bhsv.place(x = 980, y = 150)
# RGB
imagenBR = PhotoImage(file="rgb.png")
brgb = Button(pantalla, text="Mancuernas", image= imagenBR, height="40", width="200", command=dumbbellsF)
brgb.place(x = 980, y = 200)
# GRAY
imagenBG = PhotoImage(file="gray.png")
grayb = Button(pantalla, text="Elevaciones", image= imagenBG, height="40", width="200", command=elevationsF)
grayb.place(x = 980, y = 250)

imagenBG = PhotoImage(file="gray.png")
grayb = Button(pantalla, text="RGB", image= imagenBG, height="40", width="200", command=polychinellasF)
grayb.place(x = 980, y = 300)

imagenBG = PhotoImage(file="gray.png")
grayb = Button(pantalla, text="RGB", image= imagenBG, height="40", width="200", command=abdominalsF)
grayb.place(x = 980, y = 350)


# Video
lblVideo = Label(pantalla)
lblVideo.place(x = 320, y = 50)


pantalla.mainloop()


