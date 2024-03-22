import yfinance as yf #Biblioteca de dados do mercado
import pandas as pd 
import streamlit as st
from datetime import datetime
 
st.markdown('# Análise de mercado') #Título

ticker = st.text_input('Entre com o código ticker: ') #Entrada para o usuário digitar o código

st.markdown(f'## Você está vendo os dados da {ticker}')

dados = yf.Ticker(ticker)

#Notícias
st.markdown('Notícias')
dados_noticias = pd.DataFrame(dados.news) #Completo
dados_noticias=dados_noticias.reset_index() #Para que as linhas de cabeçalho sejam de cabeçalho e não de conteúdo
st.dataframe(dados_noticias)

#Pegar apenas as colunas que eu quero
#st.markdown('Notícias filtradas')
#dados_noticias2 = dados_noticias[['title', 'publisher', 'link', 'relatedTickers']] #Apenas as colunas que eu quero
#st.dataframe(dados_noticias2)

#Datas
data_final = datetime.now().strftime('%Y-%m-%d')

#Dados históricos
st.markdown('Dados históricos')
dados_historicos = dados.history(period='max', start = '2019-03-16', end = data_final, interval='5d')
dados_historicos = dados_historicos.reset_index() #Para que as linhas de cabeçalho sejam de cabeçalho e não de conteúdo
st.dataframe(dados_historicos) 

#Gráfico do valor de fechamento por data
st.markdown('# Construa seu gráfico')

eixo_x = st.selectbox('Eixo x: ', dados_historicos.columns)
eixo_y = st.selectbox('Eixo y: ', dados_historicos.columns)

st.markdown(f'Gráfico de {eixo_y} por {eixo_x}')

st.line_chart(dados_historicos, x=eixo_x, y=eixo_y)