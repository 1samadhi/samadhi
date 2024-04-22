print("ingrese la fecha actual en formato yyyy/mm/dd")
anhoActual = int(input("ingrese el año actual: "))
mesActual = int(input("ingrese el mes actual: "))
diaActual = int(input("ingrese el día actual: "))

print("ingrese su fecha de nacimiento en el siguiente formato: yyyy/mm/dd")
anhoDeNacimiento = int(input("ingrese su año de nacimiento: "))
mesDeNacimiento = int(input("ingrese su mes de nacimiento: " ))
diaDeNacimiento = int(input("ingrese su día de nacimiento: " ))

if (mesDeNacimiento>=mesActual):
    if (diaDeNacimiento>diaActual):
     edad = anhoActual-anhoDeNacimiento-1
    else:
     edad = anhoActual - anhoDeNacimiento

else:
 edad = anhoActual - anhoDeNacimiento

print("su edad es:", edad)