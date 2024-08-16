from models.Personne import Personne
import mysql.connector
from mysql.connector import Error
from Interfaces.ICRUDEleve import ICRudEleve

class Eleve(Personne, ICRudEleve):

    def __init__(self, id, dateNaissance, ville, prenom, nom, telephone, classe, matricule):
        super().__init__(id, dateNaissance, ville, prenom, nom, telephone)
        self.__classe = classe
        self.__matricule = matricule

    def __str__(self):
        return (f"[ID: {self.get_id()}, MATRICULE: {self.get_matricule()}, NOM: {self.get_nom()}, "
                f"PRENOMS: {self.get_prenom()}, DATE DE NAISSANCE: {self.get_dateNaissance()}, "
                f"VILLE: {self.get_ville()}, CLASSE: {self.get_classe()}]")

    # Getter et Setter pour la classe
    def get_classe(self):
        return self.__classe

    def set_classe(self, classe):
        self.__classe = classe

    def get_matricule(self):
        return self.__matricule

    def set_matricule(self, matricule):
        self.__matricule = matricule

    # Méthodes
    # Méthode ajouter
    @staticmethod
    def ajouter(eleve):
        connection = None
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password='09134506a'
            )

            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO eleves (date_naissance, ville, prenom, nom, telephone, classe, matricule) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (eleve.get_dateNaissance(), eleve.get_ville(), eleve.get_prenom(), eleve.get_nom(),
                     eleve.get_telephone(), eleve.get_classe(), eleve.get_matricule())
                )
                connection.commit()
                print(f"Élève {eleve.get_prenom()} {eleve.get_nom()} ajouté avec succès.")

        except Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")

        finally:
            if connection is not None and connection.is_connected():
                cursor.close()
                connection.close()

    # Méthode modifier
    @staticmethod
    def modifier(eleve):
        from Services.Gestions_eleves import Gestions_eleves as gest_eleve
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password='09134506a'
            )

            if connection.is_connected():
                cursor = connection.cursor()
                update_personne_query = """
                UPDATE eleves
                SET date_naissance = %s, ville = %s, prenom = %s, nom = %s, telephone = %s, classe = %s, matricule = %s
                WHERE id = %s
                """
                cursor.execute(update_personne_query,
                               (eleve['date_naissance'], eleve['ville'], eleve['prenom'], eleve['nom'],
                                eleve['telephone'], eleve['classe'], eleve['matricule'], eleve['id']))
                connection.commit()
                print(f"Élève {eleve['prenom']} {eleve['nom']} modifié avec succès.")
                gest_eleve.edit_choice(eleve)

        except Error as e:
            print(f"Erreur lors de la modification de l'élève : {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # Méthode lister
    @staticmethod
    def ObtenirEleve():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password='09134506a'
            )

            if connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT * FROM eleves"
                cursor.execute(query)
                eleves = cursor.fetchall()

                if not eleves:
                    return None
                return eleves
        except Error as e:
            print(f"Error: {e}")
            return False

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # Méthode supprimer
    @staticmethod
    def supprimer(id):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password='09134506a'
            )

            if connection.is_connected():
                cursor = connection.cursor()
                query = "DELETE FROM eleves WHERE id = %s"
                cursor.execute(query, (id,))
                if cursor.rowcount > 0:
                    print(f"Élève avec ID {id} supprimé.")
                else:
                    print(f"Aucun élève avec ID {id} n'a été trouvé")
                connection.commit()

        except Error as e:
            print(f"Error: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # Méthode obtenir
    @staticmethod
    def obtenir(identifiant):
        from Services.Gestions_eleves import Gestions_eleves as gest_eleve
        from menu import Menu as m
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password='09134506a'
            )

            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM eleves WHERE id = %s"
                cursor.execute(query, (identifiant,))
                eleve = cursor.fetchone()

                if eleve:
                    return eleve
                else:
                    print(f"Il y a 0 élève avec ID {identifiant}")
                    return m.get_user_choice(
                        "1. Réessayer\n2. Menu précédent\nEntrez votre choix:",
                        gest_eleve.edit_eleve,
                        gest_eleve.menu_eleve
                    )
        except Error as e:
            print(f"Error: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
