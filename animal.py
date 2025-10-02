class Animal:
  
  #método constructor
  def __init__(self, nombre, edad, raza, pelos, peso):
    self.nombre = nombre
    self.edad = edad
    self.raza = raza
    self.pelos = pelos
    self.peso = peso
    
  def ladrar(self):
    print(f"{self.nombre} dice Guau guau!")
  
  def cumplir_anyos(self):
    self.edad += 1
    # self.edad = self.edad + 1
    print(f"Felicidades {self.nombre}!!! Ahora tienes {self.edad} años!")

#############################################################
    
chucho = Animal("chucho", 4, "Perro", True, 14.5)

chucho.ladrar()
chucho.cumplir_anyos()
chucho.cumplir_anyos()
chucho.cumplir_anyos()
chucho.cumplir_anyos()
