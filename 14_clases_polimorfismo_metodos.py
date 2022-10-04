#Polimorfismo con metodos
class Colombia:
  def capital(self):
    print('La capital de Colombia es Bogota')
    
  def idioma(self):
    print('Idioma oficial: Español')
    

class Francia:
  def capital(self):
    print('La capital de Colombia es Paris')
    
  def idioma(self):
    print('Idioma oficial: Frances')
    
    
colombiano = Colombia()
frances = Francia()

for pais in (colombiano, frances):
  print(pais.capital())
  print(pais.idioma())






