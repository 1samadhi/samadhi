Proceso TablaDelDiez//nombre el algoritmo
	definir numero_uno, resultado, i Como Real;//definimos nuestras variables que usaremos al futuro: "numero_uno" para el número que ingresará el usuario, "resultado" para definir numero_uno*i e "i" que será el numero en bucle del 1 al 10
	escribir "ingrese su número para ver la tabla de multiplicar";//le pedimos al usuario que ingrese un número para mostrarle su tabla de multiplicar"
	leer numero_uno;//la máquina lee el digito ingresado por el ususario
	para i<-1 hasta 10 con paso 1 Hacer//indicamos que "i" caiga en un bucle donde irá del 1 hasta el 10 donde le adicionaremos el número que ingresó el usuario
		resultado<-numero_uno * i;//le damos significado a la variable "resultado" donde indicamos que significa el número ingresado por el usuario multiplicado por "i" que estaba en bucle del 1 al 10
			escribir numero_uno, " x ", i, " = ", resultado;//aquí simplemente le indicamos al ordenador que nos diga que el numero ingresado por el usuario "x" para hacer visible la multiplicación por la variable "i" (bucle) sea igual"=" a "resultado" definido anteriormente
		FinPara//finalizamos el bucle
FinProceso//término del algoritmo
