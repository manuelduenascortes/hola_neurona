import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(
    page_title="Hola Neurona",
    page_icon="🧠",
    layout="wide"
)

# Función para calcular la salida de la neurona
def create_neuron_visualization(inputs, weights, bias=0):
    # Calcular la suma ponderada (y = w1*x1 + w2*x2 + ... + b)
    y = sum(i * w for i, w in zip(inputs, weights)) + bias
    return y

# Header con imagen y título
st.image("assets/neurona.jpg", use_container_width=True)
st.title("🧠 Hola neurona!")
st.markdown("---")

# Tres secciones
tab1, tab2, tab3 = st.tabs(["1 Entrada", "2 Entradas", "3 Entradas + Sesgo"])

# Una entrada
with tab1:
    st.header("Neurona con 1 Entrada")
    
    st.subheader("Parámetros")
    input1 = st.number_input("Valor de Entrada (x₁)", value=1.0, step=0.1, format="%.2f", key="tab1_input1")
    weight1 = st.slider("Peso (w₁)", -5.0, 5.0, 0.5, 0.1, key="tab1_weight1")
    
    y = create_neuron_visualization([input1], [weight1])
    
    st.subheader("Resultado")
    st.metric("Salida (y)", f"{y:.4f}")

# Dos entradas
with tab2:
    st.header("Neurona con 2 Entradas")
    
    st.subheader("Parámetros")
    input2_1 = st.number_input("Valor de Entrada 1 (x₁)", value=1.0, step=0.1, format="%.2f", key="tab2_input1")
    weight2_1 = st.slider("Peso 1 (w₁)", -5.0, 5.0, 0.5, 0.1, key="tab2_weight1")
    
    input2_2 = st.number_input("Valor de Entrada 2 (x₂)", value=2.0, step=0.1, format="%.2f", key="tab2_input2")
    weight2_2 = st.slider("Peso 2 (w₂)", -5.0, 5.0, 0.3, 0.1, key="tab2_weight2")
    
    y = create_neuron_visualization([input2_1, input2_2], [weight2_1, weight2_2])
    
    st.subheader("Resultado")
    st.metric("Salida (y)", f"{y:.4f}")

# Tres entradas + sesgo
with tab3:
    st.header("Neurona con 3 Entradas + Sesgo")
    
    st.subheader("Parámetros")
    
    # Crear dos columnas: valores a la izquierda, pesos a la derecha
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Valores de Entrada**")
        input3_1 = st.number_input("Valor de Entrada 1 (x₁)", value=1.0, step=0.1, format="%.2f", key="tab3_input1")
        input3_2 = st.number_input("Valor de Entrada 2 (x₂)", value=2.0, step=0.1, format="%.2f", key="tab3_input2")
        input3_3 = st.number_input("Valor de Entrada 3 (x₃)", value=-1.0, step=0.1, format="%.2f", key="tab3_input3")
        bias = st.number_input("Sesgo (b)", value=0.0, step=0.1, format="%.2f", key="tab3_bias")
    
    with col2:
        st.markdown("**Pesos**")
        weight3_1 = st.slider("Peso 1 (w₁)", -5.0, 5.0, 0.5, 0.1, key="tab3_weight1")
        weight3_2 = st.slider("Peso 2 (w₂)", -5.0, 5.0, 0.3, 0.1, key="tab3_weight2")
        weight3_3 = st.slider("Peso 3 (w₃)", -5.0, 5.0, 0.8, 0.1, key="tab3_weight3")
    
    y = create_neuron_visualization(
        [input3_1, input3_2, input3_3], 
        [weight3_1, weight3_2, weight3_3], 
        bias
    )
    
    st.subheader("Resultado")
    st.metric("Salida (y)", f"{y:.4f}")


