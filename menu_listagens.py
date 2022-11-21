import pandas as pd
import streamlit as st


def listarCarrosAVenda():
    st.subheader('Carros a venda')
    # importa do banco a base de carros usando de index a coluna 'situacao'
    baseCarros_df = pd.read_excel(r'banco/carros.xlsx', index_col='situacao')
    # verifica se algum erro acontece ao tentar buscar o banco, se ocorrer algum, significa que não há dados
    try:
        # gera um DF apenas com os carros com indexador 'disponível'
        carrosDisponiveis_df = baseCarros_df.loc['disponivel']
        # mostra esse DF
        st.write(carrosDisponiveis_df)
    except:
        st.write('Não há carros disponíveis para venda')


def listarCarrosVendidos():
    st.subheader('Carros vendidos')
    # importa do banco a base de carros usando de index a coluna 'situacao'
    baseCarros_df = pd.read_excel(r'banco/carros.xlsx', index_col='situacao')
    # verifica se algum erro acontece ao tentar buscar o banco, se ocorrer algum, significa que não há dados
    try:
        # gera um DF apenas com os carros com indexador 'vendido'
        carrosVendidos_df = baseCarros_df.loc['vendido']
        # mostra esse DF
        st.write(carrosVendidos_df)
    except:
        st.write('Nenhum carro foi vendido ainda')