Proceso promedio
	Definir numero_uno, numero_dos, numero_tres, suma_total Como entero;//definimos nuestra variable, en este caso como n�meros enteros
	definir promedio_resultado Como Real;//definimos la variable de promedio como real por si da un n�mero decimal
	escribir "escriba primera nota";//en esta linea pedimos ingresar el primer d�gito para ser almacenado y despu�s sea sumado al segundo n�mero y luego sumado al tercer n�mero
	leer numero_uno;//en esta linea decimos el programa que lea el primer d�gito
	escribir "escriba segunda nota";//en esta linea pedimos ingresar el segundo d�gito
	leer numero_dos;//en esta linea decimos al programa que lea el segundo d�gito
	escribir "escriba tercera nota";//en esta linea pedimos ingresar el tercer n�mero deseado
	leer numero_tres;//en esta linea decimos al programa que lea el tercer d�gito que ingresamos"
	suma_total=numero_uno+numero_dos+numero_tres;//en esta linea declaramos que suma es el resultado de sumar los 3 d�gitos ingresados
	promedio_resultado=suma_total/3;// en esta linea definimos que el promedio es el resultado de la suma dividido en el total de n�meros ingresados, en este caso en concreto es 3
	escribir "su promedio es:", promedio_resultado; //en esta linea le decimos al programa que entrege el resultado de toda la operaci�n con la variable "escribir" para hacer enteder el resultado que arroje es el promedio

	si promedio_resultado >=4 entonces//aqu� dejamos definido que si el n�mero es mayor a 4 cumple cierta condici�n
		escribir "usted est� aprobado";//si la condici�n anterior se cumple como un numero mayor a 4 estar� aprobado
	sino//si no cumple lo anteriormente mencionado
		escribir "usted est� reprobado";//estar� reprobado si el n�mero resultante es menor a 4
		
		
	FinSi//finaliza el condicionante
	
FinProceso
