import streamlit as st
import pandas as pd
from views import View
import datetime

class SolicitarUI:
    def main():
        st.header("Solicitar locação")
        SolicitarUI.solicitar()
    def solicitar():
        st.write('Favor checar os veículos disponíveis ("Ver veículos disponíveis") no período desejado antes de solicitar')
        if len(View.veiculo_listar()) > 0:
            veiculo = st.selectbox("Veiculo desejado", View.veiculo_listar())
            retirada = st.text_input("Data de retirada em formato DD/MM/AAAA")
            devolucao = st.text_input("Data de devolução em formato DD/MM/AAAA")
            if st.button("Solicitar"):
              pode = True
              for loc in View.locacao_listar():
                if loc.get_idVeiculo() == veiculo.get_id():
                    if View.locacao_periodo(loc, retirada, devolucao):
                       pode = False
              if pode:
                retirada = datetime.datetime.strptime(retirada, "%d/%m/%Y")
                devolucao = datetime.datetime.strptime(devolucao, "%d/%m/%Y")
                View.locacao_inserir(st.session_state("cliente_id"), veiculo.get_id(), retirada, devolucao)
                st.success("Locação solicitada com sucesso, aguarde confirmação")
              else:
                 st.error("Veículo indisponível para o intervalo de tempo selecionado")
        else:
            st.write("Nenhum veículo disponível para locação")