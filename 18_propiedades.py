#propiedades 
class Empleado:
  def __init__(self, nombre, salario):
    #valores encapsulados
    self.__nombre = nombre
    self.__salario = salario
  
  # llamar a los valores
  def __getnombre(self): #doble barra baja al inicio para encapsular
    return self.__nombre
  
  
  def __getsalario(self):
    return self.__salario
  
  #cambiar los valores
  def __setnombre(self, nombre):
    self.__nombre = nombre
    
  
  def __setsalario(self, salario):
    self.__salario = salario
    
  # eliminar los valores
  def __delnombre(self):
    del self.__nombre
    
  
  def __delsalario(self):
    del self.__salario


  nombre = property(fget = __getnombre,
                    fset = __setnombre,
                    fdel = __delnombre,
                    doc = "soy la propiedad del 'nombre' " ) 
  
  salario = property(fget = __getsalario,
                    fset = __setsalario,
                    fdel = __delsalario,
                    doc = "soy la propiedad del 'salario' " )  


""" new_object = Empleado('Jorge', 16000)
print(new_object.getnombre(), ',' ,new_object.getsalario())

new_object.setnombre('Rafael')
new_object.setsalario(20000)

print(new_object.getnombre(), ',' ,new_object.getsalario())

new_object.delsalario()

print(new_object.getnombre()) """

new_object1 = Empleado('Rafael', 25000)
new_object1.nombre = 'Jorge'
print(new_object1.nombre, new_object1.salario)
help(new_object1)