import streamlit as st
import pandas as pd
from views import View

class ConfirmarUI:
    def main():
        st.header("Confirmar locação")
        ConfirmarUI.confirmar()
    def confirmar():
        locacoes = View.locacao_naoconfirmados()
        if len(locacoes) == 0:
          st.write("Nenhuma locação solicitada")
        else:
          st.write("Locações solicitadas")
          dic = []
          for obj in locacoes: dic.append(obj.to_json())
          df = pd.DataFrame(dic)
          st.dataframe(df)
          loc = st.selectbox("Locações solicitadas", locacoes)
          if st.button("Confirmar"):
              View.locacao_atualizar(loc.get_id(), loc.get_idCliente(), loc.get_idVeiculo(), loc.get_retirada(), loc.get_devolucao(), True)
              st.success("Horário confirmado")