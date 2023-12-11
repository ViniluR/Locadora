import streamlit as st
import pandas as pd
from views import View

class SolicitarUI:
    def main():
        st.header("Solicitar locação")
        SolicitarUI.solicitar()
    def solicitar():
        st.write("Código a programar")