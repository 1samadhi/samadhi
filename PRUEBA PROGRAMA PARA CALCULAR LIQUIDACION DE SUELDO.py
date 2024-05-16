import os
print("*******PROGRAMA PARA CALCULAR TU LIQUIDACIÓN DE SUELDO*******")

#Validar nombre
while True:
    try:
        nombreTrabajador = str(input("Por favor, ingrese su nombre: "))
    #Quitamos la posibilidad que este campo quede vacío
        if nombreTrabajador != "":
            letras = 0
            for nombre in nombreTrabajador:
                letras +=1
            if letras <= 30:
             break
            else:
             print("el nombre debe tener menos de 30 letras")
        else:
         print("Debe ingresar un nombre: ")
    except Exception:
        ("Debe utilizar solamente caracteres")
#Nos aseguramos que el sueldo base sea un número, no letras ni espacios vacíos
while True:
    try: 
        sueldoBase = int(input("Ingrese su sueldo base: "))
        if sueldoBase == "":
            print("Debe ingresar un valor numérico para el sueldo base.")
        else:
            sueldoBase = int(sueldoBase)
            if sueldoBase >= 0:
                break
            else: 
                print("El sueldo base debe ser un número positivo: ")
    except Exception:
        print("Debe utilizar solamente números")

#Nos aseguramos que las horas extras sean solo número, no letras ni espacios vacíos

while True:
    try:
        horasExtras = int(input("Ingrese sus horas extras:"))
        if horasExtras =="":
            print("Debe ingresar un valor numérico para las horas extras")
        else:
            horasExtras = int(horasExtras)
            if horasExtras >= 0:
                 break
            else: 
                print("Las horas extras debe ser un valor positivo")
    except Exception:
            print("Debe utilizar solamente números: ")

#Sueldo base
sueldoPorHora = sueldoBase / 180
sueldoPorHora = horasExtras * (sueldoPorHora * 1.5) 
print(f"el pago por horas extras es: {sueldoPorHora}")

#Total de ingresos
totalIngresos = sueldoBase + sueldoPorHora

print(f"El total de ingresos es: {totalIngresos}")

#Calcular el descuento por Fonasa
descuentoFonasa = totalIngresos * 0.07

print(f"El descuento por Fonasa es: {descuentoFonasa}")

#Calcular el descuento por AFP
descuentoAfp = totalIngresos * 0.10

print("El descuento por AFP es:", descuentoAfp)

#Calcular el total de descuentos por seguridad social
totalDescuentos = descuentoFonasa + descuentoAfp

#Calcular el sueldo neto a pagar
sueldoNeto = totalIngresos - totalDescuentos

print(f"El sueldo neto a pagar es: {sueldoNeto}")

#Imprimimos todos los datos

print("******* LIQUIDACIÓN ********")
print(f"Nombre del trabajador: {nombreTrabajador}")
print(f"Sueldo base: {sueldoBase:,.0f}")
print(f"Pago por horas extras: {sueldoPorHora:,.0f}")
print(f"Total de ingresos: {totalIngresos:,.0f}")
print(f"Descuento por Fonasa: {descuentoFonasa:,.0f}")
print(f"Descuento por AFP {descuentoAfp:,.0f}")
print(f"--------------------------------------")
print(f"Sueldo neto a pagar: {sueldoNeto:,.0f}")

#Generamos un archivo de texto.

with open("liquidacion.txt", "w") as archivo:
    archivo.write("******* LIQUIDACIÓN ********\n")
    archivo.write(f"Nombre del trabajador: {nombreTrabajador}\n")
    archivo.write(f"Sueldo base: {sueldoBase:,.0f}\n")
    archivo.write(f"Pago por horas extras: {int(horasExtras):,.0f}\n")
    archivo.write(f"Total de ingresos: {int(totalIngresos):,.0f}\n")
    archivo.write(f"Descuento por Fonasa: {int(descuentoFonasa):,.0f}\n")
    archivo.write(f"Descuento por AFP: {int(descuentoAfp):,.0f}\n")
    archivo.write("--------------------------------------\n")
    archivo.write(f"Sueldo neto a pagar: {int(sueldoNeto):,.0f}\n")

if input("Desea calcular otra liquidación) si/no: ") != 'si':
    print("******Ha finalizado el programa******")
         









    






  



                  