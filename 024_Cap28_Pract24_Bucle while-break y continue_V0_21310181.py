#Paulo Enrique Muñoz Razón    21310181_E1      28/Febrero/2024
#Inteligencia artificial
#Capitulo 28 "El bucle While break y continue"

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

x = 0
while x <= 30:
    x += 1
    
    if x == 4 or x == 6 or x == 10:
        print('Se salto el valor ', x, ' de x')
        continue
    
    if x == 15:
        print('Se rompio la ejecucion del bucle cuando x valia ', x)
        break

    print(x)
