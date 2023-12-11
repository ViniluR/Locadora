import streamlit as st
import pandas as pd
from views import View

class ManterClienteUI:
    def main():
        st.header("Manter Cliente")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
    def listar():
        st.write("Código a programar")
    def inserir():
        st.write("Código a programar")
    def atualizar():
        st.write("Código a programar")
    def excluir():
        st.write("Código a programar")