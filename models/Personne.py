#classe Personne
class Personne:
    def __init__(self,id,dateNaissance,ville,prenom,nom,telephone):
        self.__id = id
        self.__dateNaissance = dateNaissance
        self.__ville = ville
        self.__prenom = prenom
        self.__nom = nom
        self.__telephone = telephone


    #Getters
    def get_id(self):
        return self.__id

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_telephone(self):
        return self.__telephone

    def get_dateNaissance(self):
        return self.__dateNaissance

    def get_ville(self):
        return self.__ville

    #Setters

    def set_id(self, id):
        self.__id = id

    def set_nom(self, nom):
        self.__nom = nom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def set_telephone(self,telephone):
        self.__telephone = telephone

    def set_dateNaissance(self, dateNaissance):
        self.__dateNaissance = dateNaissance

    def set_ville(self, ville):
        self.__ville = ville

    #Methode obtenirAge
    def obtenirAge(age):
        pass

