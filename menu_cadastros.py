import streamlit as st
from time import sleep
from acoes import inserirDadoNoBanco

global delay_para_cadastro
delay_para_cadastro = 0.35

# função auxiliar para fazer a validaçao de dados
# valida se o dado é numérico ou nao, o método "isnumeric" não funciona para float
def isNumber(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def menuCadastrarCliente():
    # texto para facilitar a interpretação do usuário
    st.subheader('Cadastro de cliente')

    # início do formulário para submeter os dados do cliente
    with st.form('cadastro de cliente'):
        # entradas do usuário
        nome = st.text_input('nome')
        cpf = st.text_input('CPF')
        telefone = st.text_input('telefone')
        endereco = st.text_input('endereco')
        # transforma as entradas em dicionário
        novoCliente = {
            'nome': nome,
            'CPF': cpf,
            'telefone': telefone,
            'endereco': endereco
        }
        # botao para cadastrar cliente no banco de dados -> submit form
        submitted = st.form_submit_button('Cadastrar Cliente')
        if submitted:
            # validacao dos dados de entrada -> se ocorrer algum erro, não grava o novo dado no banco
            if nome == '' or telefone == '' or endereco == '' or cpf == '':
                st.error('Erro ao cadastrar cliente')
            # se os dados forem validados corretamente, eles são passados para a função que armazena em banco e da um feedback positivo ao usuário
            else:
                with st.spinner('Cadastrando...'):
                    sleep(delay_para_cadastro)
                    inserirDadoNoBanco(novoCliente, r'banco/clientes.xlsx')
                    st.success('Cliente cadastrado')
                    

def menuCadastrarVendedor():
    # texto para facilitar a interpretação do usuário
    st.subheader('Cadastro de vendedor')

    # início do formulário para submeter os dados do vendedor
    with st.form('cadastro de vendedor'):
        # entradas do usuário
        nome = st.text_input('nome')
        cpf = st.text_input('CPF')
        telefone = st.text_input('telefone')
        # transforma as entradas em dicionário
        novoVendedor = {
            'nome': nome,
            'CPF': cpf,
            'telefone': telefone,
            'vendas_realizadas': 0,
            'valor_total_vendido': 0
        }
        # botao para cadastrar vendedor no banco de dados -> submit form
        submitted = st.form_submit_button('Cadastrar Vendedor')
        if submitted:
            # validacao dos dados de entrada -> se ocorrer algum erro, não grava o novo dado no banco
            if nome == '' or telefone == '' or cpf == '':
                st.error('Erro ao cadastrar vendedor')
            # se os dados forem validados corretamente, eles são passados para a função que armazena em banco e da um feedback positivo ao usuário
            else:
                with st.spinner('Cadastrando...'):
                    sleep(delay_para_cadastro)
                    inserirDadoNoBanco(novoVendedor, r'banco/vendedores.xlsx')
                    st.success('Vendedor cadastrado')
                    

def menuCadastrarCarro():
    # texto para facilitar a interpretação do usuário
    st.subheader('Cadastro de carro')
    # início do formulário para submeter os dados do carro
    with st.form('cadastro de carro'):
        # entradas do usuário
        marca = st.text_input('marca')
        modelo = st.text_input('modelo')
        placa = st.text_input('placa')
        valor = st.text_input('valor')
        # transforma as entradas em dicionário
        novoCarro = {
            'marca': marca,
            'modelo': modelo,
            'placa': placa,
            'valor': valor,
            'situacao': 'disponivel'
        }
        # botao para cadastrar carro no banco de dados -> submit form
        submitted = st.form_submit_button('Cadastrar Carro')
        if submitted:
            # validacao dos dados de entrada -> se ocorrer algum erro, não grava o novo dado no banco
            # função "isNumber" definida neste arquivo mesmo
            if modelo == '' or marca == '' or placa == '' or not(isNumber(valor)):
                st.error('Erro ao cadastrar carro')
            # se os dados forem validados corretamente, eles são passados para a função que armazena em banco e da um feedback positivo ao usuário
            else:
                with st.spinner('Cadastrando...'):
                    sleep(delay_para_cadastro)
                    inserirDadoNoBanco(novoCarro, r'banco/carros.xlsx')
                    st.success('Carro cadastrado')