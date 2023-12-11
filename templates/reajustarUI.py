import streamlit as st
import pandas as pd
from views import View

class ReajustarUI:
    def main():
        st.header("Reajustar valor de um veículo")
        ReajustarUI.listar()
    def listar():
        st.write("Código a programar")