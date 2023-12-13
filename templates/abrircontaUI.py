import streamlit as st
from views import View

class AbrirContaUI:
  def main():
    st.header("Abrir Conta no Sistema")
    AbrirContaUI.inserir()
  
  def inserir():
    nome = st.text_input("Informe o nome")
    email = st.text_input("Informe o e-mail")
    fone = st.text_input("Informe o fone")
    senha = st.text_input("Informe a senha")
    if st.button("Cadastrar"):
      if nome == "admin":
        st.error("Nome não pode ser admin")
      else:
        View.cliente_inserir(nome, email, fone, senha)
        st.success("Conta criada com sucesso")