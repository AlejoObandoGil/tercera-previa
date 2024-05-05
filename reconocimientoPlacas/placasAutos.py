{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "area= 9007.0\n",
      "PLACA:  \n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# RECONOCIMIENTO DE PLACA. COCHE: auto001.jpg\n",
    "\n",
    "# Instalación de OpenCV\n",
    "# pip install opencv-contrib-python\n",
    "\n",
    "# Instalación de la librería de Tesseract\n",
    "# pip install pytesseract\n",
    "\n",
    "# Instalación del programa Tesseract\n",
    "# Instalar el programa Tesseract.exe\n",
    "\n",
    "# Importar librería OpenCV\n",
    "import cv2\n",
    "\n",
    "# Importar Librería para reconocimiento de caracteres\n",
    "import pytesseract\n",
    "\n",
    "# Direccionar a programa Tesseract instalado\n",
    "pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'\n",
    "\n",
    "placa = []\n",
    "\n",
    "# Lectura de la imagen\n",
    "image = cv2.imread('auto001.jpg')\n",
    "\n",
    "# Conversión a escala de grises\n",
    "gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "# Proceso de suavizado de la imagen\n",
    "gray = cv2.blur(gray,(3,3))\n",
    "\n",
    "# Algoritmo de detección de bordes\n",
    "canny = cv2.Canny(gray,150,200)\n",
    "\n",
    "# Algoritmo para resaltar los bordes detectados\n",
    "canny = cv2.dilate(canny,None,iterations=1)\n",
    "\n",
    "# Algoritmo para unir de manera continua los contornos\n",
    "# Encuentra todos los contornos presentes en la imagen\n",
    "#_,cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)\n",
    "cnts,_ = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)\n",
    "\n",
    "# Función para dibujar todos los contornos encontrados\n",
    "#cv2.drawContours(image,cnts,-1,(0,255,0),2)\n",
    "for c in cnts:\n",
    "  # Encuentra el área del contorno\n",
    "  area = cv2.contourArea(c)\n",
    "    \n",
    "  # Calcula el rectángulo del contorno\n",
    "  x,y,w,h = cv2.boundingRect(c)\n",
    "  epsilon = 0.09*cv2.arcLength(c,True)\n",
    "  approx = cv2.approxPolyDP(c,epsilon,True)\n",
    "\n",
    "  # Si tiene 4 vértices y un área aproximada de 9000, parece una placa\n",
    "  if len(approx)==4 and area>9000:\n",
    "        \n",
    "    # Imprime el área\n",
    "    print('area=',area)\n",
    "    \n",
    "    # Calcula la relación anchura-altura\n",
    "    #cv2.drawContours(image,[approx],0,(0,255,0),3)\n",
    "    aspect_ratio = float(w)/h\n",
    "    \n",
    "    # Si la relación es 2.4, el rectángulo es muy parecido a la placa\n",
    "    if aspect_ratio>2.4:\n",
    "    \n",
    "      # En las siguientes instrucciones se imprimen los datos de la placa \n",
    "      # y se la muestra en una ventana\n",
    "      placa = gray[y:y+h,x:x+w]\n",
    "      \n",
    "      # Se extrae el texto asociado a la placa utilizando Tesseract\n",
    "      text = pytesseract.image_to_string(placa,config='--psm 11')\n",
    "    \n",
    "      # Se imprime la texto de la placa encontrada\n",
    "      print('PLACA: ',text)\n",
    "    \n",
    "      # Se muestra una imagen de la placa\n",
    "      cv2.imshow('PLACA',placa)\n",
    "    \n",
    "      # Se agrega un texto a la imagen, indicando los datos encontrados\n",
    "      cv2.moveWindow('PLACA',780,10)\n",
    "      cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)\n",
    "      cv2.putText(image,text,(x-20,y-10),1,2.2,(0,255,0),3)\n",
    "\n",
    "# Se muestran los datos obtenidos\n",
    "cv2.imshow('Image',image)\n",
    "cv2.moveWindow('Image',45,10)\n",
    "cv2.waitKey(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
 "nbformat_minor": 4
}
