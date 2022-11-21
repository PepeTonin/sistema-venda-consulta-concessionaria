import streamlit as st
from menu import *


# cria alguns radio buttons para o usuário definir o que quer fazer no aplicativo
escolhaNav = st.sidebar.radio(
    'Menu', ('Cadastrar', 'Listar carros', 'Pesquisar', 'Vender'), index=0)


# se a opção 'cadastrar' for selecionada, acessa essa parte do código
if escolhaNav == 'Cadastrar':
    menuCadastrar()


# se a opção 'listar' for selecionada, acessa essa parte do código
elif escolhaNav == 'Listar carros':
    menuListar()


# se a opção 'pesquisar' for selecionada, acessa essa parte do código
elif escolhaNav == 'Pesquisar':
    menuPesquisar()


# se a opção 'vender' for selecionada, acessa essa parte do código
elif escolhaNav == 'Vender':
    menuVender()   