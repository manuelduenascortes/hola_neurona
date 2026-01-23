import streamlit as st

st.set_page_config(page_title="Hola Neurona", page_icon="🧠")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def calcular_neurona(inputs, weights, bias=0):
    return sum(i * w for i, w in zip(inputs, weights)) + bias

st.image("assets/neurona.jpg", width=1200)
st.title("🧠 Hola neurona!")
st.markdown("---")

tab1, tab2, tab3 = st.tabs(["1 Entrada", "2 Entradas", "3 Entradas + Sesgo"])

with tab1:
    st.header("Neurona con 1 Entrada")
    x1 = st.number_input("Entrada (x₁)", value=1.0, step=0.1, key="t1_x1")
    w1 = st.slider("Peso (w₁)", -5.0, 5.0, 0.5, 0.1, key="t1_w1")
    y = calcular_neurona([x1], [w1])
    st.metric("Salida (y)", f"{y:.2f}")

with tab2:
    st.header("Neurona con 2 Entradas")
    x1 = st.number_input("Entrada 1 (x₁)", value=1.0, step=0.1, key="t2_x1")
    w1 = st.slider("Peso 1 (w₁)", -5.0, 5.0, 0.5, 0.1, key="t2_w1")
    x2 = st.number_input("Entrada 2 (x₂)", value=2.0, step=0.1, key="t2_x2")
    w2 = st.slider("Peso 2 (w₂)", -5.0, 5.0, 0.3, 0.1, key="t2_w2")
    y = calcular_neurona([x1, x2], [w1, w2])
    st.metric("Salida (y)", f"{y:.2f}")

with tab3:
    st.header("Neurona con 3 Entradas + Sesgo")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Entradas**")
        x1 = st.number_input("Entrada 1 (x₁)", value=1.0, step=0.1, key="t3_x1")
        x2 = st.number_input("Entrada 2 (x₂)", value=2.0, step=0.1, key="t3_x2")
        x3 = st.number_input("Entrada 3 (x₃)", value=-1.0, step=0.1, key="t3_x3")
        b = st.number_input("Sesgo (b)", value=0.0, step=0.1, key="t3_b")
    
    with col2:
        st.markdown("**Pesos**")
        w1 = st.slider("Peso 1 (w₁)", -5.0, 5.0, 0.5, 0.1, key="t3_w1")
        w2 = st.slider("Peso 2 (w₂)", -5.0, 5.0, 0.3, 0.1, key="t3_w2")
        w3 = st.slider("Peso 3 (w₃)", -5.0, 5.0, 0.8, 0.1, key="t3_w3")
    
    y = calcular_neurona([x1, x2, x3], [w1, w2, w3], b)
    st.metric("Salida (y)", f"{y:.2f}")
