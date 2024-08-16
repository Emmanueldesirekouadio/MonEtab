import datetime
from menu import Menu as m
from models.Utilisateur import Utilisateur as user
from exceptions.ChoixInvalide import ChoixInvalide

class Gestion_Utilisateurs():
# Lancement de l'application
    def connexion():
        while True:
            m.print_welcome_message()
            identifiant=input("Identifiant : ")
            motDePasse=input("Mot de passe : ")
            user.authentification(identifiant, motDePasse)
            if user.authentification(identifiant, motDePasse):
                break

            else:
                print("Connexion echouée.\nVeuillez réessayer\n\n")

    def menu_utilisateur():
        print(f"""\t******************************************************\n\n\t\t\tGESTION DES Utilisateurs\n\n\t******************************************************\n
    Menu :
        1: Ajouter un utilisateur\n
        2: Supprimer un utilisateur\n
        3: Modifier les informations de l'utilisateur\n
        4: Lister les utilisateurs\n
        5: Retour\n
        0: Accueil\n
    """)
        try:
            choice = m.get_whit_no_space("Entrez votre choix:")
            if choice == "1":
                Gestion_Utilisateurs.enregistrer_user()
            elif choice == "2":
                Gestion_Utilisateurs.delete_user()
            elif choice == "3":
                Gestion_Utilisateurs.edit_user()
            elif choice == "4":
                Gestion_Utilisateurs.lister_utilisateurs()
            elif choice == "5" or choice == "0":
                m.accueil()

            else:
                    raise ChoixInvalide()
        except ChoixInvalide as e:
                print(e)
                Gestion_Utilisateurs.menu_utilisateur()


    def enregistrer_user():

                print("Entrez les informations sur l'utilisateur\n")
                identifiant = input("Entrez l'identifiant : ")
                motDePasse = input("Entrez le mot de passe : ")
                dateCreation = datetime.datetime.now()
                user.ajouterCompte(identifiant, motDePasse,dateCreation)
                m.get_user_choice("1: Ajouter un nouveau utilisateur\n2: Revenir au menu précendent\nEntrez votre choix:",Gestion_Utilisateurs.enregistrer_user,Gestion_Utilisateurs.menu_utilisateur)

    def edit_user():
        identifiant = input("Entrez l'identifiant pour modifier le mot de passe : ")
        nouveauMotDePasse = input("Entrez le nouveau mot de passe : ")
        user.modifierMotDePasse(identifiant, nouveauMotDePasse)
        m.get_user_choice("1: Modifier un autre utilisateur\n2: Revenir au menu précendent\nEntrez votre choix:",Gestion_Utilisateurs.edit_user,Gestion_Utilisateurs.menu_utilisateur)


    def delete_user():
        identifiant = input("Entrez l'identifiant à supprimer : ")
        motDePasse = input("Entrez le mot de passe : ")
        user.supprimerCompte(identifiant, motDePasse)
        m.get_user_choice("1: Supprimer un autre utilisateur\n2: Revenir au menu précendent\nEntrez votre choix:",Gestion_Utilisateurs.delete_user,Gestion_Utilisateurs.menu_utilisateur)

    def lister_utilisateurs():
        utilisateurs = user.listerUtilisateur()
        if utilisateurs:
            print("Liste des utilisateurs :")
            for u in utilisateurs:
                print(f"- Identifiant : {u[0]}, Mot de passe : {u[1]}")
            Gestion_Utilisateurs.menu_utilisateur()
        else:
            print("Aucun utilisateur trouvé.")

