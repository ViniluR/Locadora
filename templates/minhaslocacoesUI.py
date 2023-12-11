import streamlit as st
import pandas as pd
from views import View

class MinhasLocacoesUI:
    def main():
        st.header("Suas locações")
        MinhasLocacoesUI.listar()
    def listar():
        st.write("Código a programar")