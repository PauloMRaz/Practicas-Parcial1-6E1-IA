#Paulo Enrique Muñoz Razón    21310181_E1      1/Marzo/2024
#Inteligencia artificial
#Capitulo 33 "Metodos con diccionario"

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

del teclado1
del teclado2['Categoría']
del teclado2['Precio']

print(teclado2['Modelo'])
