import streamlit as st

st.title('Calculadora de Calorias em Repouso')

from sklearn import datasets

idade = st.slider('Idade', 16, 85, 20, 1)
altura =  st.slider('Altura', 100, 250, 170, 1)
peso =  st.slider('Peso', 10, 200, 70, 1)

#    homem: (13,75 x peso em quilos) + (5 x altura em centímetros) – (6,76 x idade em anos) + 66,5;
#    mulher: (9,56 x peso em quilos) + (1,85 x altura em centímetros) – (4,68 x idade em anos) + 665.

caloria_homem = 13.75*peso + 5*altura - 6.76*idade + 66.5 
caloria_mulher = 9.56*peso + 1.85*altura - 4.68*idade + 665 

st.metric(label = 'Caloria p/ Homem', value = caloria_homem)
st.metric(label = 'Caloria p/ Mulher', value = caloria_mulher)
