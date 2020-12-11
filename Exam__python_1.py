#Importamos las herramientas del sistema
import os

'''definiciones de funciones'''

def cargar():
    lugar = 0 # variable que maneja la cantidad de lugares total (52 segun enunciado)
    recaudacion = 0
    condicion ='si'
    while condicion == 'si':
    
        if lugar == 52:
              
            print ("No hay lugar")
            condicion = "no"
        else:  
           patente = input('Ingrese patente del vehiculo:')
           modelo = input ('Ingrese modelo del vehiculo:')
           telefono= int (input('Ingrese nro de telefono del dueño:'))
           color = input ('Ingrese color del vehiculo:')
           cantidad_horas= int (input('Ingrese cantidad de horas de estadia del vehiculo:'))
           recaudacion += 600 * cantidad_horas
           condicion = input ('Desea Ingresar otro vehiculo s/n:')
           lugar = lugar +1
           auto=[patente,modelo,telefono,color,cantidad_horas]
           listado_autos.append(auto)
    return (recaudacion)
def mostrar(listado_autos):
        
        for indice in range(len(listado_autos)):
        #En cada vuelta, mostramos todos los datos de cada uno de los clientes
            print('----------')
            print(f'Patente: {listado_autos[indice][0]}')
            print(f'Modelo: {listado_autos[indice][1]}')
            print(f'Color: {listado_autos[indice][3]}')
            print(f'Teléfono: {listado_autos[indice][2]}')
            print('----------')

#Limpiamos la pantalla
os.system("cls")
'''bloque principal'''
listado_autos = []   # se crea lista que contendra los datos que ejecutara el programa
recaudacion_final = 0 

print('Software de Administracion de Vehiculos')

#Creamos una variable opcion que va a empezar valiendo 0
#De esta forma, forzamos el comienzo del while. 
opcion = 0

while opcion != 5:
    print('--------------------------------------')
    print('1.Carga de datos del auto')
    print('2.Mostrar una lista de los vehículos cargados')
    print('3.Dar de baja un vehículo de la base de datos')
    print('4.Informe del día')
    print('5.Salir')
    print('---------------------')
    opcion = int(input('Ingrese una opcion: '))
    while opcion < 1 or opcion > 5:
        print ("Se ingreso un valor incorrecto.")
        opcion = int(input("Ingrese una opcion:"))
        
    #Estructura condicional que se va a encargar de elegir el código a ejecutar de acuerdo al código que ingrese el usuario
    if opcion == 1:
        
      recaudacion_final += cargar()
    
    elif opcion == 2:
         mostrar(listado_autos)
    elif opcion == 3:
        indice_a_borrar = 0
        bandera = False
        print('Dar de baja un vehículo de la base de datos:')
        #ingreso de patente para buscar el vehiculo a ser removido
        patenteABuscar = input('Ingrese la patente del vehiculo a ser eliminado de la base de datos: ')
        for indice in range (len(listado_autos)):
            if listado_autos[indice][0] == patenteABuscar:
             #remuevo el elemento de la lista , pero antes debo guardar las horas que consumio estacionado
                bandera = True
                indice_a_borrar = indice
                print(bandera)
            else:
                bandera = False
                print(bandera)
        if bandera == True:
            listado_autos.remove(indice_a_borrar)
            
        else:
            print ("No se encontro la patente solicitada")   
            
    if opcion == 4:
        print ("La recaudacion final es:",recaudacion_final)
    if opcion == 5:
        print ("Programa finalizado")
        print ("")
        print("")
        import this
        print ("")                