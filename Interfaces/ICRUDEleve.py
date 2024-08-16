from abc import ABC,abstractmethod
class ICRudEleve(ABC):

    #Interface ajouter
    @abstractmethod
    def ajouter(self, eleve):
        pass

    #Interface modifier
    @abstractmethod
    def modifier(self, eleve):
        pass

    #Interface supprimer
    @abstractmethod
    def supprimer(self, identifiant):
        pass

    #Interface obtenir
    @abstractmethod
    def obtenir(self, identifiant):
        pass

    #Interface lister
    @abstractmethod
    def ObtenirEleve(self):
        pass