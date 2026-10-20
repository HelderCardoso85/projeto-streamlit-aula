import pandas as pd
import scipy.stats
import streamlit as st

# Inicialização das variáveis de estado (session state)
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0

if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(
        columns=['no', 'iterations', 'mean']
    )

st.header('Jogando uma moeda')

# Função que simula o lançamento de moedas e calcula as médias acumuladas
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    
    means = []
    outcome_no = 0
    outcome_1_count = 0
    
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        means.append(outcome_1_count / outcome_no)
        
    # Desenha o gráfico de linha com a evolução das médias
    st.line_chart(means)
    
    # Retorna a média final
    return means[-1]

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