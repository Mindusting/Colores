###########
# COLORES #
###########

colores = []

# Color default
colores.append("\033[39;49m") #(0) default

# Colores normales
colores.append("\033[30m") #(1)  negro
colores.append("\033[31m") #(2)  rojo
colores.append("\033[32m") #(3)  verde
colores.append("\033[33m") #(4)  amarillo
colores.append("\033[34m") #(5)  azul
colores.append("\033[35m") #(6)  morado
colores.append("\033[36m") #(7)  cian
colores.append("\033[37m") #(8)  blanco

# Colores claros
colores.append("\033[90m") #(9)  negro claro
colores.append("\033[91m") #(10) rojo claro
colores.append("\033[92m") #(11) verde claro
colores.append("\033[93m") #(12) amarillo claro
colores.append("\033[94m") #(13) azul claro
colores.append("\033[95m") #(14) morado claro
colores.append("\033[96m") #(15) cian claro
colores.append("\033[97m") #(16) blanco claro

colores = tuple(colores)
