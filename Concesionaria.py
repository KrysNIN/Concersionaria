Marcas =  ['ford', 'chevrolet', 'fiat']
Puertas = [2, 4, 5]
Colores = ['blanco', 'azul', 'negro']
ventas = []

class Clientes ():
    
    def __init__ (self):
        self.Nombre = ""
        self.Apellido = ""        

    def datosCliente (self):
        self.Nombre = input ("Ingrese su Nombre: ")
        print()
        self.Apellido = input ("Ingrese su Apellido : ")
        print()

class Autos (Clientes):

    def __init__ (self):
        self.Marca = ""
        self.Color = ""
        self.Puertas = ""
        self.precio_marca = ""
        self.precio_puertas = ""
        self.precio_color = ""
        self.total = ""

    def marcas (self):
        self.Marca = ""
        while self.Marca not in Marcas:
            self.Marca = input('Por favor, elija una marca entre Ford, Chevrolet y Fiat: ')
            self.Marca = self.Marca.lower()
            print()
            if self.Marca == 'ford':
                self.precio_marca = 100000
            elif self.Marca == 'Chevrolet':
                self.precio_marca = 120000
            elif self.Marca == 'fiat':
                self.precio_marca = 80000
    
    def puerta (self):
        self.Puertas = ""
        while self.Puertas not in Puertas:
            self.Puertas = int(input ('Por favor, elija una cantidad de puertas entre 2, 4 y 5: '))
            print()
            if self.Puertas == 2:
                self.precio_puertas = 50000
            elif self.Puertas == 4:
                self.precio_puertas = 65000
            elif self.Puertas == 5:
                self.precio_puertas = 78000
        
    def colores (self):
        self.Color = ""
        while self.Color not in Colores:
            self.Color = input ('Elija un color valido entre Blanco, Azul o Negro: ')
            self.Color = self.Color.lower()
            print()
            if self.Color == 'blanco':
                self.precio_color = 10000
            elif self.Color == 'azul':
                self.precio_color = 20000
            elif self.Color == 'negro':
                self.precio_color = 30000
    
    def calcularPrecio (self):
        self.total = self.precio_marca+self.precio_puertas+self.precio_color
        return self.total

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