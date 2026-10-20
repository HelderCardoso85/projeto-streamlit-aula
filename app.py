import pandas as pd
import scipy.stats
import streamlit as st
import time

# Inicialização das variáveis de estado (session state)
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(
        columns=['no', 'iterations', 'mean']
    )

st.header('Jogando uma moeda')

# Gráfico de linhas com valor inicial
chart = st.line_chart([0.5])

# Função que simula o lançamento e calcula a média acumulada
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    
    mean = None
    outcome_no = 0
    outcome_1_count = 0
    
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)
        
    return mean

# Controlo deslizante e botão
number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)
start_button = st.button('Executar')

# Lógica ao clicar no botão Executar
if start_button:
    st.write(f'Executando o experimento de {number_of_trials} tentativas.')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trials)
    
    # Adiciona o resultado à tabela acumulativa
    st.session_state['df_experiment_results'] = pd.concat([
        st.session_state['df_experiment_results'],
        pd.DataFrame(
            data=[[st.session_state['experiment_no'], number_of_trials, mean]],
            columns=['no', 'iterations', 'mean']
        )
    ], axis=0)
    
    st.session_state['df_experiment_results'] = \
        st.session_state['df_experiment_results'].reset_index(drop=True)

# Exibe a tabela com o histórico de resultados
st.write(st.session_state['df_experiment_results'])