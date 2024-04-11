Proceso promedio
	Definir numero_uno, numero_dos, numero_tres, suma_total Como entero;//definimos nuestra variable, en este caso como números enteros
	definir promedio_resultado Como Real;//definimos la variable de promedio como real por si da un número decimal
	escribir "escriba primera nota";//en esta linea pedimos ingresar el primer dígito para ser almacenado y después sea sumado al segundo número y luego sumado al tercer número
	leer numero_uno;//en esta linea decimos el programa que lea el primer dígito
	escribir "escriba segunda nota";//en esta linea pedimos ingresar el segundo dígito
	leer numero_dos;//en esta linea decimos al programa que lea el segundo dígito
	escribir "escriba tercera nota";//en esta linea pedimos ingresar el tercer número deseado
	leer numero_tres;//en esta linea decimos al programa que lea el tercer dígito que ingresamos"
	suma_total=numero_uno+numero_dos+numero_tres;//en esta linea declaramos que suma es el resultado de sumar los 3 dígitos ingresados
	promedio_resultado=suma_total/3;// en esta linea definimos que el promedio es el resultado de la suma dividido en el total de números ingresados, en este caso en concreto es 3
	escribir "su promedio es:", promedio_resultado; //en esta linea le decimos al programa que entrege el resultado de toda la operación con la variable "escribir" para hacer enteder el resultado que arroje es el promedio

	si promedio_resultado >=4 entonces//aquí dejamos definido que si el número es mayor a 4 cumple cierta condición
		escribir "usted está aprobado";//si la condición anterior se cumple como un numero mayor a 4 estará aprobado
	sino//si no cumple lo anteriormente mencionado
		escribir "usted está reprobado";//estará reprobado si el número resultante es menor a 4
		
		
	FinSi//finaliza el condicionante
	
FinProceso
