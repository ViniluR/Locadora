from models.cliente import Cliente, NCliente
from models.veiculo import Veiculo, NVeiculo
from models.locacao import Locacao, NLocacao
import datetime

class View:
  def cliente_listar():
    return NCliente.listar()
  
  def cliente_listar_id(id):
    return NCliente.listar_id(id)

  def cliente_inserir(nome, email, fone, senha):
    cliente = Cliente(0, nome, email, fone, senha)
    NCliente.inserir(cliente)

  def cliente_atualizar(id, nome, email, fone, senha):
    cliente = Cliente(id, nome, email, fone, senha)
    NCliente.atualizar(cliente)
    
  def cliente_excluir(id):
    cliente = Cliente(id, "", "", "", "")
    NCliente.excluir(cliente)    

  def cliente_admin():
    for cliente in View.cliente_listar():
      if cliente.get_nome() == "admin": return
    View.cliente_inserir("admin", "admin", "0000", "admin")  

  def cliente_login(email, senha):
    for cliente in View.cliente_listar():
      if cliente.get_email() == email and cliente.get_senha() == senha:
        return cliente
    return None
  
  def veiculo_listar():
    return NVeiculo.listar()
  
  def veiculo_listar_id(id):
    return NVeiculo.listar_id(id)
  
  def veiculo_inserir(marca, modelo, ano, valor):
    NVeiculo.inserir(Veiculo(0, marca, modelo, ano, float(valor)))

  def veiculo_atualizar(id, marca, modelo, ano, valor):
    NVeiculo.atualizar(Veiculo(id, marca, modelo, ano, float(valor)))
  
  def veiculo_excluir(id):
    NVeiculo.excluir(Veiculo(id, "", "", "", 1))

  def veiculo_reajustar(id, per):
    obj = NVeiculo.listar_id(id)
    NVeiculo.atualizar(Veiculo(id, obj.get_marca(), obj.get_modelo(), obj.get_ano(), obj.get_valor() + obj.get_valor() * (per/100)))
  
  def locacao_listar():
    return NLocacao.listar()
  
  def locacao_inserir(idcliente, idveiculo, retirada, devolucao):
    NLocacao.inserir(Locacao(0, idcliente, idveiculo, retirada, devolucao, False))

  def locacao_atualizar(id, idcliente, idveiculo, retirada, devolucao, confirmado):
    NLocacao.atualizar(Locacao(id, idcliente, idveiculo, retirada, devolucao, confirmado))

  def locacao_excluir(id):
    NLocacao.excluir(Locacao(id, 0, 0, "", "", ""))

  def locacao_naoconfirmados():
    return NLocacao.listar_nao_confirmados()

  def locacao_listarcliente(cliente):
    r = []
    for obj in NLocacao.listar():
      if obj.get_idCliente() == cliente.get_id():
        r.append(obj)
    return r
  
  def locacao_periodo(obj, inicio, final):
    data_inicio = datetime.datetime.strptime(f"{inicio} 00:00", "%d/%m/%Y %H:%M")
    data_fim = datetime.datetime.strptime(f"{final} 23:59", "%d/%m/%Y %H:%M")
    if obj.get_retirada() > data_fim or obj.get_devolucao() < data_inicio: 
      return False
    else: return True

  def locacao_conta(obj, id):
    veiculo = NVeiculo.listar_id(id)
    valor = veiculo.get_valor()
    return valor * int((obj.get_devolucao() - obj.get_retirada()).days)
