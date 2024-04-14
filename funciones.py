from Conexion import cursor,BD

# Función para mostrar usuarios
def mostrarUsuarios():
    cursor.execute("select * FROM user")
    usuarios = cursor.fetchall()
    if usuarios:
        print("Listado de usuarios:")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Usuario: {usuario[2]}")
    else:
        print("No hay usuarios registrados.")

# Función para registrar usuarios
def crearUser(nombre, usuario):
    consulta = "insert into user (Nombre,Usuario) values (%s, %s)"
    valores = (nombre, usuario)
    cursor.execute(consulta,valores)
    BD.commit()
    print(f"Usuario {usuario} registrado con éxito.")

# Función para registrar usuarios
def ActualizarUser(id, nombre, usuario):
    consulta = "update user set Nombre = %s, Usuario = %s where id = %s"
    valores = (nombre, usuario, id)
    cursor.execute(consulta, valores)
    BD.commit()
    print(f"Usuario actualizado.")

# Función para registrar usuarios
def EliminarUser(user):
    consulta = "DELETE FROM user WHERE Usuario = %s"
    cursor.execute(consulta, (user,))
    BD.commit()
    print("Usuario eliminado con exito.")