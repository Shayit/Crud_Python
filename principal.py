import funciones
import Clear

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar personas")
            print("2.- Registrar personas")
            print("3.- Actualizar personas")
            print("4.- Eliminar personas")
            print("5.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("Nos vemos pronto")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    
    if opcion == 1:
        Clear.clearConsole()
        try:            
            funciones.mostrarUsuarios()
        except:
            print("No se econtraron usuarios.")

    elif opcion == 2:
        Clear.clearConsole()
        name = str(input("Ingrese su nombre: "))
        userName = str(input("Ingrese el usuario: "))    
        try:
            funciones.crearUser(name,userName)
        except:
            print("Ocurrió un error")

    elif opcion == 3:
        Clear.clearConsole()
        id = int(input("Ingrese el ID: "))
        name = str(input("Ingrese su nombre: "))
        userName = str(input("Ingrese el usuario: "))    
        try:
            Clear.clearConsole()
            funciones.ActualizarUser(id,name,userName)
        except:
            print("Ocurrió un error")

    elif opcion == 4:
        Clear.clearConsole()
        userName = str(input("Ingrese el usuario: "))
        try:
            funciones.EliminarUser(userName)
        except:
            print("Ocurrió un error.")

sele = 0
menuPrincipal()
ejecutarOpcion(sele)