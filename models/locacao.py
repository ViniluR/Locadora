import json
import datetime
from models.modelo import Modelo

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
    return f"{self.__id} - {self.__idCliente} - {self.__idVeiculo} - {self.__retirada.strftime('%d/%m/%Y')} - {self.__devolucao.strftime('%d/%m/%Y')} - {self.__confirmado}"

  def to_json(self):
    return {
      'ID': self.__id,
      'Cliente': self.__idCliente,
      'Veiculo': self.__idVeiculo,
      'Retirada': self.__retirada.strftime('%d/%m/%Y'),
      'Devolucao': self.__devolucao.strftime('%d/%m/%Y'),
      'Confirmado': self.__confirmado}


class NLocacao(Modelo):

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("locacoes.json", mode="r") as arquivo:
        locacoes_json = json.load(arquivo)
        for obj in locacoes_json:
          aux = Locacao(
            obj["ID"], obj["Cliente"], obj["Veiculo"],
            datetime.datetime.strptime(obj["Retirada"], "%d/%m/%Y"),
            datetime.datetime.strptime(obj["Devolucao"], "%d/%m/%Y"),
            obj["Confirmado"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("locacoes.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=Locacao.to_json)