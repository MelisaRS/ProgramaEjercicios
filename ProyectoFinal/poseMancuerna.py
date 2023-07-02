import cv2
import mediapipe as mp
import numpy as np
from math import acos, degrees

def mancuernas():
     
     #para dibujar anotaciones en imágenes o frames. Estas funciones 
     #se utilizan para visualizar los resultados obtenidos mediante MediaPipe.
     mp_drawing = mp.solutions.drawing_utils
     
     #es un modelo preentrenado de MediaPipe para detectar y estimar poses 
     # humanas en imágenes o frames. Proporciona métodos y funciones para procesar imágenes 
     # y obtener los landmarks (puntos de referencia) correspondientes a las articulaciones 
     # y partes del cuerpo humano
     mp_pose = mp.solutions.pose

     #cap = cv2.VideoCapture("video_001.mp4")
     #cap = cv2.VideoCapture("sentadilla.mp4")
     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
     
     up = False
     down = False
     count = 0
     with mp_pose.Pose(
          static_image_mode=False) as pose:

          while True:
               ret, frame = cap.read()
               if ret == False:
                    break
               frame = cv2.flip(frame, 1)
               height, width, _ = frame.shape
               frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
               results = pose.process(frame_rgb)

               #si no es nula -> garantiza que se hayan detectado landmarks 
               # de la pose antes de realizar operaciones adicionales
               # o cálculos basados en esos landmarks.
               if results.pose_landmarks is not None:
                    x1 = int(results.pose_landmarks.landmark[11].x * width)
                    y1 = int(results.pose_landmarks.landmark[11].y * height)

                    x2 = int(results.pose_landmarks.landmark[13].x * width)
                    y2 = int(results.pose_landmarks.landmark[13].y * height)

                    x3 = int(results.pose_landmarks.landmark[15].x * width)
                    y3 = int(results.pose_landmarks.landmark[15].y * height)

                    # Verificar si los puntos están dentro del tamaño de la pantalla
                    if 0 <= x1 < width and 0 <= y1 < height and 0 <= x2 < width and 0 <= y2 < height and 0 <= x3 < width and 0 <= y3 < height:
                    
                         # Realizando los cálculos
                         #Creamos un vector
                         p1 = np.array([x1, y1])
                         p2 = np.array([x2, y2])
                         p3 = np.array([x3, y3])

                         #la longitud del vector resultante con la norma Euclidiana del vector
                         l1 = np.linalg.norm(p2 - p3)
                         l2 = np.linalg.norm(p1 - p3)
                         l3 = np.linalg.norm(p1 - p2)

                         # Calcular el ángulo
                         angle = degrees(acos((l1**2 + l3**2 - l2**2) / (2 * l1 * l3)))
                         if angle >= 160:
                              up = True
                         if up == True and down == False and angle <= 90:
                              down = True
                         if up == True and down == True and angle >= 160:
                              count += 1
                              up = False
                              down = False

                         #print("count: ", count)

                         # Visualización
                         aux_image = np.zeros(frame.shape, np.uint8) #matriz de ceros #tipo de datos de 8 bits sin signo (0-255) para pintarlo
                         cv2.line(aux_image, (x1, y1), (x2, y2), (255, 255, 0), 20)
                         cv2.line(aux_image, (x2, y2), (x3, y3), (255, 255, 0), 20)
                         cv2.line(aux_image, (x1, y1), (x3, y3), (255, 255, 0), 5)
                         contours = np.array([[x1, y1], [x2, y2], [x3, y3]])
                         cv2.fillPoly(aux_image, pts=[contours], color=(128, 0, 250)) #rellena un polígono en la imagen 

                         output = cv2.addWeighted(frame, 1, aux_image, 0.8, 0) #una combinación ponderada de dos imágenes, frame y aux_image

                         cv2.circle(output, (x1, y1), 6, (0, 255, 255), 4)
                         cv2.circle(output, (x2, y2), 6, (128, 0, 250), 4)
                         cv2.circle(output, (x3, y3), 6, (255, 191, 0), 4)
                         cv2.rectangle(output, (0, 0), (60, 60), (255, 255, 0), -1)
                         cv2.putText(output, str(int(angle)), (x2 + 30, y2), 1, 1.5, (128, 0, 250), 2)
                         cv2.putText(output, str(count), (10, 50), 1, 3.5, (128, 0, 250), 2)

                         cv2.rectangle(output, (100, 0), (600, 40), (255, 255, 0), -1)
                         cv2.putText(output, "Ejercicios de Mancuernas", (110, 30), 1, 2, (128, 0, 250), 2 )
                         
                         cv2.imshow("Ejercicios de Brazos con Mancuernas", output)
               
               cv2.rectangle(frame,(0, 0), (500, 80), (255, 255, 0), -1)
               cv2.putText(frame, "Por favor posicionarse ", (10, 30), 1, 2, (128, 0, 250), 2 )
               cv2.putText(frame, "dentro de la camara", (10, 60), 1, 2, (128, 0, 250), 2 )
               
               cv2.imshow("Frame Mancuernas", frame)
               if cv2.waitKey(1) & 0xFF == 27:
                    break

     cap.release()
     cv2.destroyAllWindows()

