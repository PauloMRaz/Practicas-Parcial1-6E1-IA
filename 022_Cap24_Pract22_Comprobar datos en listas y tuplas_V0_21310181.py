#Paulo Enrique Muñoz Razón    21310181_E1      27/Febrero/2024
#Inteligencia artificial
#Capitulo 24 "Comprobar datos en listas y tuplas"

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

colores = ("rojo", "azul", "verde", "amarillo", "morado", "naranja")
entrada = input("Introduce un color:\n ")

if entrada in colores[0]:
    print("El rojo si se puede")
elif entrada in colores[1]:
    print("El azul si se puede")
elif entrada in colores[2]:
    print("El verde si se puede")
elif entrada in colores[3]:
    print("El amarillo si se puede")
elif entrada in colores[4]:
    print("El morado si se puede")
elif entrada in colores[5]:
    print("El naranja si se puede")
else:
    print("El color que pusiste no se puede")
