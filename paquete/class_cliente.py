
class Cliente():

    def __init__ (self,nombre,apellido,correo, edad, tarjeta):
       
        self.__nombre=nombre
        self.__apellido=apellido
        self.__correo=correo
        self.__edad=edad
        self.__tarjeta=tarjeta


    def __str__(self):
        return print("Datos del cliente: \n Nombre: " + self.__nombre + " \n Apellido: " + self.__apellido + "\n E-mail: " + self.__correo + "\n Edad: " + self.__edad)
    
    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido 

    def get_correo(self):
        return self.__correo

    def get_edad(self):
        return str(self.__edad)

    def set_nombre(self, nuevo_nombre):
        self.__nombre=nuevo_nombre
        print("El nombre se ha cambiado correctamente")

    def set_apellido(self, nuevo_apellido):
        self.__apellido=nuevo_apellido
        print("el apellido se ha cambiado correctamente")

    def set_correo(self, nuevo_correo):
        self.__correo=nuevo_correo
        print("lel e-mail se ha cambiado correctamente")

    def get_tarjeta(self):
        return str(self.__tarjeta)

    def set_tarjeta(self, nueva_tarjeta):
        self.__tarjeta=nueva_tarjeta
        print("la tarjeta de credito se ha cambiado correctamente")


    def set_edad(self, nueva_edad):
        self.__edad=nueva_edad
        print("la edad se ha cambiado correctamente")


    def agregar_carrito(self, item, cantidad):
        self.item=item
        self.cantidad=cantidad
        print(f"usted agrego {cantidad} unidades de {item} a su carrito de compras")


    def pagar(self):
        print(f"usted ha efectuado el pago con la tarjeta XX-XXXX-{self.__tarjeta[-4:]}")



