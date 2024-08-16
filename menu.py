import datetime
from exceptions.ChoixInvalide import ChoixInvalide
heure = datetime.datetime.now().strftime("%H:%M")


class Menu():
    # Fontion message de bienvenue
    def print_welcome_message():
        print(f"\t ****************************************************** \n\n\t\tBIENVENU DANS L’APPLICATION ETAB v1.3\n\n\t ******************************************************\n")

    #Fonctions Menu Principal
    def print_menu():
        print(f"""MENU:\n
        1: Gestion des élèves\n
        2: Gestion des professeurs\n
        3: Gestion des utilisateurs\n
        0: Quitter\n
    Date système :{heure}\n""")

    #fonction page d'accueil
    def accueil():
        Menu.print_welcome_message()
        Menu.print_menu()

    #fonction pour recuprer le choix sans espace
    def get_whit_no_space(prompt):
        choix = input(prompt)
        return "".join(choix.split())

    #fonction pour retourner un message d'erreur
    def erreur():
        print("Choix invalide, veuillez réessayer.")

    #fonction pour recuperer le choix de l'utilisateur et le traiter
    def get_user_choice(text,function1,function2):
        try:
                choix = Menu.get_whit_no_space(text)

                if choix == "1":
                    function1()
                elif choix == "2":
                    function2()
                else:
                    raise ChoixInvalide()

        except ChoixInvalide as e:
                print(e)
                Menu.get_user_choice(text,function1,function2)

