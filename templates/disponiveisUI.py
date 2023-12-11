import streamlit as st
import pandas as pd
from views import View

class DisponiveisUI:
    def main():
        st.header("Veja os veículos disponíveis para você")
        DisponiveisUI.listar()
    def listar():
        st.write("Código a programar")