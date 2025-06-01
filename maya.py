import streamlit as st
import pandas as pd

st.markdown("""
    <style>
        /* Arrière-plan principal */
        .stApp {
            background-color: #fef9f6;
        }

        /* Message succès (st.success) en blanc sur vert */
        .stAlert {
            font-weight: 600;
            color: white !important;
            background-color: #45c191 !important;
            border-left: 6px solid #2ea37f;
            border-radius: 8px;
            padding: 1rem;
        }

        /* Texte général */
        html, body, [class*="css"] {
            color: #2e2e2e !important;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Titres */
        h1, h2, h3, h4 {
            color: #F63366 !important;
        }

        /* Champ texte */
        .stTextInput > div > div > input {
            background-color: #ffffff;
            color: #000000;
        }

        /* Slider */
        .stSlider > div {
            color: #2e2e2e;
        }

        /* Bouton */
        .stButton > button {
            background-color: #F63366;
            color: #1a1a1a;
            border-radius: 8px;
            padding: 0.5rem 1.2rem;
            font-weight: bold;
            border: none;
        }

        .stButton > button:hover {
            background-color: #d91c54;
            transition: background-color 0.3s ease;
        }

        .stButton > button:active {
            background-color: #d91c54;
            color: #1a1a1a;
        }

        /* Tableau - En-tête */
        .stDataFrame thead tr th {
            background-color: #F63366;
            color: white;
            font-weight: bold;
            font-size: 1rem;
            text-align: center;
        }

        /* Tableau - Corps */
        .stDataFrame tbody tr td {
            font-size: 0.9rem;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

criteria_weights = {
    "Présentation": 0.2,
    "Clarté": 0.3,
    "Pertinence du pitch": 0.4,
    "Réactivité aux questions": 0.1
}

st.title("Évaluation des courtiers par le jury")

if "resultats" not in st.session_state:
    st.session_state.resultats = []

courtier = st.text_input("Nom du courtier :")

notes = {}
for critere in criteria_weights:
    notes[critere] = st.slider(f"{critere} (sur 10)", 0, 10, 5)

if st.button("Enregistrer l'évaluation"):
    if courtier.strip() == "":
        st.warning("Veuillez entrer le nom du courtier.")
    else:
        score_final = sum(notes[critere] * criteria_weights[critere] for critere in criteria_weights)
        evaluation = {
            "Courtier": courtier,
            **notes,
            "Note finale": round(score_final, 2)
        }
        st.session_state.resultats.append(evaluation)
        st.success(f"Évaluation enregistrée pour {courtier} ({round(score_final, 2)}/10)")

if st.session_state.resultats:
    st.subheader("Courtiers évalués")
    df_resultats = pd.DataFrame(st.session_state.resultats)
    st.dataframe(df_resultats, use_container_width=True)
