import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import data.data as dd

# Création histogramme de la fréquentation par ligne
def plot_histogram(data):
    fig = plt.figure(figsize=(10, 6))
    colors = ['red', 'green', 'blue', 'black'] 
    sns.barplot(data=data, x="Ligne", y="Total_Passagers", palette=colors)
    plt.xlabel("Ligne")
    plt.ylabel("Total des Passagers")
    plt.title("Histogramme des fréquentations par ligne")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Remplissage histogramme
def histogramme_frequentation():
    frequentations_par_ligne = dd.page_2_histogramme_frequentation()
    plot_histogram(frequentations_par_ligne)

# Création courbe de la fréquentation par heure
def plot_lineplot(data):
    fig = plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x="Horaire", y="Total_Passagers")
    plt.xlabel("Heure")
    plt.ylabel("Nombre de passagers")
    plt.title("Fréquentation par heure")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Remplissage histogramme
def frequentation_lineplot():

    frequentation_heures = dd.page_2_frequentation_lineplot()
    frequentation_heures["Horaire"] = frequentation_heures["Horaire"].astype(str)
    plot_lineplot(frequentation_heures)


# Création et remplissage camembert de la fréquentation par jour
def camembert_frequentation_jour():
    data_frame = dd.page_2_camembert_frequentation_jour() 
    # créer camembert
    sizes = data_frame['Total_Passagers']
    labels = data_frame['Jour']    
    fig, axe = plt.subplots(figsize=(6,5),dpi=80) 
    axe.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    axe.axis('equal')
    axe.set_title('Fréquentation par jour')
    st.pyplot(fig)    



def principal () :
    st.title("Page 2 Pour les employés")
    histogramme_frequentation ()
    frequentation_lineplot ()
    camembert_frequentation_jour()

principal()