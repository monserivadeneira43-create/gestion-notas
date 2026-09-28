# Programa de Gestión de Notas de Estudiantes
# Colección utilizada: Diccionario { Nombre: Nota }

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE NOTAS ---")
    print("1. Agregar estudiante y nota")
    print("2. Mostrar todos los estudiantes")
    print("3. Buscar nota de un estudiante")
    print("4. Eliminar un estudiante")
    print("5. Salir")

def agregar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ").strip().capitalize()
    if nombre in estudiantes:
        print(f"El estudiante '{nombre}' ya está registrado con la nota: {estudiantes[nombre]}")
    else:
        try:
            nota = float(input(f"Ingrese la nota de {nombre} (0 a 10): "))
            if 0 <= nota <= 10:
                estudiantes[nombre] = nota
                print(f"¡Estudiante '{nombre}' agregado exitosamente!")
            else:
                print("Error: La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido.")

def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("\n--- LISTA DE ESTUDIANTES Y NOTAS ---")
        for nombre, nota in estudiantes.items():
            print(f"• {nombre}: {nota}")

def buscar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante a buscar: ").strip().capitalize()
    if nombre in estudiantes:
        print(f"La nota de '{nombre}' es: {estudiantes[nombre]}")
    else:
        print(f"El estudiante '{nombre}' no se encuentra en el registro.")

def eliminar_estudiante(estudiantes):
    nombre = input("Ingrese el nombre del estudiante a eliminar: ").strip().capitalize()
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante '{nombre}' eliminado correctamente.")
    else:
        print(f"El estudiante '{nombre}' no existe en el registro.")

def main():
    # Inicialización del diccionario
    estudiantes = {}
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            agregar_estudiante(estudiantes)
        elif opcion == "2":
            mostrar_estudiantes(estudiantes)
        elif opcion == "3":
            buscar_estudiante(estudiantes)
        elif opcion == "4":
            eliminar_estudiante(estudiantes)
        elif opcion == "5":
            print("¡Gracias por utilizar el programa! Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
    