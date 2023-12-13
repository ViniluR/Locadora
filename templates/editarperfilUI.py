import streamlit as st
from views import View

class EditarPerfilUI:
    def main():
        st.header("Editar perfil")
        EditarPerfilUI.atualizar()

    def atualizar():
        op = View.cliente_listar_id(st.session_state["cliente_id"])
        nome = "admin"
        nomee = ""
        if op.get_nome() != "admin":
            nome = st.text_input("Informe o novo nome")
            nomee = nome
        email = st.text_input("Informe o novo e-mail")
        fone = st.text_input("Informe o novo fone")
        senha = st.text_input("Informe a nova senha")
        if st.button("Atualizar"):
            id = op.get_id()
            if nomee == "admin":
                st.error("Nome não pode ser admin")
            else:
                View.cliente_atualizar(id, nome, email, fone, senha)
                st.success("Perfil atualizado com sucesso")