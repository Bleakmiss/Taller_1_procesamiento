import cv2
from basicColor import basicColor as bc
#hola
if __name__ == '__main__':
    path=input("Ingrese la ruta de la imagen con que quiere trabajar: ")
    name= input("Ingrese el nombre de la imagen: ")
    #F:\Descargas
    #lena.png
    imagen= bc(path,name)

    imagen.displayProperties()
    cv2.imshow("Imagen a blanco y negro", imagen.makeBW())
    cv2.waitKey(0)
    h= int(input("Ingrese el valor del Hue que desea: "))

    imagen_hsv=imagen.colorize(h)

    cv2.imshow("Imagen a blanco y negro", imagen_hsv)
    cv2.waitKey(0)
