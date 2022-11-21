import pandas as pd
import streamlit as st
from acoes import inserirDadoNoBanco

def realizarVenda():
    # inicializa o form para realizar venda
    with st.form('realizar venda'):
        # entradas de dados
        vendedor = st.text_input('id vendedor')
        cliente = st.text_input('id cliente')
        carro = st.text_input('id carro')
        valorRealVenda = st.text_input('valor venda')
        # transforma as entradas em dicionário
        venda = {
            'id_vendedor': vendedor,
            'id_cliente': cliente,
            'id_carro': carro,
            'valor_real_venda': valorRealVenda
        }

        # botao para efetivar venda -> submit form
        submitted = st.form_submit_button('Realizar venda')

        if submitted:
            # validação dos dados de entrada
            if not(vendedor.isnumeric()) or not(cliente.isnumeric()) or not(carro.isnumeric()) or not(valorRealVenda.isnumeric()):
                st.error('Entradas não são válidas')

            # caso os dados sejam validados o fluxo de dados avança
            else:

                # tenta localizar um dado no banco de carros, caso não localize, significa que o id digitado se refere a um item válido
                try:

                    # importa o banco de carros
                    carros_df = pd.read_excel('banco/carros.xlsx')
                    # busca a situação dele -> vendido ou disponivel
                    situacaoCarro = carros_df.iloc[int(carro)]['situacao']

                    # se estiver vendido, finaliza o fluxo de dados
                    if situacaoCarro == 'vendido':
                        st.error('Este carro já foi vendido')

                    # se estiver disponível, segue
                    else:

                        # tenta localizar um dado no banco de vendedores, caso não localize, significa que o id digitado se refere a um item válido
                        try:

                            # importa o banco de vendedores
                            vendedores_df = pd.read_excel('banco/vendedores.xlsx')
                            # busca os dados do vendedor -> vendas realizadas e valor vendido
                            vendasRealizadas = int(vendedores_df.iloc[int(vendedor)]['vendas_realizadas'])
                            valorTotalVendido = float(vendedores_df.iloc[int(vendedor)]['valor_total_vendido'])

                            # tenta localizar um dado no banco de clientes, caso não localize, significa que o id digitado se refere a um item válido
                            try:

                                # importa o banco de clientes
                                clientes_df = pd.read_excel('banco/clientes.xlsx')
                                # busca um dado --> finalidade apenas de verificar se o id é válido, dado não será usado
                                clientes_df.iloc[int(cliente)]['CPF']
                                
                                ## PROGRAMA SÓ CHEGA NESSA PARTE SE TODAS AS VALIDAÇÕES FOREM SATISFEITAS ##

                                # gatilho -> altera situação do carro no banco de carros
                                # atualiza a situação do carro no banco de carros, de disponivel para vendido
                                atualizacaoSituacao = pd.DataFrame({'situacao': 'vendido'}, index=[int(carro)])
                                carros_df.update(atualizacaoSituacao)
                                carros_df.to_excel('banco/carros.xlsx', index=False)

                                # gatilho -> atualiza os dados de quantidade de vendas e valor total vendido, no banco dos vendedores
                                # atualiza os dados do vendedor no banco de vendedores
                                valorTotalVendido += float(valorRealVenda)      # soma o valor da venda atual no valor total vendido
                                vendasRealizadas += 1                           # soma 1 nas vendas realizadas
                                atualizacaoVendedor = pd.DataFrame({'vendas_realizadas': vendasRealizadas, 'valor_total_vendido': valorTotalVendido}, index=[int(vendedor)])
                                vendedores_df.update(atualizacaoVendedor)
                                vendedores_df.to_excel('banco/vendedores.xlsx', index=False)

                                st.success('Venda realizada com sucesso')

                                # função para inserir este novo dado no banco de vendas
                                inserirDadoNoBanco(venda, 'banco/vendas.xlsx')
                            
                            # mensagens de erro das validações
                            except:
                                st.error('ID do cliente incorreto')
                        except:
                            st.error('ID do vendedor incorreto')
                except:
                    st.error('ID do carro inválido')