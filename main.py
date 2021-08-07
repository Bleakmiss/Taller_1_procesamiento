# Este codigo fue realizado por Daniel Barandica para la materia de procesamiento de imagenes y video.
# El codigo fue diseñado para mostrar las propiedades de una imagen, una version de la imagen a blanco y negro y una version de la imagen con un Hue especifico


# Se importa la libreria cv2 y la clase creada en el codigo basicColor
import cv2
from basicColor import basicColor as bc

# Se define la condicion para ejecutar solo una vez el codigo
if __name__ == '__main__':
    # INCISO B
    path=input("Ingrese la ruta de la imagen con que quiere trabajar: ") # Ruta de la imagen
    name= input("Ingrese el nombre de la imagen: ") # Nombre de la imagen

    # INCISO A
    imagen= bc(path,name) # Creacion de la clase con los dos parametros necesarios

    # INCISO C
    imagen.displayProperties() # Uso de metodo para mostrar las propiedades de la imagen

    # INCISO D
    imagen_gray=imagen.makeBW() # Uso de metodo para obtener la version de la imagen en blanco y negro
    cv2.imshow("Imagen a blanco y negro", imagen_gray) # Visualizacion de imagen en blanco y negro
    cv2.waitKey(0)

    # INCISO E
    h= int(input("Ingrese el valor del Hue que desea: ")) # Valor de H que ingresa el usuario
    imagen_hsv=imagen.colorize(h) # Uso de metodo para obtener version de la imagen con H ingresado por el usuario
    cv2.imshow("Imagen con el h dado", imagen_hsv) # Visualizacion de imagen con H ingresado
    cv2.waitKey(0)
