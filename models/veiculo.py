import json
from models.modelo import Modelo

class Veiculo:
  def __init__(self, id, marca, modelo, ano, valor):
    self.__id = id
    self.__marca = marca
    self.__modelo = modelo
    self.__ano = ano
    self.__valor = valor

  def get_id(self): return self.__id
  def get_marca(self): return self.__marca
  def get_modelo(self): return self.__modelo
  def get_ano(self): return self.__ano
  def get_valor(self): return self.__valor

  def set_id(self, id): self.__id = id
  def set_marca(self, marca): self.__marca = marca
  def set_modelo(self, modelo): self.__modelo = modelo
  def set_ano(self, ano): self.__ano = ano
  def set_valor(self, valor): self.__valor = valor

  def __eq__(self, x):
    if self.__id == x.__id and self.__marca == x.__marca and self.__modelo == x.__modelo and self.__ano == x.__ano and self.__valor == x.__valor:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__marca} - {self.__modelo} - {self.__ano} - {self.__valor:.2f}"
  
  def to_json(self):
    return {
      'ID': self.__id,
      'Marca': self.__marca,
      'Modelo': self.__modelo,
      'Ano': self.__ano,
      'Valor p/dia': self.__valor}



class NVeiculo(Modelo):

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("veiculos.json", mode="r") as arquivo:
        veiculos_json = json.load(arquivo)
        for obj in veiculos_json:
          aux = Veiculo(obj["_Veiculo__id"], obj["_Veiculo__marca"], obj["_Veiculo__modelo"], obj["_Veiculo__ano"], obj["_Veiculo__valor"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("veiculos.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)