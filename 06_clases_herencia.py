#Herencia
class Pokemon:
  pass
  def __init__(self, name, type):
    self.name = name
    self.type = type
  
  def descripcion(self):
    return 'El pokemon {} es de tipo {} '.format(self.name, self.type)

#clase hijo de la clase Pokemon
class Pikachu (Pokemon):
      def attak(self, tipo_attak):
        return '{} tipo de ataque: {}'.format(self.name, tipo_attak)
      
class Charmander (Pokemon):
      def attak(self, tipo_attak):
        return '{} tipo de ataque: {}'.format(self.name, tipo_attak)
      
nuevo_Pokemon = Pikachu("Pika Pika", "Electrico")
print(nuevo_Pokemon.descripcion())

otro_pokemon = Charmander("Saidok", "Agua")
print(otro_pokemon.attak("Bomba de agua"))