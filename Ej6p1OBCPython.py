class Vehiculo:
    def __init__(self, Color, Ruedas, Puertas):
        self.Color = Color
        self.Ruedas = Ruedas
        self.Puertas = Puertas
    
class Coche(Vehiculo):
    def __init__(self, Color, Ruedas, Puertas, Velocidad, Cilindrada):
        self.Color = Color
        self.Ruedas = Ruedas
        self.Puertas = Puertas
        self.Velocidad = Velocidad
        self.Cilindrada = Cilindrada
    def __str__(self):
        return "coche de color {}, que alcanza los {} kmph, con {} ruedas, {} puertas y {} cc de cilindrada".format(self.Color, self.Velocidad, self.Ruedas, self.Puertas, self.Cilindrada)

coche1 = Coche('Blanco', 4, 5, 160, 200)
coche2 = Coche('negro', 4, 5, 180, 250)
print(coche1)
print(coche2)
