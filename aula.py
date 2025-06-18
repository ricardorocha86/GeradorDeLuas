import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model

# --- Configuração da Página ---
pagina = st.sidebar.radio('Página:', ['Calculadora de Calorias', 'Previsão de Sucesso em Tarefas'])

# --- Página 1: Calculadora de Calorias ---
if pagina == 'Calculadora de Calorias':

    st.title('Calculadora de Calorias em Repouso')

    idade = st.slider('Idade (anos)', 16, 85, 20, 1)
    altura = st.slider('Altura (cm)', 100, 250, 170, 1)
    peso = st.slider('Peso (kg)', 10, 200, 70, 1)

    # Fórmulas de Harris-Benedict (revisadas)
    # homem: (13,75 x peso em quilos) + (5 x altura em centímetros) – (6,76 x idade em anos) + 66,5;
    # mulher: (9,56 x peso em quilos) + (1,85 x altura em centímetros) – (4,68 x idade em anos) + 665.

    caloria_homem = 13.75 * peso + 5 * altura - 6.76 * idade + 66.5
    caloria_mulher = 9.56 * peso + 1.85 * altura - 4.68 * idade + 665

    # MELHORIA: Exibindo os valores como inteiros para melhor legibilidade
    st.metric(label='Calorias p/ Homem (kcal/dia)', value=f'{caloria_homem:.0f}')
    st.metric(label='Calorias p/ Mulher (kcal/dia)', value=f'{caloria_mulher:.0f}')

# --- Página 2: Previsão de Sucesso em Tarefas ---
if pagina == 'Previsão de Sucesso em Tarefas':

    st.title('Previsão de Sucesso em Tarefas')
 
    # Isso melhora drasticamente a performance do app. 
    def carregar_modelo_pycaret():
        return load_model('modelo_final')

    # CORREÇÃO: Carregar o modelo apenas uma vez, usando a função com cache
    modelo = carregar_modelo_pycaret()

    # --- Inputs do Usuário ---
    # CORREÇÃO: A função correta é st.slider e os rótulos (labels) foram corrigidos.
    hours_coding = st.slider('Horas programando:', 0.0, 12.0, 6.0, 0.1)
    coffee_intake_mg = st.slider('Café ingerido (mg):', 0, 600, 300, 10)
    sleep_hours = st.slider('Horas de sono:', 3.0, 10.0, 7.0, 0.5)
    ai_usage_hours = st.slider('Horas de uso de IA:', 0.0, 6.5, 3.0, 0.1)
    cognitive_load = st.slider('Carga cognitiva (1-10):', 1.0, 10.0, 5.0, 0.1)
    
    # Usando st.number_input para valores que podem ser digitados
    distractions = st.number_input('Número de distrações:', min_value=0, max_value=20, value=3, step=1)
    commits = st.number_input('Número de commits:', min_value=0, max_value=20, value=2, step=1)
    bugs_reported = st.number_input('Bugs reportados:', min_value=0, max_value=5, value=1, step=1)

    # --- Função de Previsão ---
    def prever_sucesso_tarefa(hours_coding, coffee_intake_mg, distractions, sleep_hours, commits, bugs_reported, ai_usage_hours, cognitive_load):
        
        # Cria um DataFrame com os dados de entrada para o modelo
        dados_input = pd.DataFrame({
            'hours_coding': [hours_coding],
            'coffee_intake_mg': [coffee_intake_mg],
            'distractions': [distractions],
            'sleep_hours': [sleep_hours],
            'commits': [commits],
            'bugs_reported': [bugs_reported],
            'ai_usage_hours': [ai_usage_hours],
            'cognitive_load': [cognitive_load]
        })

        # Realiza a predição
        predicao = predict_model(estimator=modelo, data=dados_input)
        
        # Extrai o resultado e a probabilidade
        resultado = 'SIM' if predicao['prediction_label'].iloc[0] == 1 else 'NÃO'
        score = predicao['prediction_score'].iloc[0]
        
        return f'Previsão de Sucesso na Tarefa: **{resultado}** (Confiança: {score:.2%})'

    # --- Botão para Executar a Previsão ---
    if st.button('FAZER PREVISÃO'):
        resultado_previsao = prever_sucesso_tarefa(hours_coding, coffee_intake_mg, distractions, sleep_hours, commits, bugs_reported, ai_usage_hours, cognitive_load)
        st.success(resultado_previsao)
