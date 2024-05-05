{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Reconocimiento de colores con numpy y openCV\n",
    "\n",
    "####"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Pulsa cualquier tecla para cerrar las ventanas\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# -*- coding: latin-1 -*-\n",
    "\"\"\"\n",
    "EJEMPLO 4 - Detectar múltiples colores\n",
    " \n",
    "Este código detecta los colores rojo, azul y amarillo en una imagen estática.\n",
    " \n",
    "Escrito por Glare y Transductor\n",
    "www.robologs.net\n",
    "\"\"\"\n",
    "import cv2\n",
    "import numpy as np\n",
    " \n",
    "#Cargamos la imagen:\n",
    "img = cv2.imread(\"taxis-colores.jpg\")\n",
    " \n",
    "#Convertimos la imagen a hsv:\n",
    "hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)\n",
    " \n",
    "#Establecemos el rango mínimo y máximo de HSV:\n",
    "# azul_bajos = np.array([100, 50, 50])\n",
    "# azul_altos = np.array([130, 255, 255])\n",
    "amarillo_bajos = np.array([20, 50, 50])\n",
    "amarillo_altos = np.array([40, 255, 255])\n",
    "# rojo_bajos = np.array([0, 50, 50])\n",
    "# rojo_altos = np.array([20, 255, 255])\n",
    "\n",
    " \n",
    "#Detectamos los píxeles que estén dentro del rango que hemos establecido:\n",
    "# mask_azul = cv2.inRange(hsv, azul_bajos, azul_altos)\n",
    "mask_amarillo = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)\n",
    "# mask_rojo = cv2.inRange(hsv, rojo_bajos, rojo_altos)\n",
    "\n",
    "#Detectamos los píxeles que estén dentro del rango que hemos establecido:\n",
    "mask = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)\n",
    " \n",
    "#Unimos estas dos mascaras:\n",
    "# mask_union = cv2.bitwise_or(mask_azul, mask_amarillo)\n",
    "\n",
    "\n",
    "#Eliminamos el ruido de esta nueva máscara:\n",
    "kernel = np.ones((6,6),np.uint8)\n",
    " \n",
    "#Eliminamos el ruido con un CLOSE seguido de un OPEN:\n",
    "mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)\n",
    "mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)\n",
    "\n",
    "# mask_union = cv2.morphologyEx(mask_union, cv2.MORPH_CLOSE, kernel)\n",
    "# mask_union = cv2.morphologyEx(mask_union, cv2.MORPH_OPEN, kernel)\n",
    " \n",
    "#Mostramos la imagen original y la máscara:\n",
    "cv2.imshow(\"Original\", img)\n",
    "cv2.imshow(\"Taxis\", mask)\n",
    "# cv2.imshow(\"Amarillo+Azul\", mask_union)\n",
    "\n",
    "\n",
    "print(\"\\nPulsa cualquier tecla para cerrar las ventanas\\n\")\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
