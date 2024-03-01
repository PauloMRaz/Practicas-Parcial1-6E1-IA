#Paulo Enrique Muñoz Razón    21310181_E1      1/Marzo/2024
#Inteligencia artificial
#Capitulo 35 "args-Argumentos arbitrarios"

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores('rojo', 'azul')

def suma(*args):
	resultado = args[0] + args[1] + args[2] + args[3] + args[4]
	print('El resultado de sumar estos cinco números es:', resultado)

suma(5, 7, 45, 8657, 3, 4)
