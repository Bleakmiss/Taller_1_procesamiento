import cv2
import os
import numpy as np

class basicColor:

    def __init__(self, path, image_name):
        path_file = os.path.join(path, image_name)
        self.image=cv2.imread(path_file)

    def displayProperties(self):
        pixeles= self.image.size
        canales=self.image.shape
        print("El numero de pixeles de las imagenes es: ",(pixeles)/1000000,"M y el numero de canales de la imagen es:",canales)

    def makeBW(self):
        image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        ret, Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return(Ibw_otsu)

    def colorize(self,h):
        image_hsv=cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        h1, s, v = cv2.split(image_hsv)
        h2 = h * np.ones_like(s)
        image_hsv2 = cv2.merge((h2, s, v))
        image_hsv_bgr = cv2.cvtColor(image_hsv2, cv2.COLOR_HSV2BGR)
        return(image_hsv_bgr)
