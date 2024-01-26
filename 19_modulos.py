import sys
print(sys.path) #muestra la carpeta en done estoy

import re
test="mi numero de telefono es  1441 445 444, el codigo de pais es +51 , tengo 20 años"
result=re.findall("[0-9]+",test) #busca coincidencia segun lo que se indique
print(result) 

import time
timestamp=time.time()
local=time.localtime()
result=time.asctime()
print(timestamp)
print(result)

