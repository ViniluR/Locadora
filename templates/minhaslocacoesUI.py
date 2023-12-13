import streamlit as st
import pandas as pd
from views import View

class MinhasLocacoesUI:
    def main():
        st.header("Suas locações")
        MinhasLocacoesUI.listar()
    def listar():
        cliente = View.cliente_listar_id(st.session_state["cliente_id"])
        locacoes = View.locacao_listarcliente(cliente)
        if len(locacoes) == 0:
          st.write("Você não possui nenhuma locação")
        else:
          dic = []
          for obj in locacoes: dic.append({"Veículo" : f'{View.veiculo_listar_id(obj.get_idVeiculo()).get_marca()} - {View.veiculo_listar_id(obj.get_idVeiculo()).get_modelo()}', "Retirada" : obj.get_retirada().date(), "Devolução" : obj.get_devolucao().date(), "Valor a pagar" : View.locacao_conta(obj, obj.get_idVeiculo())})
          df = pd.DataFrame(dic)
          st.dataframe(df)