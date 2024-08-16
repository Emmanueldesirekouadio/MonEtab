import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host='localhost', database='etab_db', user='root', password='09134506a'):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                database=database,
                user=user,
                password=password
            )
            if self.connection.is_connected():
                print("Connexion à la base de données réussie")
        except Error as e:
            print(f"Erreur de connexion : {e}")
            self.connection = None

    def execute_query(self, query, data=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, data)
            self.connection.commit()
        except Error as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")

    def fetch_query(self, query, data=None):
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, data)
            return cursor.fetchall()
        except Error as e:
            print(f"Erreur lors de la récupération des données : {e}")
            return []

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connexion fermée")
