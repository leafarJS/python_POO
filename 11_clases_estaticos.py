import math 

#clases y estaticos
#CLASE: es como una plantilla o un molde para crear diferentes objetos.
#INSTANCIA DE CLASE
#OBJETO: se crea usando el constructor de una clase. una vez que el objeto es creado se le conoce como una instancia de la clase.


# En python existen 3 tipos de métodos: estaticos, clases e instancias

#metodo de clase @classmethod, este metodo puede ser llamado sin crear una instancia de la clase
class Pastel:
  #constructor y sus atributos 
  def __init__(self, ingredientes):
    self.ingredientes = ingredientes

  def __repr__(self):
    return f'pastel({self.ingredientes !r})'
  
  @classmethod
  def Pastel_chocolate(cls):
    return cls(['harina', 'leche', 'chocolate', 'vainilla', 'azucar', 'sal'])
  
  @classmethod
  def Pastel_durazno(cls):
    return cls(['harina', 'leche', 'durazno', 'vainilla', 'azucar', 'sal'])
  

print(Pastel.Pastel_chocolate())
print(Pastel.Pastel_durazno())


#método estatico: pueden ser llamados sin tener una instancia de clase, ademas este tipo métodos no tienen acceso al exterior. por lo que no pueden acceder a ningun otro atributo o llamar a ninguna otra función dentro la clase. 

class Pastel_1:
  def __init__(self, ingredientes, medida):
    self.ingredientes = ingredientes
    self.medida = medida
    
  def __repr__(self):
    return (f"Pastel_1({self.ingredientes}, 'f'{self.medida})")
  
  def area_pastel(self):
    return self.medida_area(self.medida)
  
  @staticmethod
  def medida_area(ar):
    return ar ** 2 * math.pi
    

new_pastel = Pastel_1(['harina', 'azucar' 'crema', 'leche'], 4)
print(new_pastel.ingredientes)
print(new_pastel.area_pastel)
print(new_pastel.medida_area(12))
