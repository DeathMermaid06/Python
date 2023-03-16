
registro={}

def registrar_usuario():
  usuario=input("Ingrese el usuario: ")
  while usuario in registro.keys():
    print("El usuario ya existe, elija otro nombre")
    break
  else:
    contrasena=input("Ingrese la contraseña: ")
    registro[usuario]=contrasena
    return (print("El usuario se ha registrado correctamente"))

def mostrar_usuario():
  print("Los usuarios registrados hasta el momento son: ")
  for r in registro: 
    print(f"Usuario:{r} Contraseña:{registro[r]}")

def login_usuario():
  usuario = input("Ingrese el usuario: ")
  if usuario in registro.keys():
    password = input("Ingrese la contraseña: ")
    if usuario in registro:
      if password==(registro[usuario]):
        print("Ha ingresado correctamente")
      else:
        print("El password es incorrecto")
  else:
    print("El usuario no existe")

def guardar_registro():
  o_usuarios =open("usuarios_last.txt", "a")
  for r in registro:
    o_usuarios.write(f"Usuario:{r} Contraseña:{registro[r]}")
  print("se han guardado los usuarios en el sistema")
  o_usuarios.close()
