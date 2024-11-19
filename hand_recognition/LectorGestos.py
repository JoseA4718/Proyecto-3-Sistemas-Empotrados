#------------------------------ Importamos las librerias ----------------------------------------
import cv2
import numpy as np
import SeguimientoManos as sm  #Programa que contiene la deteccion y seguimiento de manos

#-------------------------------SERVER-----------------------------------------------------------
import requests

url = "https://ejemplo.com/api"
accion = ""
payload = {"accion":accion}
estado = "pausado"
0

#---------------------------------Declaracion de variables---------------------------------------
anchocam, altocam = 640, 480
cuadro = 100 #Rango donde podemos interactura
sua = 5
pubix, pubiy = 0,0
cubix, cubiy = 0,0
#print(anchopanta, anchocam)

#----------------------------------- Lectura de la camara----------------------------------------
cap = cv2.VideoCapture(0)
cap.set(3,anchocam)  #Definiremos un ancho y un alto definido para siempre
cap.set(4,altocam)

#------------------------------------ Declaramos el detector -----------------------------
detector = sm.detectormanos(hands=1) #Ya que solo vamos a utilizar una mano

while True:
    #----------------- Vamos a encontrar los puntos de la mano -----------------------------
    ret, frame = cap.read()
    frame = detector.find_hands(frame)  #Encontramos las manos
    lista, bbox = detector.find_position(frame) #Mostramos las posiciones

    #-----------------Obtener la punta del dedo indice y corazon----------------------------
    if len(lista) != 0:
        x1, y1 = lista[8][1:]                  #Extraemos las coordenadas del dedo indice
        x2, y2 = lista[12][1:]                 #Extraemos las coordenadas del dedo corazon
        #print(x1,y1,x2,y2)

        #----------------- Comprobar que dedos estan arriba --------------------------------
        dedos = detector.fingers_up() #Contamos con 5 posiciones nos indica si levanta cualquier dedo
        #print(dedos)
        cv2.rectangle(frame, (cuadro, cuadro), (anchocam - cuadro, altocam - cuadro), (0, 0, 0), 2)  # Generamos cuadro
        #-----------------Modo movimiento: solo dedo indice-------------------------------------
        if dedos[1]== 1 and dedos[2] == 0 and dedos[3] == 0:  #Si el indice esta arriba pero el corazon esta abajo
            #print("play/pause")
            if accion != "play" and accion != "pausa":
                if estado == "pausado":
                    accion = "play"
                    estado = "play"
                else:
                    accion = "pausa"
                    estado = "pausado"
                try:
                    #response = requests.post(url, json=payload)
                    print(f"se envio la vara de prueba con el estado: {accion}")
                    #print(f"Acción enviada: {accion}, Código de estado: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"Error al enviar la acción: {e}")

        #----------------------------- Comprobar si esta en modo click -------------------------
        elif dedos[1] == 1 and dedos[2] == 1 and dedos[3] == 0:  # Si el indice esta arriba y el corazon tambien
            #print("siguiente")
            if accion != "siguiente":
                accion = "siguiente"
                try:
                    print(f"se envio la vara de prueba con el estado: {accion}")
                    #response = requests.post(url, json=payload)
                    #print(f"Acción enviada: {accion}, Código de estado: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"Error al enviar la acción: {e}") 

        elif dedos[1] == 1 and dedos[2] == 1 and dedos[3] == 1:  # Si el indice esta arriba y el corazon tambien
            #print("anterior")
            if accion != "anterior":
                accion = "anterior"
                try:
                    print(f"se envio la vara de prueba con el estado: {accion}")
                    #response = requests.post(url, json=payload)
                    #print(f"Acción enviada: {accion}, Código de estado: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"Error al enviar la acción: {e}") 

        elif dedos[1]== 0 and dedos[2] == 0 and dedos[3] == 0:
            accion = None 

    cv2.imshow("Mouse", frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
