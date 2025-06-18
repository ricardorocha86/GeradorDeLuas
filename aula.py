import streamlit as st
import pandas as pd
from pycaret.classification import load_model, predict_model 
from sklearn import datasets

pagina = st.sidebar.radio('Página:', ['Calculadora de Calorias', 'Previsão de Sucesso em Tarefas']

if pagina == 'Calculadora de Calorias':
    
    st.title('Calculadora de Calorias em Repouso')
    
    
    idade = st.slider('Idade', 16, 85, 20, 1)
    altura =  st.slider('Altura', 100, 250, 170, 1)
    peso =  st.slider('Peso', 10, 200, 70, 1)
    
    #    homem: (13,75 x peso em quilos) + (5 x altura em centímetros) – (6,76 x idade em anos) + 66,5;
    #    mulher: (9,56 x peso em quilos) + (1,85 x altura em centímetros) – (4,68 x idade em anos) + 665.
    
    caloria_homem = 13.75*peso + 5*altura - 6.76*idade + 66.5 
    caloria_mulher = 9.56*peso + 1.85*altura - 4.68*idade + 665 
    
    st.metric(label = 'Caloria p/ Homem', value = caloria_homem)
    st.metric(label = 'Caloria p/ Mulher', value = caloria_mulher)

if pagina == 'Previsão de Sucesso em Tarefas':
    
    st.title('Deploy do Modelo para Classificação de Sucesso em Tarefas')
    
    modelo = load_model('modelo_final')
    
    hours_coding = st.slider_input('Horas programando:', 0., 12., 6., 0.1)
    coffee_intake_mg = st.slider_input('Café tomado (mg):', 0, 600, 500, 1)
    sleep_hours = st.slider_input('Café tomado (mg):', 3, 10, 7, 1)
    ai_usage_hours = st.slider_input('Café tomado (mg):', 0., 6.5, 3., 0.1)
    cognitive_load = st.slider_input('Café tomado (mg):', 1., 10., 5., .1)
    distractions = st.number_input('Café tomado (mg):', 0, 8, 1, 1)
    commits = st.number_input('Café tomado (mg):', 0, 13, 2, 1)
    bugs_reported = st.number_input('Café tomado (mg):', 0, 5, 1, 1)
    
     
    modelo = load_model('modelo_final')
    
    def PrevisorSucessoTarefa(hours_coding, coffee_intake_mg, distractions, sleep_hours, commits, bugs_reported, ai_usage_hours, cognitive_load):
    
        aux = {'hours_coding': [hours_coding], 
                  'coffee_intake_mg': [coffee_intake_mg], 
                  'distractions': [distractions], 
                  'sleep_hours': [sleep_hours], 
                  'commits': [commits], 
                  'bugs_reported': [bugs_reported],
                  'ai_usage_hours': [ai_usage_hours], 
                  'cognitive_load': [cognitive_load]}
    
        dados = pd.DataFrame(aux)
     
        pred = predict_model(modelo, data = dados)
        resp = 'NÃO' if pred['prediction_label'][0] == 0 else 'SIM'
        prob = pred['prediction_score'][0]
        return f'Previsão de Sucesso na Tarefa: *{resp}* com score de {prob}'
    
    
    if st.button('APLICAR O MODELO'): 
        saida = PrevisorSucessoTarefa(hours_coding, coffee_intake_mg, distractions, sleep_hours, commits, bugs_reported, ai_usage_hours, cognitive_load)
        st.success(saida)
    
     
