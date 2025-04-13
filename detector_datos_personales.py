import re

# Bienvenida inicial
print(" <---BIENVENIDO A DATA-SCANNER--->")
print(" <----------------------------------->\n")

# Menu principal que se repite mientras el programa este activo
def menu():
    print("Puedes escanear.....\n")
    print("1. Correos")
    print("2. Fechas")
    print("3. Teléfonos")
    print("4. Contraseñas")
    print("5. Cedulas")
    print("<------------->")
    print("6. Salir\n")
    
# Función para detectar correos electrónicos en un texto
def detectar_correos(texto):
    patron = r"[\w\.-]+@[\w\.-]+\.\w{2,}"
    correos = re.findall(patron, texto)
    
    if correos:
        print("Correos encontrados.")
        for correo in correos:
           print(f"- {correo}")
    else:
        return "Correos no encontrados.\n"

#Texto que contiene un correo
texto1 = "Hola, mi correo es Juan23@gmail.com"


# Función para detectar fechas en formato dd/mm/aaaa
def detectar_fecha(texto):
    patron = r"(?:0[1-9]|1[0-9]|2[0-9]|3[0-1])/(?:0[1-9]|1[0-2])/\d{4}"
    fechas = re.findall(patron, texto)
    
    if fechas:
        print("Fechas encontradas.")
        for fecha in fechas:
            print(f"- {fecha}")
    else:
        return "No se encontraron fechas.\n"

texto2 = "Nací el 04/12/1990."


# Función para detectar teléfonos dominicanos válidos
def detectar_telefonos(texto):
    patron = r"(?:809|829|849)-\d{3}-\d{4}"
    telefonos = re.findall(patron, texto)
    
    if telefonos:
        print("Teléfonos encontrados.")
        for telefono in telefonos:
            print(f"- {telefono}")
    else:
        return "No se encontraron teléfonos.\n"
        
texto3 = "Mi número es 829-555-9999."


# Función para detectar contraseñas seguras dentro de un texto
def detectar_contraseña(contraseña):
    patron = r"(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&])(?=.*\d)[a-zA-Z!@#$%^&\d]{8,}"
    contraseñas = re.findall(patron, contraseña)
    
    if contraseñas:
        print("Contraseñas encontradas.\n")
        for i in contraseñas:
            print(f"- {i}")
    else:
        return "No se encontraron contraseñas"
        
texto4 = "Uso Luis@2025 para registrarme."


# Función para detectar cédulas dominicanas en formato 000-0000000-0
def detectar_cedula(texto):
    patron = r"\d{3}-\d{7}-\d{1}"
    cedulas = re.findall(patron, texto)
    
    if cedulas:
        print("Cedulas encontradas.")
        for cedula in cedulas:
            print(f"- {cedula}")
    else:
        return "No se encontraron cedulas.\n"
        
texto5 = "Mi cédula es 001-1234567-2"


# Bucle principal del programa (ejecuta el menú hasta que el usuario salga)
while True:
        menu()
        opcion = int(input("Introduzca un numero de opción:\n"))
        
        # Ejecuta la opción seleccionada
        if opcion == 1:
            detectar_correos(texto1)
        elif opcion == 2:
            detectar_fecha(texto2)
        elif opcion == 3:
            detectar_telefonos(texto3)
        elif opcion == 4:
            detectar_contraseña(texto4)
        elif opcion == 5:
            detectar_cedula(texto5)
        elif opcion == 6:
            print("Gracias por usar ---DATA SCANNER---\n")
            break
        else:
            print("Opción no valida. Intente de nuevo.")
        



    
    