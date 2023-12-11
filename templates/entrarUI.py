import streamlit as st
from views import View
import time

class EntrarUI:
  def main():
    st.header("Entrar no Sistema")
    EntrarUI.entrar()
  def entrar():
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    if st.button("Login"):
      cliente = View.cliente_login(email, senha) 
      if cliente is not None:
        st.success("Login realizado com sucesso")
        st.success("Bem-vindo(a), " + cliente.get_nome())
        st.session_state["cliente_id"] = cliente.get_id()
        st.session_state["cliente_nome"] = cliente.get_nome()
        time.sleep(1)
        st.rerun()
      else:
        st.error("Usuário ou senha inválido(s)")