import re

texto = 'Buenas tardes a todas y todos!'

patron = 'B.*t.*a'
patron2 = 'd[aeo]{1,2}s'

#coincidencia = re.match(patron, texto)

coincidencia2 = re.search(patron2, texto)

encontrar = re.findall(patron2, texto)



pass