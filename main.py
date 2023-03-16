from paquete.class_cliente import *
from paquete.login import *

#uso de fx de la primer entrega

registrar_usuario()
registrar_usuario()
registrar_usuario()
mostrar_usuario()
login_usuario()
guardar_registro()

#uso de clases (segunda entrega)


cliente1=Cliente("Carlos", "Perez", "dsdasdasd@gmail.com", "23", "32143423443424")
cliente2=Cliente("Jose", "Gomez", "11111111@gmail.com", "28", "32342444679532")


cliente1.set_apellido("Gimenez")

cliente1.agregar_carrito("Computadora", 1)
cliente1.agregar_carrito("Mouse", 7)

cliente2.pagar()

print(cliente1)