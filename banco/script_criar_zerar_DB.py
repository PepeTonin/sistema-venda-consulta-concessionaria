import pandas as pd

# criar os dicionarios base que serão os bancos de dados
clientes = {
    # inteiro
    'id': None,
    # string
    'nome': None,
    # string
    'CPF': None,
    # string
    'telefone': None,
    # string
    'endereco': None
}

vendedores = {
    # inteiro
    'id': None,
    # string
    'nome': None,
    # string
    'CPF': None,
    # string
    'telefone': None,
    # inteiro
    'vendas_realizadas': None,
    # float
    'valor_total_vendido': None
}

carros = {
    # inteiro
    'id': None,
    # string
    'marca': None,
    # string
    'modelo': None,
    # string
    'placa': None,
    # float
    'valor': None,
    # string
    'situacao': None
}

vendas = {
    # inteiro
    'id': None,
    # inteiro
    'id_cliente': None,
    # inteiro
    'id_vendedor': None,
    # inteiro
    'id_carro': None,
    # float
    'valor_real_venda': None
}

# transforma o dicionario em DataFrame depois o salva em arquivos excel
clientes_df = pd.DataFrame([clientes])
clientes_df.to_excel('banco/clientes.xlsx', index=False)

vendedores_df = pd.DataFrame([vendedores])
vendedores_df.to_excel('banco/vendedores.xlsx', index=False)

carros_df = pd.DataFrame([carros])
carros_df.to_excel('banco/carros.xlsx', index=False)

vendas_df = pd.DataFrame([vendas])
vendas_df.to_excel('banco/vendas.xlsx', index=False)
