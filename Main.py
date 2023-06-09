# Ce sont des instructions d'importation en Python, qui importent les bibliothèques et les modules
# nécessaires pour que le code s'exécute.
import streamlit as st
import pandas as pd
import data.data as dd

# Cette fonction affiche une carte avec un seul marqueur à une latitude et une longitude spécifiques.

def affichage_carte () :
    data_map = pd.DataFrame([[48.202047, -2.932644]], columns=["lat","lon"])
    st.map(data=data_map, zoom=None, use_container_width=True )

# Cette fonction affiche l'horaire d'une ligne de bus sélectionnée à partir d'une base de données
# MySQL dans une trame de données Streamlit.

def dataframe_ligne () :
    ligne_select = st.selectbox("De quelle ligne voulez-vous voir l'horaire ?", (1, 2, 3, 4))
    horaires = dd.sous_main()
    horaires["heure"] = horaires["heure"].astype(str)
    horaires_par_ligne = horaires.loc[horaires["ligne"] == ligne_select]
    st.dataframe(horaires_par_ligne)

# La fonction "principale" appelle deux autres fonctions, "affichage_carte" et "dataframe_ligne".
    
def principal():
    affichage_carte()
    dataframe_ligne ()

#appel de la fonction principal qui appelle les autres fonctions a la suite
st.title("Bienvenue dans notre application Breizhibus")
principal()




