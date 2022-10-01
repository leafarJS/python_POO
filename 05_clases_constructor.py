#metodo constructor
class Persona:
  pass
  #constructor 
  def __init__(self, nombre, year, edad, pais):
    self.nombre = nombre
    self.year = year
    self.edad = edad
    self.pais = pais
  
  def descripcion(self):
    return '{} tiene {} años, estamos en el año {} y vive en el pais {}'.format(self.nombre, self.edad, self.year, self.pais)
  
  def comentarios(self, msg):
    return '{} dice: {}'.format(self.nombre, msg) 
    

doctor = Persona("jorge", 2022, 45, "Bolivia")
print(doctor.nombre)
print(doctor.descripcion())   
print(doctor.comentarios("Solo se que nada se")) 

#modificar un atributo 
class Email:
  pass
  def __init__(self):
    self.enviado = False
  
  def enviar_email(self):
    self.enviado = True  
    
    
my_email = Email()
print(my_email.enviado)
my_email.enviar_email()
print(my_email.enviado)