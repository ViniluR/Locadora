import streamlit as st
from views import View

class EditarPerfilUI:
    def main():
        st.header("Atualizar perfil")
        EditarPerfilUI.atualizar()

    def atualizar():
        st.write("Código a programar")