# exibir grafico de barrar
# exibir a tabela filtrado


import streamlit as st
import pandas as pd
import plotly.express as px
#Ler os dados
st.set_page_config(page_title="Painel de Entregas", layout="wide")

df = pd.read_excel("Entregas.xlsx")

#Lista de categoria
categorias = ["Todos"] + list(df["Categoria"].unique())

#Construir o select box (categoria)
filtro_categoria = st.selectbox("Selecione a categoria:", categorias)

# Lista de tipos de veiculo
tipoVeiculo = ["Todos"] + list(df["Veiculo"].unique())

# Construir o select box (tipo veiculo)
filtro_veiculo = st.selectbox("Selecione o veiculo :", tipoVeiculo)

# Calcular metricas
st.subheader("Total de entregas:")
st.text(f"{len(df)}")

# Exibir as metricas
st.subheader("Soma do valor dos fretes:")
soma_fretes = df["Valor_Frete"].sum()
st.write(f"Valor total: R$ {soma_fretes :,.2f}")

# Agrupar os dados por estado

estado = df.groupby('Estado_Entrega')['Cliente'].count().reset_index()
st.bar_chart(data= estado, x='Estado_Entrega', y= 'Cliente')

dados_filtrados = df[(df['Categoria'] == filtro_categoria) & (df['Veiculo'] == filtro_veiculo)]
st.dataframe (dados_filtrados)