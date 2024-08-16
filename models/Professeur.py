from Interfaces.ICRUDProfesseur import ICRUDProfesseur
from Interfaces.IEducation import IEducation
from models.Personne import Personne
from datetime import datetime
import mysql.connector
from mysql.connector import Error
#Classe Professeur
class Professeur(IEducation,ICRUDProfesseur,Personne):
    def __init__(self, id, dateNaissance, ville, prenom, nom,telephone, vacant,matiereEnseignee, prochainCours, sujetProchaineReunion):
        super().__init__(id, dateNaissance, ville, prenom, nom, telephone)
        self.__vacant = vacant
        self.__matiereEnseignee = matiereEnseignee
        self.__prochainCours = prochainCours
        self.__sujetProchaineReunion = sujetProchaineReunion

    def __str__(self):
        return f"""[ID: {self.get_id()}, NOM: {self.get_nom()}, PRENOMS: {self.get_prenom()}, DATE DE NAISSANCE: {self.get_dateNaissance()}, VILLE: {self.get_ville()}]
        """


    # Getter et Setter pour la classe

    def get_vacant(self):
        return self.__vacant

    def get_matiereEnseignee(self):
        return self.__matiereEnseignee

    def get_prochainCours(self):
        return self.__prochainCours

    def get_sujetProchaineReunion(self):
        return self.__sujetProchaineReunion

    def set_vacant(self, vacant):
        self.__vacant = vacant

    def set_matiereEnseignee(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def set__prochainCours(self, prochainCours):
        self.__prochainCours = prochainCours

    def set_sujetProchaineReunion(self, sujetProchaineReunion):
        self.__sujetProchaineReunion = sujetProchaineReunion


    # Méthodes
    #Méthode ajouter
    @staticmethod
    def ajouter(professeur):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )

            if connection.is_connected():
                cursor = connection.cursor()

                cursor.execute("INSERT INTO professeurs (date_naissance, ville, prenom, nom, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (professeur.get_dateNaissance(), professeur.get_ville(), professeur.get_prenom(), professeur.get_nom(), professeur.get_telephone(),professeur.get_vacant(), professeur.get_matiereEnseignee(), professeur.get_prochainCours(), professeur.get_sujetProchaineReunion()))
                connection.commit()
                print(f"Professeur {professeur.get_prenom()} {professeur.get_nom()} ajouté avec succès.")

        except Error as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    #Méthode modifier
    def modifier(professeur):
        from Services.Gestions_professeurs import Gestions_professeurs as gest_prof
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )

            if connection.is_connected():
                cursor = connection.cursor()

                query = """
                UPDATE professeurs
                SET date_naissance = %s, ville = %s, prenom = %s, nom = %s, telephone = %s, vacant = %s, matiere_enseigne = %s, prochain_cours= %s,  sujet_prochaine_reunion= %s
                WHERE id = %s
                """
                cursor.execute(query,
                        (professeur['date_naissance'], professeur['ville'], professeur['prenom'], professeur['nom'], professeur['telephone'],professeur['vacant'], professeur['matiere_enseigne'], professeur['prochain_cours'], professeur['sujet_prochaine_reunion'], professeur['id']))
                connection.commit()

                print(f"Élève {professeur['prenom']} {professeur['nom']} modifié avec succès.")
                gest_prof.edit_choice(professeur)

        except Error as e:
            print(f"Erreur lors de la modification du professeur : {e}")


        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    #Méthode lister
    @staticmethod
    def ObtenirProfesseur():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )

            if connection.is_connected():
                cursor = connection.cursor()
                query = " SELECT * FROM professeurs"
                cursor.execute(query)
                profs = cursor.fetchall()

                if not profs:
                    return None

            return profs
        except Error as e:
            print(f"Error: {e}")
            return False

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    #Méthode supprimer
    @staticmethod
    def supprimer(id):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )

            if connection.is_connected():
                cursor = connection.cursor()
                connection.start_transaction()

                query = "DELETE FROM professeurs WHERE id = %s"
                cursor.execute(query, (id,))
                connection.commit()
                if cursor.rowcount > 0:
                    print(f"Professeur avec ID {id} supprimés.")
                else:
                    print(f"Aucun professeur avec ID {id} n'a été")

        except Error as e:
            print(f"Error: {e}")


        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    #Méthode obtenir
    @staticmethod
    def obtenir(identifiant):
        from Services.Gestions_professeurs import Gestions_professeurs as gest_prof
        from menu import Menu as m
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='root',
                password=''
            )

            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                get_eleve_query = "SELECT id, nom, prenom, date_naissance, ville, telephone, vacant, matiere_enseigne, prochain_cours, sujet_prochaine_reunion FROM professeurs WHERE id = %s"
                cursor.execute(get_eleve_query, (identifiant,))
                prof = cursor.fetchone()
                if prof:
                    return prof
                else:
                    print(f"Il y a 0 professeur avec ID {identifiant}")
                    m.get_user_choice("1. Réessayer\n2. Menu précédent\nEntrez votre choix:",gest_prof.edit_prof,gest_prof.menu_professeur)
        except Error as e:
            print(f"Error: {e}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    #Méthode enseigner
    @staticmethod
    def enseigner(self, matiere):
        return f"Enseigne la matière {matiere}"

    #Méthode preparerCours
    @staticmethod
    def preparerCours(self, prochainCours):
        return f"Prépare le contenu d'un cours sur le sujet {prochainCours}"

    #Méthode assisterReunion
    @staticmethod
    def assisterReunion(self, sujetProchaineReunion):
        return f"Doit assister à une reunion sur {sujetProchaineReunion}"