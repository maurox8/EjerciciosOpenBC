class Vehiculo:
    Color = None
    Ruedas = None
    Puertas = None

class Coche(Vehiculo):
    Velocidad = None
    Cilindrada = None

v = Vehiculo()
c = Coche()

c.Color= 'Blanco'
c.Velocidad = 180

print('El coche es de color', c.Color, 'y alcanza los', c.Velocidad, 'kmph')
