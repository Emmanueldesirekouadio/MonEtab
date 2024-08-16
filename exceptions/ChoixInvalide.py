class ChoixInvalide(Exception):
    def __init__(self, message="Choix invalide, veuillez réessayer."):
        self.message = message
        super().__init__(self.message)