def calcular_precio (Marca, Puertas, Color, ventas):

    marcas =  {'ford': 100000, 'chevrolet': 120000, 'fiat': 80000}
    colores = {'blanco': 10000, 'azul': 20000, 'negro': 30000}
    puertas = {2: 50000, 4: 65000, 5: 78000}
    precio = marcas[Marca]+colores[Color]+puertas[Puertas]
    
    if len(ventas) > 3 and len(ventas) < 6:
        precio = precio*0.9
    elif len(ventas) > 6 and len(ventas) < 10:
        precio = precio*0.85
    elif len(ventas) > 10:
        precio = precio*0.82
        
    return precio

ventas = []
mas_clientes = "si"
puertas = [2, 4, 5]
colores = ['blanco', 'azul', 'negro']
marcas = ['ford', 'chevrolet', 'fiat']

print ()
print ("===================================================")
print ("Bienvenido al Sistema de Consecionaria Automatizado")
print ("===================================================")

while mas_clientes == "si":

    print ()
    Nombre = input ('Ingrese su Nombre: ')
    Apellido = input ('Ingrese su Apellido: ')
    Marca = ""
    Puertas = 0
    Color = ""

    while Marca not in marcas:
        Marca = input ('Por favor, elija una marca entre Ford, Chevrolet y Fiat: ')
        Marca = Marca.lower()
    if Marca == "ford":
        precio_marca = 100000
    elif Marca == "chevrolet":
        precio_marca = 120000
    elif Marca == "fiat":
        precio_marca = 80000

    while Puertas not in puertas:
        Puertas = int(input ('Por favor, elija una cantidad de puertas entre 2, 4 y 5: '))
    if Puertas == 2:
        precio_puertas = 50000
    elif Puertas == 4:
        precio_puertas = 65000
    elif Puertas == 5:
        precio_puertas = 78000

    while Color not in colores:
        Color = input ('Elija un color valido entre Blanco, Azul o Negro: ')
        Color = Color.lower()
    if Color == "blanco":
        precio_color = 10000
    elif Color == "azul":
        precio_color = 20000
    elif Color == "negro":
        precio_color = 30000
  
    precio = calcular_precio (Marca, Puertas, Color, ventas)

    ventas.append({'Nombre':Nombre, 'Apellido':Apellido, 'Marca':Marca, 'Puertas':Puertas, 'Color':Color, 'Total':precio, 'PrecioMarca':precio_marca, 'PrecioPuertas':precio_puertas, 'PrecioColor':precio_color})

    print ()
        
    mas_clientes = input('Hay mas clientes?: ')
    mas_clientes = mas_clientes.lower()
    
    if mas_clientes == "no":
        
        print()
        for i in ventas:
            print()        
            print("La persona: " + i['Nombre']+" "+i['Apellido']+", compro un Auto marca "+i['Marca']+", de " +str(i['Puertas'])+" puertas, color " +i['Color']+", por un precio Total de: $ " +str(i['Total']))
            print()
            print("Los precios por separado son: ")
            print("==============================")
            print()
            print("Precio del Auto Base: $ " + str(i['PrecioMarca']))
            print("Precio de las Puertas: $ " + str(i['PrecioPuertas']))
            print("Precio del Color: $ " + str(i['PrecioColor']))
            print()
            print("==============================")
            print()
        
        if len(ventas) > 3 and len(ventas) < 6:
            print("Estas ventas tienen un descuento del 10%...!")
            print()
            print("============================================")
        elif len(ventas) > 6 and len(ventas) < 9:
            print("Estas ventas tienen un descuento del 15%...!")
            print()
            print("============================================")
        elif len(ventas) > 9:
            print("Estas ventas tienen un descuento del 18%...!")
            print()
            print("============================================")

        print()
        print("Cantidad de Ventas Totales: "+str(len(ventas)))                                         
        print()
        print("==============================")
        print()
        print('Muchas gracias por utilizar este sistema!, que tenga un excelente dia. :)')
        print()