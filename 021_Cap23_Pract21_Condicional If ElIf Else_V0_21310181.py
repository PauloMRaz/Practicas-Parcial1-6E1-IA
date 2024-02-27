#Paulo Enrique Muñoz Razón    21310181_E1      27/Febrero/2024
#Inteligencia artificial
#Capitulo 23 "Condicional IF ElIf Else"

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 1 and edad <= 18:
	print('Eres menor de edad.')
elif edad >= 18 and edad <= 45:
	print('Eres mayor de edad.')
elif edad >= 100 and edad <= 120:
        print('Eres una persona muy vieja')
else:
	print('Edad no válida.')
