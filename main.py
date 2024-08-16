
import time
from menu import Menu as m
from Services.Gestions_eleves import Gestions_eleves as gest_eleve
from Services.Gestions_professeurs import Gestions_professeurs as gest_prof
from Services.Gestions_Utilisateurs import Gestion_Utilisateurs as gest_user
from models.Utilisateur import Utilisateur as u
class Etab():

    def main(self):
        # Lancement de l'application
        start_time = time.time()
        u.initialize_default_user_sql()
        gest_user.connexion()
        m.accueil()

        # Boucle principale
        while True:
            choice = m.get_whit_no_space("Entrez votre choix: ")
            if choice == "1":
                gest_eleve.menu_eleve()
            elif choice == "2":
                gest_prof.menu_professeur()
            elif choice == "3":
                gest_user.menu_utilisateur()
            elif choice == "0":
                end_time = time.time()
                duration = end_time - start_time
                print(f"Merci d'avoir utilisé l'application ETAB. Au revoir!\n Temps de session:  {duration:.1f} s")
                break
            else:
                m.erreur()
                m.accueil()


if __name__ == "__main__":
    app=Etab()
    app.main()