import streamlit as st

# Configuración de la página
st.set_page_config(page_title="IA en Salud Mental", layout="centered")

# --- ESTILOS PERSONALIZADOS (Diseño minimalista con bordes redondeados) ---
st.markdown("""
    <style>
    .main-container {
        border: 1px solid #e6e6e6;
        padding: 30px;
        border-radius: 15px;
        background-color: #f9f9f9;
    }
    .quote-left {
        border-left: 5px solid #4A90E2;
        padding-left: 20px;
        color: #555;
        font-style: italic;
        margin-bottom: 30px;
    }
    .stat-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 1) Título del artículo [cite: 1, 2]
st.title("¿Un psicólogo en el bolsillo?")
st.subheader("La revolución (y los riesgos) de la IA en nuestra salud mental")

# 2) Frase motivadora alineada a la izquierda [cite: 3]
st.markdown('<div class="quote-left">"La tecnología puede ser el puente, pero el encuentro entre dos seres humanos seguirá siendo el destino."</div>', unsafe_allow_html=True)

# 3) Inicio del Artículo (Diseño minimalista) [cite: 4, 5]
with st.container():
    st.write("""
    En un mundo donde las citas con el psicólogo pueden tardar meses y los costos son prohibitivos, 
    una nueva figura emerge: el **chatbot de salud mental**. [cite: 5]
    """)
    
    # Dato relevante [cite: 6]
    st.info("Para 2025, el uso más común de la IA generativa es la búsqueda de apoyo emocional. [cite: 6]")

    # Metamorfosis [cite: 8, 10]
    st.header("La metamorfosis del acompañante digital")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**1. Guiones Rígidos**")
        st.caption("Sistemas basados en reglas y palabras clave como 'estoy triste'. [cite: 11, 12]")
    with col2:
        st.markdown("**2. Machine Learning**")
        st.caption("Uso de NLP para entender el tono y si el usuario está en crisis. [cite: 14, 15]")
    with col3:
        st.markdown("**3. Era de los LLM**")
        st.caption("Sistemas como ChatGPT que 'piensan' probabilísticamente. [cite: 16, 17]")

    # Evidencia Científica [cite: 19, 21]
    st.header("¿Qué dice la ciencia?")
    
    # Gráficos simples o métricas
    m1, m2, m3 = st.columns(3)
    m1.metric("Estudiantes", "-22%", "en depresión (IA con TCC) [cite: 24]")
    m2.metric("Adultos Mayores", "Puente", "contra la soledad [cite: 26]")
    m3.metric("Ansiedad", "-21%", "mejora promedio [cite: 27]")

    # Advertencias [cite: 28, 30]
    with st.expander("⚠️ Ver riesgos y 'puntos ciegos'"):
        st.error("**Alucinaciones:** Datos inventados que pueden incluir consejos médicos fatales. [cite: 35, 36, 37]")
        st.warning("**Empatía Artificial:** Riesgo de dependencia y abandono del contacto humano. [cite: 32, 34]")
        st.warning("**Vacío Legal:** Solo el 16% de las IAs avanzadas tienen pruebas de eficacia clínica. [cite: 39, 40]")

    # Conclusión [cite: 41, 48]
    st.divider()
    st.markdown("### El Futuro: La 'Receta' Digital Segura [cite: 41]")
    st.write("""
    El modelo ideal propone tres niveles: **Validación técnica, Pruebas de usuario y Eficacia clínica**. [cite: 43, 44, 45, 46]
    La IA es un excelente triaje inicial, pero la profundidad de la psique sigue necesitando la mirada humana. [cite: 47, 48]
    """)

# 4) Referencias (Botón desplegable) [cite: 49, 50]
with st.expander("📚 Ver Referencias Bibliográficas"):
    st.write("- Hua, Y., et al. (2024). Charting the evolution of artificial intelligence mental health chatbots. World Psychiatry. [cite: 51]")
    st.write("- Nyakhar, S. & Wang, H. (2025). Effectiveness of AI chatbots on mental health in college students. Front. Psychiatry. [cite: 52]")
    st.write("- Satake, Y., et al. (2026). Autonomous conversational agents for loneliness and depression in older people. Psychological Medicine. [cite: 53]")
    st.write("- Manole, A., et al. (2024). Harnessing AI in Anxiety Management. Information Journal. [cite: 54]")
    st.write("- Agencia SINC (2025). Chatbots y salud mental: ¿solución accesible o experimento peligroso? por Alberto Payo. [cite: 55]")
