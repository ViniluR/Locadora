import streamlit as st
import pandas as pd
from views import View

class DisponiveisUI:
    def main():
        st.header("Veja os veículos disponíveis para você")
        DisponiveisUI.listar()
    def listar():
        veiculos = View.veiculo_listar()
        if veiculos == 0:
           st.write("Não há veículos a serem locados")
        else:
            inicio = st.text_input("Informe a data inicial no formato DD/MM/AAAA")
            final = st.text_input("Informe a data final no formato DD/MM/AAAA")
            if st.button("Ver disponíveis"):
              veiculos = View.veiculo_disponiveis(inicio, final)
              if len(veiculos) == 0:
                st.write("Nenhum veículo disponível")
              else:
                dic = []
                for obj in veiculos: dic.append(obj.to_json())
                df = pd.DataFrame(dic)
                st.dataframe(df)