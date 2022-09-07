class Clientes ():
    
    def __init__ (self):
        self.Nombre = ""
        self.Apellido = ""        

    def datosCliente (self):
        self.Nombre = input ("Ingrese su Nombre: ")
        print()
        self.Apellido = input ("Ingrese su Apellido : ")
        print()