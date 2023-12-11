import streamlit as st
import pandas as pd
from views import View

class ManterLocacaoUI:
    def main():
        st.header("Manter Locação")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterLocacaoUI.listar()
        with tab2: ManterLocacaoUI.inserir()
        with tab3: ManterLocacaoUI.atualizar()
        with tab4: ManterLocacaoUI.excluir()
    def listar():
        st.write("Código a programar")
    def inserir():
        st.write("Código a programar")
    def atualizar():
        st.write("Código a programar")
    def excluir():
        st.write("Código a programar")