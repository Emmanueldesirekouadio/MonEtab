from menu import Menu as m
from models.Professeur import Professeur
from datetime import datetime
from exceptions.ChoixInvalide import ChoixInvalide

class Gestions_professeurs():
#Fonctions Menu PROFESSEURS
    def menu_professeur():
        print(f"""\t******************************************************\n\n\t\t\tGESTION DES PROFESSEURS\n\n\t******************************************************\n
    Menu :
        1: Ajouter un professeur\n
        2: Supprimer un professeur\n
        3: Modifier les informations du professeur\n
        4: Lister les professeurs\n
        5: Retour\n
        0: Accueil\n
    """)
        try:
            choice = m.get_whit_no_space("Entrez votre choix:")
            if choice == "1":
                Gestions_professeurs.enregistrer_prof()
            elif choice == "2":
                Gestions_professeurs.delete_prof()
            elif choice == "3":
                Gestions_professeurs.edit_prof()
            elif choice == "4":
                Gestions_professeurs.lister_prof()
            elif choice == "5" or choice == "0":
                m.accueil()
            else:
                    raise ChoixInvalide()
        except ChoixInvalide as e:
                print(e)
                Gestions_professeurs.menu_professeur()


    def enregistrer_prof():
        nom = input("Entrez le nom du professeur : ")
        prenom = input("Entrez le prénom du professeur : ")
        while True:
            try:
                dateNaissance_str = m.get_whit_no_space("Date de Naissance (format JJ-MM-AAAA): ")
                dateNaissance = datetime.strptime(dateNaissance_str, "%d-%m-%Y").date()
                break
            except ValueError:
                print("Erreur : Format de date invalide. Veuillez entrer la date au format JJ-MM-AAAA.")
        ville = input("Entrez la ville : ")
        while True:
            telephone = input("Entrez le numéro de téléphone : ")
            if telephone.isdigit():
                break
            else:
                print("le numéro doit être numérique")
        while True:
            vacant = input("Vancant? Entrez 0 ou 1 : ")
            if vacant in ["0","1"]:
                break
            else: print("vacant doit être 0(non) ou 1(oui)")
        matiere = input("Entrez la matiere : ")
        cours = input("Entrez le prochain cours : ")
        sujet = input("Entrez le sujet de la reunion : ")
        prof = Professeur(id,dateNaissance,ville,prenom,nom,telephone,vacant,matiere,cours,sujet)
        Professeur.ajouter(prof)
        m.get_user_choice("1: Ajouter un nouveau prof\n2: Revenir au menu précendent\nEntrez votre choix:",Gestions_professeurs.enregistrer_prof,Gestions_professeurs.menu_professeur)

    def delete_prof():
        if Professeur.ObtenirProfesseur():
            while True:
                id= input("Entrez l'id du professeur à supprimer:")
                if id.isdigit():
                    break
                else: print("l'id doit être un entier")
            Professeur.supprimer(id)
            m.get_user_choice("1: Supprimer un autre professeur\n2: Revenir au menu précendent\nEntrez votre choix:",Gestions_professeurs.delete_prof,Gestions_professeurs.menu_professeur)
        else:
            print("Aucun professeur enregistré")
            Gestions_professeurs.menu_professeur()


    def edit_prof():
        profs = Professeur.ObtenirProfesseur()
        if profs is not None:
            try:
                id = int(input("Entrez l'id du professeur à modifier: "))
            except:
                print("Le id doit être un entier")
                Gestions_professeurs.edit_prof()
            prof = next((prof for prof in Professeur.professeurs if prof.get_id() == id), None)
            print(prof)
            if prof:
                Professeur.modifier(prof)
            else:
                print("ID incorrect")
                Gestions_professeurs.edit_prof()
        else:
            print("Aucun professeur enregistré")
            Gestions_professeurs.menu_professeur()

    def lister_prof():
        profs = Professeur.ObtenirProfesseur()
        if profs is not None:
            print("Liste des professeurs :")
            for p in profs:
                print(f"ID: {p[0]}, Nom : {p[4]}, Prénom : {p[3]}, Ville : {p[2]}, Date de Naissance : {p[1]}, "
                    f"Téléphone : {p[5]}, Matière enseigné : {p[7]}")
            Gestions_professeurs.menu_professeur()
        else:
            print("Aucun professeur trouvé.")
            Gestions_professeurs.menu_professeur()


    def edit_prof():
        try:
            id = int(input("Entrez l'id du professeur à modifier: "))
        except ValueError:
            print("l'id doit être un entier")
            Gestions_professeurs.edit_prof()
        prof=Professeur.obtenir(id)
        print(prof)
        if prof :
            Gestions_professeurs.edit_choice(prof)
        else:
            Gestions_professeurs.menu_professeur()

    def edit_choice(prof):
        try:
                print("1. Modifier le nom\n2. Modifier le prénom\n3. Modifier la date de Naissance\n4. Modifier la ville\n5. Modifier la statut(vacant)\n6. Modifier le numéro de téléphone\n7. Modifier la matiere\n8. Modifier le prochain cours\n9. Modifier le sujet de la reunion\n10. Retour\n0. Accueil")
                choice = m.get_whit_no_space("Entrez votre choix:")
                if choice == "1":
                    nom=input("Entrez le nom: ")
                    prof['nom'] = nom
                    Professeur.modifier(prof)
                elif choice == "2":
                    prenom=input("Entrez le prenom: ")
                    prof['prenom'] = prenom
                    Professeur.modifier(prof)
                elif choice == "3":
                    while True:
                        try:
                            dateNaissance_str = m.get_whit_no_space("Date de Naissance (format JJ-MM-AAAA): ")
                            dateNaissance = datetime.strptime(dateNaissance_str, "%d-%m-%Y").date()
                            if dateNaissance:
                                prof['date_naissance'] = dateNaissance
                                Professeur.modifier(prof)
                        except ValueError:
                            print("Erreur : Format de date invalide. Veuillez entrer la date au format JJ-MM-AAAA.")
                elif choice == "4":
                    ville=input("Entrez la ville: ")
                    prof['ville'] = ville
                    Professeur.modifier(prof)
                elif choice == "5":
                    if prof['vacant'] == True:
                        prof['vacant'] = False
                        Professeur.modifier(prof)
                    else:
                        prof['vacant'] = True
                        Professeur.modifier(prof)
                elif choice == "6":
                    while True:
                        tel=input("Entrez le nuémro: ")
                        if tel.isdigit():
                            prof['telephone'] = tel
                            Professeur.modifier(prof)
                            break
                        else:
                            print("le numéro doit être numérique")
                elif choice == "7":
                    matiere=input("Entrez le matière: ")
                    prof['matiere_enseigne']=matiere
                    Professeur.modifier(prof)
                elif choice == "8":
                    prochain_cours=input("Entrez le prochain cours: ")
                    prof['prochain_cours'] = prochain_cours
                    Professeur.modifier(prof)
                elif choice == "9":
                    sujet_prochaine_reunion=input("Entrez le sujet de la prochaine reunion: ")
                    prof['sujet_prochaine_reunion'] = sujet_prochaine_reunion
                    Professeur.modifier(prof)
                elif choice == "10":
                    Gestions_professeurs.menu_professeur()
                elif choice == "0":
                    m.accueil()
                    return
                else:
                    raise ChoixInvalide()
        except ChoixInvalide as e:
                print(e)
                Gestions_professeurs.edit_choice(prof)