

SubProceso  Fotografias()
	total <- 0
	Escribir "Bienvenido Al Sistem De Fotografia"
	Escribir "Ingrese La Cantidad de Fotografias"
	Leer Cantidad_Fotos
	Escribir "Tipo De Fotografia: a)Blanco Y Negro b)Color"
	Leer Tipo_Fotografia
	Tipo_Fotografia <- Mayusculas(Tipo_Fotografia)
	
	Escribir "Tamaño de las fotografías: 1.-4 x 6   2.-6x8  3.-8x10  4.-10x12"
	Leer  Tamano_Foto
	
	si Tipo_Fotografia == "A" Entonces
		Segun Tamano_Foto Hacer
			1:
				total <- (1.5 * Cantidad_Fotos)
			2:
				total <- (3.0 * Cantidad_Fotos)
			3:
				total <- (5.5 * Cantidad_Fotos)
			4:	
				total <- (10.0 * Cantidad_Fotos)
			De Otro Modo:
				Escribir "Opcion Seleccionada No Disponible"
		FinSegun
	 
	si Tipo_Fotografia == "B" Entonces
		Segun Tamano_Foto Hacer
			1:
				total <- (5.5 * Cantidad_Fotos)
			2:
				total <- (12.0 * Cantidad_Fotos)
			3:
				total <- (15.0 * Cantidad_Fotos)
			4:	
				total <- (18.5 * Cantidad_Fotos)
			De Otro Modo:
				Escribir "Opcion Seleccionada No Disponible"
		FinSegun
	SiNo
		Escribir "Opcion Seleccionada No Disponible"
	FinSi
	FinSi
	
	Escribir "¿El Servicio Será Impreso o por correo electrónico? [I / C]?:"
	leer servicio
	servicio <- Mayusculas(servicio)
	
	si servicio == "I" Entonces
		total <- total + (total * 0.15)
		Escribir  "TOTAL a pagar: $ " , total , "pesos"
		
		si servicio == "C" Entonces
			Repetir
				Escribir  "Favor De Indicar El Correo De Envio"
				Leer  correo
				Escribir "La Direccion De Correo A La Que Se enviara es:",correo
				Escribir  "TOTAL a pagar: $ " , total , "pesos"
			Hasta Que Verdadero
		SiNo
			Escribir "DIRECCION DE CORREO NO VALIDA"
		FinSi
		
	FinSi
	
FinSubProceso

SubProceso Calificaciones ( Estudiantes )
	calificacion = 0
	
	Calificaciones7 <- 0
	Calificaciones8 <- 0
	Calificaciones9 <- 0
	Calificaciones10 <- 0
	
	estudiantes_aprobados = 0
    estudiantes_reprobados = 0
	
	A = ""
    R = ""
	
	Para i <- 0 Hasta Estudiantes-1 Con Paso 1 Hacer
		Escribir  "Ingrese la Calificacion N°" , i + 1
		Leer calificacion
			
		si calificacion >= 7 Entonces
			estudiantes_aprobados <- estudiantes_aprobados + 1
			Segun calificacion Hacer
				7:
					Calificaciones7 <- Calificaciones7 + 1
				8:
					Calificaciones8 <- Calificaciones8 + 1
				9:
					Calificaciones9 <- Calificaciones9 + 1
				10:	
					Calificaciones10 <- Calificaciones10 + 1
			FinSegun
		SiNo
			estudiantes_reprobados <- estudiantes_reprobados + 1
		FinSi
	FinPara
	
	Escribir "Estudiantes con calificacion de 7: " , Calificaciones7
	Escribir "Estudiantes con calificacion de 8: " , Calificaciones8
	Escribir "Estudiantes con calificacion de 9: " , Calificaciones9
	Escribir "Estudiantes con calificacion de 10: " , Calificaciones10
	
	Escribir "Estudiantes aprobados: " ,estudiantes_aprobados
	Escribir "Estudiantes reprobados: " ,estudiantes_reprobados
	
	
	Escribir "¿Desea Graficar Los Resultados S/N?:"
	Leer  graficar
	graficar <- Mayusculas(graficar)
	
	si graficar == "S" Entonces
		Para i <- 0  Hasta estudiantes_aprobados Con Paso 1 Hacer
			A <- A + "**"
		FinPara
		Para i <- 0  Hasta estudiantes_reprobados Con Paso 1 Hacer
			R <- R + "**"
		FinPara
		
		Escribir "--------GRÁFICA--------"
		Escribir "A ", A
		Escribir "R ", R
	SiNo
		Escribir "Saliendo..."
	FinSi
	
FinSubProceso

Proceso Principal
	
	
	Repetir
		Escribir "Bienvenido Al menu"
		Escribir "1. Fotografías 2.Calificaciones 3. Salir"
		Leer  opcion 
		
		si opcion == 1 Entonces
			Fotografias()
		FinSi	
		si opcion == 2 Entonces
			Escribir "BIENVENIDO AL SISTEMA DE CALIFICACIONES"
			Escribir "Cantidad de estudiantes del grupo: "
			Leer  Estudiantes
			Calificaciones(Estudiantes)
		SiNo
			Escribir "Saliendo.."
		FinSi
			
		
	Hasta Que opcion <>1 y opcion <>2
FinProceso
