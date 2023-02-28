import pandas as pd
import numpy as np 
import streamlit as st
import altair as alt 
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_database():
    return pd.read_csv('brasil_estados.csv')

st.title('Meu primeiro App - GCI')

estados = load_database()

dados, estatisica = st.tabs(['Dados', 'Estatística Descritiva'])

with dados:
    regiao = st.selectbox(
        'Selecione a região:',
        estados['regiao_nome'].unique()
    )
    st.dataframe(estados[estados['regiao_nome'] == regiao])

with estatisica:
    variavel = st.selectbox(
        'Selecione a variável:',
        ['area', 'populacao', 'idh', 'matricula'],
    )
    st.table(estados[variavel].describe())