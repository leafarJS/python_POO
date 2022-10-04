#Super
class Mamifero:
  def __init__(self, nombre):
    print(nombre, 'Los mamiferos son de sangre caliente')
    
  
class Leon(Mamifero):
  def __init__(self):
    print('Los leones viven en manada y son mamiferos')
    super().__init__('Sandocan')
    #Mamifero.__init__(self, 'simba')
    
new_object = Leon()
print(new_object)

