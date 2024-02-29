import pandas as pd
import mysql.connector as mysqlpy

class Dataclass:

    def __init__(self):
        pass

    def connection_mysql(self):
        user = "Breizhibus"
        password = "Breizhibus"
        host = "db"
        port = "3306"
        database = "Breizhibus"
        cnx = mysqlpy.connect(user=user, password=password, host=host, port=port, database=database)
        return cnx

    def sous_main (self) :
        query = "SELECT * FROM horaires"
        cnx = self.connection_mysql()
        horaires = pd.read_sql_query(query, con=cnx)
        return horaires

    def page_2_histogramme_frequentation(self):
        cnx = self.connection_mysql()
        query = """SELECT lignes.nom AS Ligne, SUM(frequentation.nombre_passagers) AS Total_Passagers
                FROM frequentation
                INNER JOIN horaires ON frequentation.horaire = horaires.id
                INNER JOIN lignes ON horaires.ligne = lignes.id
                GROUP BY lignes.nom;"""
        fl = pd.read_sql_query(query, con=cnx)
        return fl

    def page_2_frequentation_lineplot(self):
        cnx = self.connection_mysql()
        query = """
        SELECT horaires.heure AS Horaire, SUM(frequentation.nombre_passagers) AS Total_Passagers
        FROM frequentation
        INNER JOIN horaires ON frequentation.horaire = horaires.id
        GROUP BY horaires.heure;"""
        fl = pd.read_sql_query(query, con=cnx)
        return fl

    def page_2_camembert_frequentation_jour(self):
        cnx = self.connection_mysql()
        query = """
        SELECT frequentation.jour AS Jour, SUM(frequentation.nombre_passagers) AS Total_Passagers
        FROM frequentation
        GROUP BY frequentation.jour; """
        fl = pd.read_sql_query(query, con=cnx)
        return fl
    
    