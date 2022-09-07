from listas import *
from autos import *

class Ventas (Autos):

    def __init__(self):
        self.descuentos = ""

    def descuento (self):
        if len(ventas) > 3 and len(ventas) < 6:
            self.descuentos = self.total*0.9
           
    def Imprimir (self):
        for i in ventas:
            print()
            print("El cliente: "+i['Nombre']+" "+i['Apellido']+", compro un Auto Marca: "+i['Marca']+", la Cantidad de Puertas es de: "+str(i['Puertas'])+", y el color es: "+i['Color'])
            print()
            print()
            print("==================")
            print("Resumen de Compra:")
            print("==================")
            print("Auto Base ("+i['Marca']+"): $ "+str(i['precioMarcas']))
            print(str(i['Puertas'])+" Puertas: $ "+str(i['precioPuertas']))
            print("Color "+i['Color']+" $: "+str(i['precioColor']))
            print("===============================")
            print()
            print("===============================")
            print("El precio total es de: $ "+str(i['Total']))
            print("===============================")
            print()

        if len(ventas) > 3 and len(ventas) < 6:
            print("==============================================")
            print("Estas ventas tuvieron un 10% de descuento...!!")
            print("==============================================")
            print()
        print("=================")
        print("Ventas totales: "+str(len(ventas)))
        print("=================")
        print()
        print("===================================================================")
        print("Muchas gracias por utilizar este sistema!, que tenga un buen día :)")
        print("===================================================================")
        print()