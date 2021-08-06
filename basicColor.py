#Importado de librerias utilizadas en el codigo
import cv2
import os
import numpy as np

#Declaracion de clase con nombre basicColor
class basicColor:

    #Metodo constructor donde se guarda la imagen al ingresar los dos parametros requeridos (ruta de imagen y nombre de imagen)
    def __init__(self, path, image_name):
        path_file = os.path.join(path, image_name)
        self.image=cv2.imread(path_file) #Guardado de imagen

    #Metodo displayProperties donde se mostrara el numero de pixeles de la imagen en unidades de Mega y el numero de canales de la imagen
    def displayProperties(self):
        pixeles= self.image.size #Numero de pixeles
        canales=self.image.shape #Canales de la imagen
        print("El numero de pixeles de las imagenes es: ",(pixeles)/1000000,"MP y el numero de canales de la imagen es:",canales[2]) #Impresion de las caracteristicas

    #Metodo makeBW para convertir la imagen en blanco y negro
    def makeBW(self):
        image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY) #Conversion de imagen a blanco y negro
        ret, Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_OTSU) #Aplicacion de metodo de umbralizacion otsu
        return(Ibw_otsu) #Se devuelve la imagen en blanco y negro umbralizada

    #Metodo colorize para convertir la imagen con el h ingresado por el usuario
    def colorize(self,h):
        image_hsv=cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV) #Conversion de imagen a HSV con H ingresado
        h1, s, v = cv2.split(image_hsv) #Division de la imagen en cada uno de sus canales
        h2 = h * np.ones_like(s) # Creacion de vector para H con el valor ingresado
        image_hsv2 = cv2.merge((h2, s, v)) # Union de los canales para imagen HSV con el H del usuario
        image_hsv_bgr = cv2.cvtColor(image_hsv2, cv2.COLOR_HSV2BGR) #Conversion de imagen HSV a RGB
        return(image_hsv_bgr) #Se devuelve la imagen en HSV

