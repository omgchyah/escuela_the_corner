# Un diccionario para almacenar las credenciales de los usuarios
# La clave es el nombre de usuario y el valor es la contraseña.
credenciales = [
    {'usuario': 'usuario1', 'password': 'Mio1'},
    {'usuario': 'admin', 'password': '1234'}
]

# {
#     'usuario1': 'Mio1',
#     'admin': '1234'
# }

def login():
    """
    Función para simular el proceso de inicio de sesión.
    """
    print("👋 ¡Bienvenido al servicio de inicio de sesión!\n")
    
    # Solicitar al usuario que ingrese su nombre de usuario
    nombre_usuario = input("Por favor, ingresa tu nombre de usuario: ").strip()
    
    # Verificar si el nombre de usuario existe en el diccionario
    for credencial in credenciales:
        if credencial['usuario'] == nombre_usuario:
            # Si el usuario existe, verificar si la contraseña es correcta
            # Solicitar al usuario que ingrese su contraseña
            contrasena = input("Por favor, ingresa tu contraseña:✍🏻 ").strip()
            if credencial['password'] == contrasena:
                print(f"✅ ¡Inicio de sesión exitoso! Bienvenido, {nombre_usuario}.")
            else:
                print("❌ Contraseña incorrecta. Por favor, inténtalo de nuevo.")
                return

    print("❌ Nombre de usuario no encontrado. Por favor, revisa tus credenciales.")

# Llamar a la función para ejecutar el programa La línea if __name__ == "__main__":
# es una convención común en Python. Asegura que la función login() 
# se llame solo cuando el script se ejecuta directamente, no cuando se importa como un módulo en otro programa.
if __name__ == "__main__":
    login()