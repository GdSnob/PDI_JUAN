#-----------------------------------
# Names: Octavio O. H. y Juan. L. L.
#Project Name:  Clasificador de imágenes
#-----------------------------------

import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_images_and_labels(base_directory, gamma_value):
    images = []
    labels = []
    label_dict = {}
    first_images = []  # Para almacenar una imagen de cada carpeta

    # Obtener la lista de subcarpetas
    for label, subdir in enumerate(os.listdir(base_directory)):
        subdir_path = os.path.join(base_directory, subdir)

        # Verificar que es un directorio
        if os.path.isdir(subdir_path):
            label_dict[subdir] = label  # Asignar un número de etiqueta a cada carpeta
            subdir_images = []

            # Obtener la lista de archivos en la subcarpeta
            for file_name in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, file_name)

                # Verificar que el archivo es una imagen
                if file_path.endswith(('jpg', 'jpeg', 'png', 'JPG')):
                    # Abrir la imagen, convertirla a RGB y a un arreglo NumPy
                    image = Image.open(file_path).convert('RGB')
                    image_array = np.array(image)

                    # Aplica gamma y agregalas al arreglo
                    image_gamma = operacion_gamma(image_array, gamma_value)

                    # Agregar la imagen y la etiqueta a las listas
                    subdir_images.append(image_gamma)
                    images.append(image_gamma)
                    labels.append(label)

            # Agregar una imagen representativa de cada carpeta
            if subdir_images:
                first_images.append(subdir_images[0])

    # Convertir las listas en arreglos NumPy
    images_array = np.array(images)
    labels_array = np.array(labels)
    first_images_array = np.array(first_images)

    return images_array, labels_array, label_dict, first_images_array

""" Funcion que aplica la operacion gamma, esto es para mejorar el brillo de las imagenes """
def operacion_gamma(imagen, gamma):
    # Normalizar los valores de la imagen a [0, 1]
    imagen_normalizada = imagen / 255.0
    # Aplicar la corrección gamma
    imagen_gamma = np.power(imagen_normalizada, gamma)
    # Escalar de nuevo a [0, 255]
    imagen_gamma = np.uint8(imagen_gamma * 255)
    return imagen_gamma

def mostrar_imagenes(first_images_array):
    plt.figure(figsize=(10, 10))
    num_images = len(first_images_array)

    for i in range(num_images):
        plt.subplot(3, 2, i + 1)  # 3 filas, 2 columnas
        plt.imshow(first_images_array[i])
        plt.axis('off')  # Ocultar los ejes

    plt.tight_layout()
    plt.show()

# Define el directorio base que contiene las subcarpetas con imágenes
base_directory = 'archive/Training'  # Reemplaza esto con la ruta a tu carpeta principal

# Valor de corrección gamma
gamma_value = 0.5  # Cambia este valor según la corrección que desees aplicar

# Cargar imágenes y etiquetas
images, labels, label_dict, first_images = load_images_and_labels(base_directory, gamma_value)

# Mostrar las imágenes
mostrar_imagenes(first_images)



