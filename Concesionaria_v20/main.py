from ventas import *
from listas import *
from autos import *


mis_ventas = Ventas()

def Compra():
    
    mas_clientes = "si"

    print ()
    print ("===================================================")
    print ("Bienvenido al Sistema de Concesionaria Automatizado")
    print ("===================================================")
    print ()

    while mas_clientes == "si":    
        print()
        mis_ventas.datosCliente()
        mis_ventas.marcas()
        mis_ventas.puerta()
        mis_ventas.colores()         
        mis_ventas.calcularPrecio()
        ventas.append({'Nombre':mis_ventas.Nombre, 'Apellido':mis_ventas.Apellido, 'Marca':mis_ventas.Marca, 'Puertas':mis_ventas.Puertas, 'Color':mis_ventas.Color, 'precioMarcas':mis_ventas.precio_marca, 'precioPuertas':mis_ventas.precio_puertas, 'precioColor':mis_ventas.precio_color, 'Total':mis_ventas.total})
        mas_clientes = input ("Hay mas clientes?: ").lower()
        
    if mas_clientes == "no":
        mis_ventas.descuento()
        mis_ventas.Imprimir()

comprar = Compra()

comprar