import streamlit as st
import pandas as pd
from views import View
import datetime

class ManterLocacaoUI:
    def main():
        st.header("Manter Locações")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterLocacaoUI.listar()
        with tab2: ManterLocacaoUI.inserir()
        with tab3: ManterLocacaoUI.atualizar()
        with tab4: ManterLocacaoUI.excluir()

    def listar():
        locacoes = View.locacao_listar()
        if len(locacoes) == 0:
            st.write("Nenhuma locação cadastrada")
        else:
          dic = []
          for obj in locacoes: dic.append(obj.to_json())
          df = pd.DataFrame(dic)
          st.dataframe(df)

    def inserir():
        cliente = st.selectbox("Cliente", View.cliente_listar())
        veiculo = st.selectbox("Veiculo", View.veiculo_listar())
        retirada = st.text_input("Data de retirada (DD/MM/AAAA)")
        devolucao = st.text_input("Data de devolução (DD/MM/AAAA)")
        if st.button("Inserir"):
          pode = True
          for loc in View.locacao_listar():
            if loc.get_idVeiculo() == veiculo.get_id():
                if View.locacao_periodo(loc, retirada, devolucao):
                   pode = False
          if pode:
            retirada = datetime.datetime.strptime(retirada, "%d/%m/%Y")
            devolucao = datetime.datetime.strptime(devolucao, "%d/%m/%Y")
            View.locacao_inserir(cliente.get_id(), veiculo.get_id(), retirada, devolucao)
            st.success("Locação inserida com sucesso")
          else:
             st.error("Veículo não disponível para o intervalo de tempo selecionado")

    def atualizar():
        locacoes = View.locacao_listar()
        if len(locacoes) == 0:
            st.write("Nenhuma locação no sistema")
        else:
            op = st.selectbox("Locação a atualizar", locacoes)
            cliente = st.selectbox("Novo cliente", View.cliente_listar())
            veiculo = st.selectbox("Novo veículo", View.veiculo_listar())
            retirada = st.text_input("Nova data de retirada")
            devolucao = st.text_input("Nova data de devolucao")
            if st.button("Atualizar"):
                retirada = datetime.datetime.strptime(retirada, "%d/%m/%Y")
                devolucao = datetime.datetime.strptime(devolucao, "%d/%m/%Y")
                View.locacao_atualizar(op.get_id(), cliente.get_id(), veiculo.get_id(), retirada, devolucao, False)
                st.success("Locação atualizada com sucesso")

    def excluir():
        locacoes = View.locacao_listar()
        if len(locacoes) == 0:
          st.write("Nenhuma locação cadastrada")
        else:
          op = st.selectbox("Locação a excluir", locacoes)
          if st.button("Excluir"):
            id = op.get_id()
            View.locacao_excluir(id)
            st.success("Locação excluída com sucesso")