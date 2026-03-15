import streamlit as st
import pandas as pd

st.title("Agente de Planificación de Auditoría Ciber")

st.header("1. Información del Encargo")

auditoria = st.text_input("Nombre de la auditoría")
auditor = st.text_input("Auditor responsable")

st.header("2. Clasificación del Alcance")

q1 = st.radio(
"¿El alcance es a Gobierno o Estrategia de Ciberseguridad?",
["SI","NO"]
)

dominio = None

if q1 == "SI":

    dominio = "Aplicar RT Ciber (3 dominios)"

else:

    q2 = st.radio(
    "¿El alcance es a Gestión de Riesgos?",
    ["SI","NO"]
    )

    if q2 == "SI":

        dominio = "Dominio Gobierno"

    else:

        q3 = st.radio(
        "¿El alcance es a proceso específico?",
        ["SI","NO"]
        )

        if q3 == "SI":

            dominio = "Dominio Gestión de Riesgos"

        else:

            q4 = st.radio(
            "¿El alcance es a control específico?",
            ["SI","NO"]
            )

            if q4 == "SI":

                dominio = "Dominio Controles"

            else:

                dominio = "Evaluar mediante análisis de riesgo"

st.success("Dominio sugerido: " + dominio)

st.header("3. Evaluación de Activos")

numero = st.number_input(
"Cantidad de sistemas a evaluar",
1,
20,
1
)

risk_questions = [

("Incluye sistemas o aplicaciones",3),
("Procesa información organizacional",3),
("Impacto en operaciones o reputación",4),
("Controles de seguridad relevantes",6),
("Sistema crítico",3),
("Requisito regulatorio",3),
("Conectado a terceros o nube",2),
("Incidentes previos",3),
("Expuesto a internet",4)

]

resultados = []

for i in range(numero):

    st.subheader("Sistema " + str(i+1))

    nombre = st.text_input("Nombre del sistema",key=i)

    score = 0

    justificaciones = []

    for q,w in risk_questions:

        r = st.radio(q,["SI","NO"],key=str(i)+q)

        if r == "SI":

            score += w
            justificaciones.append(q)

    if score >= 15:

        decision = "APLICA"

    elif score >= 8:

        decision = "APLICA PARCIAL"

    else:

        decision = "NO APLICA"

    resultados.append({
        "Sistema":nombre,
        "Score":score,
        "Decision":decision,
        "Justificacion":"; ".join(justificaciones)
    })

df = pd.DataFrame(resultados)

st.header("4. Resultado")

st.dataframe(df)

csv = df.to_csv(index=False)

st.download_button(
"Descargar resultado",
csv,
"evaluacion_rt_ciber.csv"
)

st.info(
"Esta herramienta apoya la decisión del auditor. "
"El juicio profesional es el criterio final."
)