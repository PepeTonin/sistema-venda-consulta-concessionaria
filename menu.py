import streamlit as st
from menu_cadastros import *
from menu_listagens import *
from menu_vendas import *
from menu_pesquisas import *
from acoes import gerarResumoVendedor
from acoes import auxVenda_listarItens


def menuCadastrar():
    # título da seção
    st.header('Área de cadastros')
    # cria 3 abas, cada uma com um nome
    tab1, tab2, tab3 = st.tabs(['Cliente', 'Vendedor', 'Carro'])
    # se for selecionado 'cliente'
    with tab1:
        menuCadastrarCliente()
    # se for selecionado 'vendedor'
    with tab2:
        menuCadastrarVendedor()
    # se for selecionado 'carro'
    with tab3:
        menuCadastrarCarro()


def menuListar():
    # título da seção
    st.header('Listagens')
    # cria 2 abas, cada uma com um nome
    tab1, tab2 = st.tabs(['Carros a venda', 'Carros vendidos'])
    # se for selecionado 'carros a venda'
    with tab1:
        listarCarrosAVenda()
    # se for selecionado 'carros vendidos'
    with tab2:
        listarCarrosVendidos()


def menuPesquisar():
    # título da seção
    st.header('Área de pesquisas')
    # cria 2 abas, cada uma com um nome
    tab1, tab2 = st.tabs(['Pesquisar por vendedor', 'Pesquisar por cliente'])

    # se for selecionado 'Pesquisar por vendedor'
    with tab1:
        # importa o banco que será a base das buscas
        directory_path = r'banco/vendedores.xlsx'
        bancoBase_df = pd.read_excel(directory_path)

        if bancoBase_df.empty:
            st.write('Não há nenhuma venda lançada para esta categoria')

        else:
            with st.form('pesquisar por vendedor'):
                # cria uma lista suspensa com os dados de acordo com a base importada e retorna o index do item selecionado
                indexBaseSelecionado = listaSuspensa_menuPesquisar(bancoBase_df, 'vendedor')
                # botão de submit do form
                submitted = st.form_submit_button('Pesquisar')
                if submitted:
                    gerarResumoVendedor(bancoBase_df, indexBaseSelecionado)
                    pesquisarVendas(indexBaseSelecionado, 'vendedor')

    # se for selecionado 'Pesquisar por cliente'
    with tab2:
        # importa o banco que será a base das buscas
        directory_path = r'banco/clientes.xlsx'
        bancoBase_df = pd.read_excel(directory_path)

        if bancoBase_df.empty:
            st.write('Não há nenhuma venda lançada para esta categoria')
            
        else:
            with st.form('pesquisar por cliente'):
                # cria uma lista suspensa com os dados de acordo com a base importada e retorna o index do item selecionado
                indexBaseSelecionado = listaSuspensa_menuPesquisar(bancoBase_df, 'cliente')
                # botão de submit do form
                submitted = st.form_submit_button('Pesquisar')
                if submitted:
                    pesquisarVendas(indexBaseSelecionado, 'cliente')


def menuVender():
    # título da seção
    st.header('Área de venda')
    # cria 2 colunas que dividem espaço na tela de trabalho
    col1, col2 = st.columns(2)
    # aqui fica o que é mostrada na parte esquerda (coluna 1)
    with col1:
        realizarVenda()
    # aqui fica o que é mostrada na parte direita (coluna 2)
    with col2:
        # cria 3 abas, cada uma com um nome
        tab1, tab2, tab3 = st.tabs(['Listar vendedores', 'Listar clientes', 'Listar carros'])
        # para a aba 'Listar clientes'
        with tab1:
            auxVenda_listarItens('vendedores')
        # para a aba 'Listar carros'
        with tab2:
            auxVenda_listarItens('clientes')
        # para a aba 'Listar vendedores'
        with tab3:
            auxVenda_listarItens('carros')