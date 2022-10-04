# Introducción al Poliformismo
""" 
te valor sobre carga de metodos, eso quiere decir que la clase definida tiene comportamientos diferentes
pylo  = muchas 
morfismo = formas
Polimorfismo en python es la capacidad que tienen los objetos en diferentes clases para usar un comportamiento o atributo del mismo nombre pero con diferen """


#pueden ser iguales en sus atributos pero diferentes en sus acciones y funciones y a eso se llama polymorfismo

class Automovil:
  rueda = 4
  def desplazamiento(self):
    print('El auto se desplaza sobre 4 ruedas')
    
    
class Motocicleta:
  rueda = 2
  def desplazamiento(self):
    print('La moto se desplaza sobre 2 ruedas')
    

class Animales:
  def __init__(self, nombre):
    self.nombre = nombre
    
  def especie_animal(self):
    pass
  
 
class Leon(Animales):
  def especie_animal(self):
    print(f"Felino, altamente peligroso, nombre: {self.nombre}") 
    

class Perro(Animales):
  def especie_animal(self):
    print(f"Canino, animal domesticado por el hombre, nombre: {self.nombre}")
  

new_object = Leon("Simba")
print(new_object.especie_animal())

new_object2 = Perro("Lisa")
print(new_object2.especie_animal())














    
