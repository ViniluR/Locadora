import json
import datetime

class Locacao:
  def __init__(self, id, idCliente, idVeiculo, retirada, devolucao, confirmado):
    self.__id = id
    self.__idCliente = idCliente
    self.__idVeiculo = idVeiculo
    self.__retirada = retirada
    self.__devolucao = devolucao
    self.__confirmado = confirmado

  def get_id(self): return self.__id
  def get_idCliente(self): return self.__idCliente
  def get_idVeiculo(self): return self.__idVeiculo
  def get_retirada(self): return self.__retirada
  def get_devolucao(self): return self.__devolucao
  def get_confirmado(self): return self.__confirmado

  def set_id(self, id): self.__id = id
  def set_idCliente(self, idCliente): self.__idCliente = idCliente
  def set_idVeiculo(self, idVeiculo): self.__idVeiculo = idVeiculo
  def set_retirada(self, retirada): self.__retirada = retirada
  def set_devolucao(self, devolucao): self.__devolucao = devolucao
  def set_confirmado(self, confirmado): self.__confirmado = confirmado 

  def __eq__(self, x):
    if self.__id == x.__id and self.__idCliente == x.__idCliente and self.__idVeiculo == x.__idVeiculo and self.__retirada == x.__retirada and self.__devolucao == x.__devolucao and self.__confirmado == x.__confirmado:
        return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__idCliente} - {self.__idVeiculo} - {self.__retirada.strftime('%d/%m/%Y %H:%M')} - {self.__devolucao.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}"

  def to_json(self):
    return {
      'id': self.__id,
      'idCliente': self.__idCliente,
      'idVeiculo': self.__idVeiculo,
      'retirada': self.__retirada.strftime('%d/%m/%Y %H:%M'),
      'devolucao': self.__devolucao.strftime('%d/%m/%Y %H:%M'),
      'confirmado': self.__confirmado}


class NLocacao:
  __locacoes = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__locacoes:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__locacoes.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__locacoes

  @classmethod
  def listar_nao_confirmados(cls):
    cls.abrir()
    nao_confirmados = []
    for obj in cls.__locacoes:
      if not obj.get_confirmado():
        nao_confirmados.append(obj)
    return nao_confirmados

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_idCliente(obj.get_idCliente())
      aux.set_idVeiculo(obj.get_idVeiculo())
      aux.set_retirada(obj.get_retirada())
      aux.set_devolucao(obj.get_devolucao())
      aux.set_confirmado(obj.get_confirmado())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__locacoes.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__locacoes = []
    try:
      with open("locacoes.json", mode="r") as arquivo:
        locacoes_json = json.load(arquivo)
        for obj in locacoes_json:
          aux = Locacao(
            obj["id"], obj["idCliente"], obj["idVeiculo"],
            datetime.datetime.strptime(obj["retirada"], "%d/%m/%Y %H:%M"),
            datetime.datetime.strptime(obj["devolucao"], "%d/%m/%Y %H:%M"),
            obj["confirmado"])
          cls.__locacoes.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("locacoes.json", mode="w") as arquivo:
      json.dump(cls.__locacoes, arquivo, default=Locacao.to_json)