import streamlit as st
# calculo_normal.py

def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal (IMC)"""
    if altura == 0:
        return 0
    return peso / (altura * altura)

st.title("--- Calculadora de IMC ---")


# Entradas do usuário com valores padrão e limites
peso_usuario = st.number_input(
    "Digite seu peso (em kg):", 
    min_value=0.1, 
    value=70.0, 
    step=0.5
)

altura_usuario = st.number_input(
    "Digite sua altura (em metros, ex: 1.75):", 
    min_value=0.1, 
    value=1.70, 
    step=0.01,
    format="%.2f"
)

# Botão para executar o cálculo
if st.button("Calcular IMC"):
    if altura_usuario > 0:
        imc = calcular_imc(peso_usuario, altura_usuario)

        st.success(f"Seu IMC é: {imc:.2f}")

        # Classificação
        if imc < 18.5:
            st.info("Classificação: Abaixo do peso")
        elif imc < 24.9:
            st.warning("Classificação: Peso normal")
        elif imc < 29.9:
            st.error("Classificação: Sobrepeso")
        else:
            st.error("Classificação: Obesidade")
    else:
        st.error("A altura deve ser maior que zero.")
