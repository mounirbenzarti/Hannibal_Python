import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Configuration de la page
st.set_page_config(
    page_title="L'Odyssée d'Hannibal Barca",
    page_icon="🐘",
    layout="wide"
)

# --- DONNÉES HISTORIQUES ---
# Les étapes clés de son voyage
steps = [
    {
        "titre": "Le Départ : Carthagène",
        "date": "218 av. J.-C.",
        "lieu": "Carthagène, Espagne",
        "coords": [37.6, -0.98],
        "desc": "Hannibal quitte la base carthaginoise en Espagne avec une armée massive (environ 90 000 fantassins et 12 000 cavaliers) et ses célèbres éléphants de guerre pour marcher sur Rome."
    },
    {
        "titre": "La Traversée du Rhône",
        "date": "Septembre 218 av. J.-C.",
        "lieu": "Rhône, France",
        "coords": [43.9, 4.8],
        "desc": "Hannibal doit faire traverser le fleuve à son armée et à ses éléphants, tout en évitant les forces romaines de Scipion et en combattant les tribus gauloises locales."
    },
    {
        "titre": "La Traversée des Alpes",
        "date": "Octobre 218 av. J.-C.",
        "lieu": "Les Alpes",
        "coords": [45.1, 6.8],
        "desc": "L'exploit légendaire. Dans le froid et la neige, Hannibal perd une grande partie de son armée et de ses éléphants, mais réussit l'impossible : entrer en Italie par le nord, surprenant totalement Rome."
    },
    {
        "titre": "La Bataille de la Trébie",
        "date": "Décembre 218 av. J.-C.",
        "lieu": "Rivière Trébie, Italie",
        "coords": [45.0, 9.6],
        "desc": "Première victoire majeure sur le sol italien. Hannibal utilise le terrain et une embuscade pour vaincre les légions romaines."
    },
    {
        "titre": "La Bataille de Cannes (Cannae)",
        "date": "2 août 216 av. J.-C.",
        "lieu": "Cannae, Italie",
        "coords": [41.3, 16.1],
        "desc": "Le chef-d'œuvre tactique. En infériorité numérique, Hannibal encercle et anéantit l'armée romaine. C'est considéré comme l'une des plus grandes manœuvres militaires de l'histoire."
    },
    {
        "titre": "Le Retour et la Défaite : Zama",
        "date": "202 av. J.-C.",
        "lieu": "Zama, Tunisie",
        "coords": [36.1, 9.2],
        "desc": "Rappelé en Afrique pour défendre Carthage, Hannibal est finalement vaincu par Scipion l'Africain. C'est la fin de la puissance carthaginoise."
    }
]

# --- FONCTIONS ---

def afficher_carte(selected_step_index):
    # Centrer la carte sur l'étape sélectionnée ou sur la Méditerranée par défaut
    center = steps[selected_step_index]["coords"]
    m = folium.Map(location=center, zoom_start=6, tiles="CartoDB positron")

    # Tracer la ligne du parcours complet
    route_coords = [step["coords"] for step in steps]
    folium.PolyLine(route_coords, color="red", weight=2.5, opacity=0.8, dash_array='5').add_to(m)

    # Ajouter les marqueurs
    for i, step in enumerate(steps):
        color = "red" if i == selected_step_index else "blue"
        icon = "star" if i == selected_step_index else "info-sign"
        
        folium.Marker(
            location=step["coords"],
            popup=step["titre"],
            tooltip=step["titre"],
            icon=folium.Icon(color=color, icon=icon)
        ).add_to(m)

    st_folium(m, width="100%", height=400)

# --- INTERFACE UTILISATEUR (UI) ---

st.title("🐘 L'Odyssée d'Hannibal Barca")
st.markdown("""
**Le fléau de Rome.** Cette application retrace le parcours incroyable du général carthaginois 
qui a osé défier Rome sur son propre territoire.
""")

st.divider()

# Création de deux colonnes : Menu à gauche, Contenu à droite
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Chronologie")
    # Sélecteur d'étape (Radio button stylisé)
    step_titles = [s["titre"] for s in steps]
    selected_step_name = st.radio("Sélectionnez une étape clé :", step_titles)
    
    # Trouver l'index de l'étape sélectionnée
    selected_index = step_titles.index(selected_step_name)
    current_step = steps[selected_index]

with col2:
    st.header(f"📍 {current_step['titre']}")
    st.subheader(f"📅 Date : {current_step['date']}")
    
    # Affichage de la description
    st.info(current_step['desc'])
    
    # Affichage de la carte
    st.markdown("### 🗺️ Carte Stratégique")
    afficher_carte(selected_index)

# Section "Le Saviez-vous" en bas
st.divider()
st.subheader("💡 Le Saviez-vous ?")
with st.expander("La tactique de Cannes"):
    st.write("""
    À Cannes, Hannibal a disposé ses troupes en forme de croissant convexe face aux Romains. 
    Au moment de l'impact, le centre a reculé volontairement tandis que les ailes avançaient, 
    créant un effet de tenaille qui a complètement encerclé l'armée romaine.
    """)

with st.expander("Les Éléphants"):
    st.write("""
    Sur les 37 éléphants partis d'Espagne, très peu survécurent à l'hiver italien. 
    Cependant, leur impact psychologique sur les légions romaines (qui n'avaient jamais vu de telles bêtes) fut immense au début de la campagne.
    """)
