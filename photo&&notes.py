############################################################################################################################
#PROGRAMA DE FOTOGRAFIAS
import re
def Fotografias():
    total = 0

    print("\n######################################\n#Bienvenido Al Sistema De Fotografias#\n######################################\n")
           
    Cantidad_Fotos = int(input("\nIngrese La Cantidad De Fotografias\n"))

    Tipo_Fotografia = input("\nTipo de fotografía: a)Blanco y negro  b)Color\n")
    Tipo_Fotografia = Tipo_Fotografia.upper()

    Tamaño_Foto = int(input("\nTamaño de las fotografías: 1.-4 x 6   2.-6x8  3.-8x10  4.-10x12\n"))

    #EVALUAMOS SI EL TIPO DE LA FOTOGRAFIA ES A BLANCO Y NEGRO
    if Tipo_Fotografia == "A":
        
        #EVALUAMOS EL TAMAÑO DE LA FOTOGRAFIA SI SELECCIONA UNA OPCION NO DISPONIBLE MOSTRARA UN MENSAJE AL USUARIO
        if Tamaño_Foto == 1: 
            total = (1.5 * Cantidad_Fotos)
             
        elif Tamaño_Foto == 2:
            total = (3.0 * Cantidad_Fotos)
             
        elif Tamaño_Foto == 3:
            total = (5.5 * Cantidad_Fotos)
             
        elif Tamaño_Foto == 4:    
            total = (10.0 * Cantidad_Fotos)
            
        else:
            print("Opcion Seleccionada No Disponible")

    #EVALUAMOS SI EL TIPO DE LA FOTOGRAFIA ES A COLOR
    elif Tipo_Fotografia == "B":

        #EVALUAMOS EL TAMAÑO DE LA FOTOGRAFIA SI SELECCIONA UNA OPCION NO DISPONIBLE MOSTRARA UN MENSAJE AL USUARIO
        if Tamaño_Foto == 1: 
            total = (5.5 * Cantidad_Fotos)
             
        elif Tamaño_Foto == 2:
            total = (12.0 * Cantidad_Fotos)
            
        elif Tamaño_Foto == 3:
            total = (15.0 * Cantidad_Fotos)
             
        elif Tamaño_Foto == 4:    
            total = (18.5 * Cantidad_Fotos)
            
        else:
            print("Opcion Seleccionada No Disponible")

    #SI NO ES NI A BLANCO Y NEGRO NI A COLOR MOSTRARA MENSAJE DE OPCION NO DISPONIBLE
    else:
        print("Opcion Seleccionada No Disponible")        

    servicio = input("\n¿El Servicio Será Impreso o por correo electrónico? [I / C]?:\n")
    servicio = servicio.upper()


    if servicio == "I":
        total = total + (total * 0.15)
        print(f"TOTAL a pagar: $ {total} pesos\n")               
    elif servicio == "C":
        
        #EVALUAMOS MEDIANTE EXPRESIONES REGULARES HACIENDO USO DE LA LIBRERIA "re" si la estructura corresponde a la de un correo electronico si no muestra un mensaje de correo no valido y solicita de nuevo el correo
        while True:
            print("\nFavor de indicar el correo de envío:\n") 
            correo = input()
            if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
                print(f"\nLa Direccion De Correo A La Que Se enviara es: {correo}")
                print(f"\nTOTAL a pagar: $ {total} pesos\n")
            else:
                print ("*** DIRECCIóN DE CORREO NO VÁLIDA ***")
            if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):break 
#######################################################################################################################################
#PROGRAMA DE CALIFICACIONES
def Calificaciones(estudiantes):

    #VARIABLE PARA GUARDAR LAS CALIFICACIONES DE LOS ALUMNOS
    calificacion = 0

    #VARIABLES DE ACUMULACION PARA GUARDAR LA CANTIDAD DE ALUMNOS CON ESTA CALIFICACION
    calificaciones7 = 0
    calificaciones8 = 0
    calificaciones9 = 0
    calificaciones10 = 0

    #VARIABLES DE ACUMULACION PARA LOS ALUMNOS QUE APROBARON Y LOS QUE NO
    estudiantes_aprobados = 0
    estudiantes_reprobados = 0

    #VARIABLES PARA GRAFICAR SI EL USUARIO SELECCIONA LA OPCION 
    A = ""
    R = ""
           

