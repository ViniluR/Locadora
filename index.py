from templates.entrarUI import EntrarUI
from templates.editarperfilUI import EditarPerfilUI
from templates.abrircontaUI import AbrirContaUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterveiculoUI import ManterVeiculoUI
from templates.manterlocacaoUI import ManterLocacaoUI
from templates.reajustarUI import ReajustarUI
from templates.confirmarUI import ConfirmarUI
from templates.disponiveisUI import DisponiveisUI
from templates.solicitarUI import SolicitarUI
from templates.minhaslocacoesUI import MinhasLocacoesUI
from views import View

import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login": EntrarUI.main()
    if op == "Abrir Conta": AbrirContaUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Cliente", "Manter Veículo", "Manter Locação", "Reajustar", "Confirmar", "Editar Perfil"])
    if op == "Editar Perfil": EditarPerfilUI.main()
    if op == "Manter Cliente": ManterClienteUI.main()
    if op == "Manter Veículo": ManterVeiculoUI.main()
    if op == "Manter Locação": ManterLocacaoUI.main()
    if op == "Reajustar": ReajustarUI.main()
    if op == "Confirmar": ConfirmarUI.main()


  def menu_cliente():
    op = st.sidebar.selectbox("Menu", ["Ver veículos disponíveis", "Solicitar locação", "Suas locações", "Editar perfil"])
    if op == "Editar perfil": EditarPerfilUI.main()
    if op == "Ver veículos disponíveis": DisponiveisUI.main()
    if op == "Solicitar locação": SolicitarUI.main()
    if op == "Suas locações": MinhasLocacoesUI.main()

  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["cliente_id"]
      del st.session_state["cliente_nome"]
      st.rerun()

  def sidebar():
    if "cliente_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
      if st.session_state["cliente_nome"] == "admin": IndexUI.menu_admin()
      else: IndexUI.menu_cliente()
      IndexUI.btn_logout()  

  def main():
    View.cliente_admin()
    IndexUI.sidebar()

IndexUI.main()