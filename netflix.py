import streamlit as st
import pandas as pd
import codecs as co


st.title("Netflix app")
DATA_URL =co.open('movies.csv', 'rU', 'latin1')
#creacion de cache
@st.cache
def load_data(nrows):
    
    data=pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state =st.text('Load data...')
data=load_data(500)
data_load_state.text("Done! (using st.cache)")



#side bar
sidebar = st.sidebar
sidebar.title("Rodrigo Mencias Gonzalez")
sidebar.title("zs20006748")
sidebar.image("logo.jpg")
sidebar.title("Opciones:")
agree = sidebar.checkbox("mostrar todos los filmes")
if agree:
    st.dataframe(data)

#busqueda por nombre
@st.cache
def load_data_byname(name):
    data =pd.read_csv(DATA_URL)
    filtered_data_byname =data[data["name"].str.contains(name)]
    return filtered_data_byname

name = sidebar.text_input("Titulo del filme")
btnbuscar = sidebar.button('Buscar filme')

if(btnbuscar):
    filterbyname = load_data_byname(name)
    count_row = filterbyname.shape[0]
    st.write("total names: {count_row}")

    st.dataframe(filterbyname)

#selected box
@st.cache
def load_data_bydir(direct):
    data =pd.read_csv(DATA_URL)
    filtered_data_bydir = data[data['director'] == direct]

    return filtered_data_bydir

selected_sex =sidebar.selectbox('Seleccionar director ', data['director'].unique())
btndirector = sidebar.button('filtrar')

if(btndirector):
    filterbysex =load_data_bydir(selected_sex)
    count_row = filterbysex.shape[0]
    st.write(f"Total items: {count_row}")

    st.dataframe(filterbysex)
