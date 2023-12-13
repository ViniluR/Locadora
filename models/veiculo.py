import json

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



class NVeiculo:
  __veiculos = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__veiculos:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__veiculos.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__veiculos

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__veiculos:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_marca(obj.get_marca())
      aux.set_modelo(obj.get_modelo())
      aux.set_ano(obj.get_ano())
      aux.set_valor(obj.get_valor())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__veiculos.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__veiculos = []
    try:
      with open("veiculos.json", mode="r") as arquivo:
        veiculos_json = json.load(arquivo)
        for obj in veiculos_json:
          aux = Veiculo(obj["_Veiculo__id"], obj["_Veiculo__marca"], obj["_Veiculo__modelo"], obj["_Veiculo__ano"], obj["_Veiculo__valor"])
          cls.__veiculos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("veiculos.json", mode="w") as arquivo:
      json.dump(cls.__veiculos, arquivo, default=vars)