import streamlit as st
import pandas as pd
from views import View

class ManterVeiculoUI:
    def main():
        st.header("Manter Veículo")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterVeiculoUI.listar()
        with tab2: ManterVeiculoUI.inserir()
        with tab3: ManterVeiculoUI.atualizar()
        with tab4: ManterVeiculoUI.excluir()
    def listar():
        st.write("Código a programar")
    def inserir():
        st.write("Código a programar")
    def atualizar():
        st.write("Código a programar")
    def excluir():
        st.write("Código a programar")