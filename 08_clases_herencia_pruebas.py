#herencia ejemplo practico
class Calculadora:
  pass
  def __init__(self, num):
    self.num = num
    self.datos = [0 for i in range(num)]
  
  def ingresar_datos(self):
    self.datos = [int(input('Ingresar números '+str(i+ 1) + ' = ')) for i in range(self.num)]
    

class Operaciones_Basicas (Calculadora):
  def __init__(self):
    Calculadora.__init__(self, 2)

  
  def suma(self):
    a,b, = self.datos
    sum = a + b
    print(f'El resultado de la suma es : {sum}')
  
  def resta(self):
    a,b, = self.datos
    rest = a + b
    print(f'El resultado de la resta es: {rest}')
  
  
class Raiz (Calculadora):
  def __init__(self):
    Calculadora.__init__(self,1)
    
  def raiz_cuadrada(self):
    import math
    a, = self.datos
    print(f"El resultado de la raiz cuadrada es {math.sqrt(a)}")
    
resultado = Operaciones_Basicas()
print(isinstance(resultado, Operaciones_Basicas)) # el objeto trabaja con la función
print(isinstance(resultado, Raiz)) # el objeto no esta trabajando con esta función

print(issubclass(Calculadora, Raiz)) # falso
print(issubclass(Raiz, Calculadora)) # true
print(issubclass(Exponente, Calculadora)) # Error
