import streamlit as st
import pandas as pd
from views import View

class ReajustarUI:
    def main():
        st.header("Reajustar valor de um veículo")
        ReajustarUI.listar()
    def listar():
        veiculos = View.veiculo_listar()
        if len(veiculos) == 0:
          st.write("Nenhum veículo cadastrado")
        else:  
          dic = []
          for obj in veiculos: dic.append(obj.to_json())
          df = pd.DataFrame(dic)
          st.dataframe(df)
          percentual = st.text_input("Informe o percentual (%)")
          op = st.selectbox("Escolha o veículo", veiculos)
          if st.button("Reajustar"):
            View.veiculo_reajustar(op.get_id(), float(percentual))
            st.success("Reajuste realizado com sucesso")