#las funciones dentro de las clases son metodos 
# los metodos describien una acción o comportamiento 

#SELF nos referimos al objeto , la otra función de SELF es para ejecutar la variable que puede ser un valor o un algoritmo.

#Metodos
class Matematicas:
  #creación de un método 
  def suma(self):
    self.x = 2
    self.y = 4

sum = Matematicas()
sum.suma()
print(sum.x + sum.y)

# metodo constructor
#__init__(self) es una función constructor que sirve para iniciar 

class Ropa:
  def __init__(self):
    self.marca = "Nike"
    self.talla = "M"
    self.color = "Anaranjado"
    

pantalon =  Ropa()

print(pantalon.marca)
print(pantalon.talla)


class Calculadora:
  def __init__(self, num1, num2):
    self.sumar = num1 + num2
    self.restar = num1 - num2 
    self.producto = num1 * num2
    self.dividir = num1 / num2 
    
operacion = Calculadora(10,100)
print(operacion.producto)
print(operacion.sumar)
print(operacion.dividir)
print(operacion.restar)