import pandas as pd
import streamlit as st


def inserirDadoNoBanco(novoDado, directory_path):
    # importa a base de dados, que foi dada como parâmetro da função
    base_df = pd.read_excel(directory_path)
    # caso o DataFrame esteja vazio, cria o primeiro elemento com o ID 0
    if base_df.empty:
        # cria um novo dicionário com a key 'id' e com o valor do id = 0
        novoPar = {'id': 0}
    # caso o DataFrame não esteja vazio, adiciona o item com o id anterior + 1
    else:
        # verifica o id anterior
        idAnterior = int(base_df.iloc[-1]['id'])
        # cria um novo dicionário com a key 'id' e com o valor do id anterior + 1
        novoPar = {'id': (idAnterior+1)}
    # adiciona esse par no dicionário de entrada
    novoDado.update(novoPar)
    # transforma o dado da entrada atualizado em DataFrame
    novoDado_df = pd.DataFrame([novoDado])
    # concatena esse novo DF ao banco de dados importado
    novo_df = pd.concat([base_df, novoDado_df], ignore_index=True)
    # salva o arquivo atualizado no mesmo local
    novo_df.to_excel(directory_path, index=False)


def gerarResumoVendedor(bancoBase_df, i):          
    # gera um resuminho do vendedor antes de listar as vendas
    # com o index e o DF base passados como parametro, busca os dados necessários e os mostra na tela
    vendasRealizadas = int(bancoBase_df.iloc[i]['vendas_realizadas'])
    valorTotalVendido = float(bancoBase_df.iloc[i]['valor_total_vendido'])
    nomeVendedor = bancoBase_df.iloc[i]['nome']
    # gera um resuminho com base nos dados
    if vendasRealizadas > 1:
        resumoVendedorOutput = f'O vendedor **{nomeVendedor}** realizou **{vendasRealizadas}** vendas, totalizando **R${valorTotalVendido:,.2f}**'
    elif vendasRealizadas == 1:
        resumoVendedorOutput = f'O vendedor **{nomeVendedor}** realizou **uma** venda de **R${valorTotalVendido:,.2f}**'
    else:
        resumoVendedorOutput = f'O vendedor **{nomeVendedor}** ainda não realizou nenhuma venda'
    # print do resultado na tela
    st.markdown(resumoVendedorOutput)


def auxVenda_listarItens(base):
    # padrões para cada um dos parametros possíveis
    if base == 'vendedores':
        directory_path = 'banco/vendedores.xlsx'
        colunasMostradas = ['nome','CPF']
    if base == 'clientes':
        directory_path = 'banco/clientes.xlsx'
        colunasMostradas = ['nome','CPF']
    if base == 'carros':
        directory_path = 'banco/carros.xlsx'
        colunasMostradas = ['modelo','placa','valor']
    # importa a base correta
    base_df = pd.read_excel(directory_path)
    if base_df.empty:
        st.write('Não há itens para serem mostrados')
    else:
        # mostra a tabela com as colunas desejadas
        st.write(base_df[colunasMostradas])