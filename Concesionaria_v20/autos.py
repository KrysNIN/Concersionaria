from listas import *
from clientes import *

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