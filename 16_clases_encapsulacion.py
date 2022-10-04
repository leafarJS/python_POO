# encapsulación 
class Cliente:
  def __init__(self):
    self.__codigo = 54321
    
    
  def __cuenta(self):
    print('N° de cuenta ahorro')  
    
  
  def getcodigo(self):
    return self.__codigo  
    
    
persona = Cliente()
#objeto._nombreClase__nombreAtributo
print(persona._Cliente__codigo)
print(persona._Cliente__cuenta())
print(persona.getcodigo())