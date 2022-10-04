#Poliformismo por función
class Tomate:
  def tipo(self):
    print('fruta vegetal')
  
  
  def color(self):
    print('rojo')
    
class Manzana:
  def tipo(self):
    print('fruta')
  
  
  def color(self):
    print('verde')
    
    
def my_function(obj):
  obj.tipo()
  obj.color()
  

new_object = Tomate()
result = my_function(new_object)  
print(result)

new_object1 = Manzana()
result2 = my_function(new_object1)
print(result2)
