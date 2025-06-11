import streamlit as st

st.title('Gerador de Luas')

from sklearn import datasets

n = st.slider('Tamanho amostral', 50, 1000, 500, 50)

bagunca = st.slider('Bagunça nos dados', 0, 1000, 200, 50)

X, Y = datasets.make_moons(n_samples = n, noise = bagunca/1000, random_state = 1)

import matplotlib.pyplot as plt

plt.scatter(X[:, 0], X[:, 1], c = Y, marker = 's', alpha = 0.5, cmap = 'Spectral')
plt.axis('off') 

st.pyplot()
