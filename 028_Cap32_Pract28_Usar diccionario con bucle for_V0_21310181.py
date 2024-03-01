#Paulo Enrique Muñoz Razón    21310181_E1      1/Marzo/2024
#Inteligencia artificial
#Capitulo 32 "Usar diccionarios con el bucle for"

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

for x,y in teclado1.items():
    print(x,"= ",y,".")

#for x in teclado1:
	#print(x, '=', teclado1[x] + '.')
