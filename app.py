import random
import streamlit as st

st.title("Lançador de Moedas 🪙")
st.write("Este aplicativo simula o lançamento de uma moeda quantas vezes quiser.")

# Número de lançamentos escolhido pelo utilizador
num_lances = st.slider(
    "Quantas vezes quer lançar a moeda?", min_value=1, max_value=100, value=5
)

if st.button("Lançar Moedas"):
  resultados = [
      random.choice(["Cara", "Coroa"]) for _ in range(num_lances)
  ]

  st.write(f"Resultados dos {num_lances} lançamentos:")
  st.write(resultados)

  # Contagem de caras e coroas
  caras = resultados.count("Cara")
  coroas = resultados.count("Coroa")

  st.success(f"Total de Caras: {caras} | Total de Coroas: {coroas}")