#Polimorfismo con herencia
class Aves:
  def volar(self):
    print('Las aves son de tipo aereas')


class Aguila(Aves):
  def volar(self):
    print('Las aguilas puden volar a 300k/h')
    

class Gallina(Aves):
  def volar(self):
    print('Las gallinas son aves que no pueden volar')


new_object = Aves()
new_aguila = Aguila()
new_gallina = Gallina()

print(new_object.volar())
print(new_aguila.volar())
print(new_gallina.volar())
