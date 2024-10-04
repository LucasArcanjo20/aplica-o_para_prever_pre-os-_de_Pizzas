import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Leitura do arquivo CSV
df = pd.read_csv("pizzas.csv")

# Definindo as variáveis independentes e dependentes
x = df[["diametro"]]
y = df["preco"]

# Criando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(x, y)

st.title("Prevendo o valor de uma pizza")
st.divider()

# Solicita ao usuário que digite o tamanho do diâmetro da pizza
diametro = st.number_input('Digite o tamanho do diâmetro da pizza:')

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0]  # Acessa o primeiro elemento diretamente
    st.write(f"O valor da pizza com diâmetro de {diametro:.2f} cm é de R$ {preco_previsto:.2f}")
    st.balloons()