import pandas as pd
import streamlit as st

def listaSuspensa_menuPesquisar(bancoBase_df, base):
    # padrões para vendedor
    if base == 'vendedor':
        selectboxHeader = 'Selecione o vendedor que deseja pesquisar'

    # padrões para cliente
    if base == 'cliente':
        selectboxHeader = 'Selecione o cliente que deseja pesquisar'

    # transforma em lista as colunas 'nome' e 'cpf' do banco base
    listaNomes = bancoBase_df['nome'].tolist()
    listaCPFs = bancoBase_df['CPF'].tolist()
    
    # adiciona esses valores a uma lista que será a base da lista suspensa do STREAMLIT
    conteudoListaSuspensa = []
    for i in range(len(listaNomes)):
        conteudoListaSuspensa.append(f'Nome: {listaNomes[i]}  --  CPF: {listaCPFs[i]}')

    # cria a lista suspensa
    opcaoSelecionada = st.selectbox(selectboxHeader, conteudoListaSuspensa)

    # i recebe o index da lista do valor da opção selecionada
    i = conteudoListaSuspensa.index(opcaoSelecionada)

    # retorna este index
    return i

def pesquisarVendas(i, base):
    # padrões para vendedor
    if base == 'vendedor':
        id_buscado = 'id_vendedor'
    # padrões para cliente
    if base == 'cliente':
        id_buscado = 'id_cliente'

    # importa o banco de vendas
    bancoVendas_df = pd.read_excel(r'banco/vendas.xlsx')

    # cria um outro DataFrame, filtrando a base de vendas e buscando apenas as vendas com base no id buscado
    # 'id_vendedor' para base de vendedores - 'id_cliente' para base de clientes
    vendasFiltradas_df = bancoVendas_df[bancoVendas_df[id_buscado] == i]

    # verifica se o DF 'vendasFiltradas_df' está vazio, ou seja, o item buscado não participou de nenhuma venda até o momento, seja cliente ou vendedor
    if vendasFiltradas_df.empty:
        st.write('Não há itens para serem listados')

    # caso não esteja vazio, realiza a listagem das vendas
    else:
        # importa os bancos que serão usados
        bancoVendedores_df = pd.read_excel(r'banco/vendedores.xlsx')
        bancoClientes_df = pd.read_excel(r'banco/clientes.xlsx')
        bancoCarros_df = pd.read_excel(r'banco/carros.xlsx')

        # cria listas, a partir do DF filtrado, contendo os valores:
        # ids dos clientes
        listaClientesVendas = vendasFiltradas_df['id_cliente'].tolist()
        # ids dos vendedores
        listaVendedoresVendas = vendasFiltradas_df['id_vendedor'].tolist()
        # ids dos carros
        listaCarrosVendas = vendasFiltradas_df['id_carro'].tolist()
        # valores reais de venda
        listaValoresVendas = vendasFiltradas_df['valor_real_venda'].tolist()

        # cria um DF com as colunas 'Cliente', 'CPF', 'Marca', 'Modelo', 'Placa', 'Vendedor' ,'Valor da venda', sem dados
        # esse DF irá receber os dados das vendas que posteriormente serão printados na tela
        vendasRealizadas_df = pd.DataFrame(data=None, columns=['Cliente', 'CPF', 'Marca', 'Modelo', 'Placa', 'Vendedor' ,'Valor da venda'])

        # for que rodará de acordo com quantas vendas foram realizadas
        for i in range(len(vendasFiltradas_df)):
            
            # localiza o item (linha inteira) no respectivo banco, com base no item armazenado no index i da lista contendo os ids já filtrados
            carroVendido_itemDF = bancoCarros_df.iloc[listaCarrosVendas[i]]
            cliente_itemDF = bancoClientes_df.iloc[listaClientesVendas[i]]
            vendedor_itemDF = bancoVendedores_df.iloc[listaVendedoresVendas[i]]

            # localiza o valor de cada um dos itens presentes do DF que deseja-se mostrar e os armazena
            cliente = cliente_itemDF['nome']
            cpf = cliente_itemDF['CPF']
            marca = carroVendido_itemDF['marca']
            modelo = carroVendido_itemDF['modelo']
            placa = carroVendido_itemDF['placa']
            vendedor = vendedor_itemDF['nome']
            valor = listaValoresVendas[i]

            # gera um novo DF contendo esses valores
            novoDado_df = pd.DataFrame({'Cliente': cliente, 'CPF': cpf, 'Marca': marca, 'Modelo': modelo, 'Placa':placa, 'Vendedor':vendedor,'Valor da venda':valor}, index=[i])

            # concatena esse novo DF com o DF previamente criado que será mostrado ao final
            vendasRealizadas_df = pd.concat([vendasRealizadas_df, novoDado_df], ignore_index=False)

        st.write(vendasRealizadas_df)