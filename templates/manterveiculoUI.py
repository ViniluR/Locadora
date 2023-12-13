import streamlit as st
import pandas as pd
from views import View

class ManterVeiculoUI:
    def main():
        st.header("Manter Veículos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterVeiculoUI.listar()
        with tab2: ManterVeiculoUI.inserir()
        with tab3: ManterVeiculoUI.atualizar()
        with tab4: ManterVeiculoUI.excluir()

    def listar():
        veiculos = View.veiculo_listar()
        if len(veiculos) == 0:
            st.write("Nenhum veículo cadastrado")
        else:
            dic = []
            for obj in veiculos: dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        marca = st.text_input("Insira a marca")
        modelo = st.text_input("Insira o modelo")
        ano = st.text_input("insira o ano")
        valor = st.text_input("Valor do carro p/dia (Ex: 499.90)")
        if st.button("Inserir"):
          View.veiculo_inserir(marca, modelo, ano, float(valor))
          st.success("Veículo inserido com sucesso")

    def atualizar():
        veiculos = View.veiculo_listar()
        if len(veiculos) == 0:
            st.write("Nenhum veículo no sistema")
        else:
            op = st.selectbox("Veículo a atualizar", veiculos)
            marca = st.text_input("Insira a nova marca")
            modelo = st.text_input("Insira o novo modelo")
            ano = st.text_input("insira o novo ano")
            valor = st.text_input("Novo valor do carro p/dia (Ex: 499.90)")
            if st.button("Atualizar"):
                View.veiculo_atualizar(op.get_id(), marca, modelo, ano, float(valor))
                st.success("Veículo atualizado com sucesso")

    def excluir():
        veiculos = View.veiculo_listar()
        if len(veiculos) == 0:
          st.write("Nenhum veículo no sistema")
        else:
          op = st.selectbox("Veículo a excluir", veiculos)
          if st.button("Excluir"):
            id = op.get_id()
            View.veiculo_excluir(id)
            st.success("Veículo excluído com sucesso")