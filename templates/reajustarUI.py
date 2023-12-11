import streamlit as st
import pandas as pd
from views import View

class ReajustarUI:
    def main():
        st.header("Reajustar valor de um veículo")
        ReajustarUI.reajustar()
    def reajustar():
        st.write("Código a programar")