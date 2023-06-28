import cv2
import mediapipe as mp
import numpy as np
from math import acos, degrees

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

#cap = cv2.VideoCapture("video_001.mp4")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cap = cv2.VideoCapture("sentadilla.mp4")
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

          if results.pose_landmarks is not None:
               x1 = int(results.pose_landmarks.landmark[11].x * width)
               y1 = int(results.pose_landmarks.landmark[11].y * height)

               x2 = int(results.pose_landmarks.landmark[13].x * width)
               y2 = int(results.pose_landmarks.landmark[13].y * height)

               x3 = int(results.pose_landmarks.landmark[15].x * width)
               y3 = int(results.pose_landmarks.landmark[15].y * height)

               p1 = np.array([x1, y1])
               p2 = np.array([x2, y2])
               p3 = np.array([x3, y3])

               l1 = np.linalg.norm(p2 - p3)
               l2 = np.linalg.norm(p1 - p3)
               l3 = np.linalg.norm(p1 - p2)

               #verficar q los puntos esten dentro de la pantalla
               #con el .shape de la pantalla
               #y si estan adentro recien hacer la deteccion y el calculo del angulo

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
          cv2.imshow("Frame", frame)
          if cv2.waitKey(1) & 0xFF == 27:
               break

cap.release()
cv2.destroyAllWindows()

#sugerencia de interfaz, hacer un main q contenga q si apreto cierta tecla, yo pueda hacer que se ponga en funcionamiento cualquiera de mis 5 codigos para hacer los ejercicios.