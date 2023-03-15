class Cliente:
    def __init__ (self,nombre,apellido,edad,correo,contrasena):
        self.nombre=nombre
        self.apellido=apellido
        self.__edad=edad
        self.__correo=correo
        self.__contrasena=contrasena

    def __str__(self):
        return "Nombre" + self.nombre + "Apellido" + self.apellido