#MEDIANTE ESTE CICLO FOR LLENAMOS EL ARREGLO CON LAS CALIFICACIONES DE LOS ALUMNOS Y ACUMULAMOS LOS ESTUDIANTES APROBADOS Y REPROBADOS
    for i in range(estudiantes):
        calificacion = int(input(f"\nIngrese la Calificacion N° {i + 1}\n"  )) 
        if calificacion >= 7:
            estudiantes_aprobados = estudiantes_aprobados + 1
            if calificacion == 7:
                calificaciones7 = calificaciones7 + 1
            if calificacion == 8:
                calificaciones8 = calificaciones8 + 1
            if calificacion == 9:
                calificaciones9 = calificaciones9 + 1        
            if calificacion == 10:
                calificaciones10 = calificaciones10 + 1        
        else:
            estudiantes_reprobados = estudiantes_reprobados + 1

    print(f"\nEstudiantes con una calificación de 7: {calificaciones7}")
    print(f"Estudiantes con una calificación de 8: {calificaciones8}")
    print(f"Estudiantes con una calificación de 9: {calificaciones9}")
    print(f"Estudiantes con una calificación de 10: {calificaciones10}")

    print(f"\nEstudiantes Que Reprobaron: {estudiantes_reprobados}\nEstudiantes Que Aprobaron: {estudiantes_aprobados}")
    
    graficar = input("\n¿Desea Graficar Los Resultados S/N?:\n")
    graficar = graficar.upper()

    if graficar == "S":
        for i in range (estudiantes_aprobados):
            A = A + "**"
        
        for i in range (estudiantes_reprobados):
            R = R + "**"

        print(f"\n--------GRÁFICA---------\nA {A}\nR {R}\n")
        import matplotlib.pyplot as plt
        import numpy as np

        #HACEMOS USO DE NUMPY MEDIANTE INTERFAZ GRAFICA SE MUESTRA UN GRAFICO CON LOS ALUMNOS QUE SACARON CALIFICACION DE 7,8,9  Y 10
        #ARREGLO con las calificaciones como string
        calificacionestxt = ['Calificacion 7', 'Calificacion 8', 'Calificacion 9', 'Calificacion 10']
        #ARREGLO con la calificacion como entero
        calificacionesval = [calificaciones7 , calificaciones8 , calificaciones9 , calificaciones10 ]

        fig, ax = plt.subplots()
        #Colocamos una etiqueta en el eje Y
        ax.set_ylabel('CANTIDAD DE PERSONAS')
        #Colocamos una etiqueta en el eje X
        ax.set_title('Promedio De Calificaciones APROBATORIAS')
        #Creamos la grafica de barras utilizando 'calificaciones' como eje X y 'CANTIDAD DE PERSONAS CALIFICACIONES' como eje y.
        plt.bar(calificacionestxt, calificacionesval)
       
        #mostramos la grafica con el metodo show()
        gr = plt.show()
        return gr
    else:
        print("Saliendo...\n")                    
##############################################################################################################################
#PROGRAMA PRINCIPAL
#CREAMOS UN CICLO PARA SALIR HASTA QUE EL USUARIO SELECCIONE LA OPCION 3 O UNA OPCION DIFERENTE A LA 1 Y 2
while True:
    print("********************************\n*****  Bienvenido Al Menu  *****\n********************************\n1. Fotografías 2.Calificaciones 3. Salir")
    opcion = int(input("Seleccione Una Opcion\n"))
    
    #HACEMOS EL LLAMADO A LA FUNCION DE FOTOGRAFIAS Y EJECUTA SU PROCESO
    if opcion == 1:
        Fotografias()
    #HACEMOS EL LLAMADO A LA FUNCION DE CALIFICACIONES Y EJECUTA SU PROCESO ESTA FUNCION RECIBE PARAMETROS Y RETORNA UNA VARIABLE DEPENDIENDO DE LA SELECCION DEL USUARIO
    elif opcion == 2:
        print("\n#########################################\n#Bienvenido Al Sistema De Calificaciones#\n#########################################\n")
        
        estudiantes = int(input("Cantidad de estudiantes en el grupo:\n"))
        Calificaciones(estudiantes)
    #SI EL USUARIO SELECCIONA LA OPCION 3 O INGRESA UNA OPCION DIFERENTE A 1 O 2 EL PROGRAMA MOSTRARA UN MENSAJE DE SALIENDO Y FINALIZARA  
    else:
        print("Saliendo...")
        break        