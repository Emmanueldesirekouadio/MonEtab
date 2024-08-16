import mysql.connector
from mysql.connector import Error
from datetime import datetime

class Utilisateur:
    def __init__(self, pseudo, motDePasse, dateCreation):
        self.__id = None  # Assigner plus tard lors de l'insertion en DB
        self.__pseudo = pseudo
        self.__motDePasse = motDePasse
        self.__dateCreation = dateCreation

    def __str__(self) -> str:
        return f"[Identifiant:{self.get_pseudo()} | Mot de passe:{self.get_motDePasse()}]"

    def get_id(self):
        return self.__id

    def get_pseudo(self):
        return self.__pseudo

    def get_motDePasse(self):
        return self.__motDePasse

    def get_dateCreation(self):
        return self.__dateCreation

    def set_id(self, id):
        self.__id = id

    def set_pseudo(self, pseudo):
        self.__pseudo = pseudo

    def set_motDePasse(self, motDePasse):
        self.__motDePasse = motDePasse

    def set_dateCreation(self, dateCreation):
        self.__dateCreation = dateCreation

    @staticmethod
    def get_database_connection():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password='09134506a'  # Assurez-vous que ce mot de passe est correct
            )
            return connection
        except Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            return None

    @staticmethod
    def authentification(pseudo, motDePasse):
        connection = None
        try:
            connection = Utilisateur.get_database_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT pseudo, mot_de_passe FROM utilisateurs WHERE pseudo = %s AND mot_de_passe = %s"
                cursor.execute(query, (pseudo, motDePasse))
                result = cursor.fetchone()
                return result is not None
        except Error as e:
            print(f"Erreur lors de l'authentification : {e}")
            return False
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def ajouter_compte(pseudo, motDePasse, creationDate):
        connection = None
        try:
            connection = Utilisateur.get_database_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM utilisateurs WHERE pseudo = %s", (pseudo,))
                if cursor.fetchone():
                    print("Identifiant déjà utilisé.\nVeuillez en choisir un autre.")
                    return

                cursor.execute("INSERT INTO utilisateurs (pseudo, mot_de_passe, date_creation) VALUES (%s, %s, %s)",
                               (pseudo, motDePasse, creationDate))
                connection.commit()
                print(f"Utilisateur {pseudo} ajouté avec succès.")
        except Error as e:
            print(f"Erreur lors de l'ajout du compte : {e}")
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def modifierMotDePasse(pseudo, motDePasse):
        connection = None
        try:
            connection = Utilisateur.get_database_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM utilisateurs WHERE pseudo = %s", (pseudo,))
                user = cursor.fetchone()

                if user:
                    cursor.execute("UPDATE utilisateurs SET mot_de_passe = %s WHERE pseudo = %s",
                                   (motDePasse, pseudo))
                    connection.commit()
                    print("Mot de passe modifié avec succès.")
                else:
                    print("Utilisateur non trouvé.")
        except Error as e:
            print(f"Erreur lors de la modification du mot de passe : {e}")
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def supprimerCompte(pseudo, motDePasse):
        connection = None
        try:
            connection = Utilisateur.get_database_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM utilisateurs WHERE pseudo = %s AND mot_de_passe = %s",
                               (pseudo, motDePasse))
                user = cursor.fetchone()

                if user:
                    cursor.execute("DELETE FROM utilisateurs WHERE pseudo = %s", (pseudo,))
                    connection.commit()
                    print(f"Utilisateur {pseudo} supprimé avec succès.")
                else:
                    print("Identifiant ou mot de passe incorrect.")
        except Error as e:
            print(f"Erreur lors de la suppression du compte : {e}")
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def listerUtilisateur():
        connection = None
        try:
            connection = Utilisateur.get_database_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT pseudo, mot_de_passe FROM utilisateurs"
                cursor.execute(query)
                utilisateurs = cursor.fetchall()

                if not utilisateurs:
                    return "Il n'y a pas d'utilisateur."

                return utilisateurs
        except Error as e:
            print(f"Erreur lors de la liste des utilisateurs : {e}")
            return False
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def initialize_default_user_sql():
        default_username = "admin"
        default_password = "admin"
        default_dateCreation = datetime.now()

        connection = None
        try:
            connection = Utilisateur.get_database_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM utilisateurs WHERE pseudo = %s", (default_username,))
                if not cursor.fetchone():
                    cursor.execute("INSERT INTO utilisateurs (pseudo, mot_de_passe, date_creation) VALUES (%s, %s, %s)",
                                   (default_username, default_password, default_dateCreation))
                    connection.commit()
                    print("Utilisateur par défaut créé.")
                else:
                    print("L'utilisateur par défaut existe déjà.")
        except Error as e:
            print(f"Erreur lors de l'initialisation de l'utilisateur par défaut : {e}")
        finally:
            if connection and connection.is_connected():
                cursor.close()
                connection.close()
