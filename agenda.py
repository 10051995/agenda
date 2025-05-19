 
import os

users = []

def load_users():
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r", encoding="utf-8") as file:
            for line in file:
                users.append(line.strip())

def save_users():
    with open("usuarios.txt", "w", encoding="utf-8") as file:
        for user in users:
            file.write(user + "\n")

def show_menu():
    print("\n--- Menú ---")
    print("1. Registrar nuevo usuario")
    print("2. Ver todos los usuarios")
    print("3. Salir")

def register_user():
    name = input("Ingresa el nombre del nuevo usuario: ")
    if name:
        users.append(name)
        save_users()
        print(f"Usuario '{name}' registrado con éxito.")
    else:
        print("Nombre no válido. Intenta de nuevo.")

def show_users():
    if users:
        print("\nUsuarios registrados:")
        for index, name in enumerate(users, start=1):
            print(f"{index}. {name}")
    else:
        print("No hay usuarios registrados.")

# Cargar usuarios al iniciar
load_users()

while True:
    show_menu()
    option = input("Selecciona una opción: ")
    if option == "1":
        register_user()
    elif option == "2":
        show_users()
    elif option == "3":
        print("Saliendo del programa. ¡Adiós!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
