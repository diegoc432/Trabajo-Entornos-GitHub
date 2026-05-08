# --- Módulo de Lógica de Tareas ---

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Salir")

def añadir_tarea(lista):
    nueva_tarea = input("Escribe la descripción de la tarea: ")
    lista.append(nueva_tarea)
    print("¡Tarea añadida!")

def ver_tareas(lista):
    if not lista:
        print("La lista está vacía.")
    else:
        for i, tarea in enumerate(lista):
            print(f"{i+1}. {tarea}")

# Esta parte es para probar que funciona
if __name__ == "__main__":
    mis_tareas = []
    print("Iniciando el sistema de gestión...")
