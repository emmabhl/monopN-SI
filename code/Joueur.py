from random import randint

class Joueur:

    def __init__(self, nom):
        """
            Constructeur de Joueur
        """
        self.nom = nom
        self.position = [0,0]
        self.compte = 1500
        self.propriétés = []

    def tirer_de(self):
        """
            Renvoie la valeur du dé
        """
        return randint(1,6)

    def deplacement(self, nb_cases):
        """
            Déplace le joueur de nb_cases
        """
        self.position[1] = (self.position[1] + nb_cases) % 7
        self.position[0] = ((self.position[1] + nb_cases) // 7 + self.position[0]) % 4

    def acheter(self, terrain):
        """
            Le joueur achete le terrain terrain
        """
        self.compte -= terrain.cout_achat
        self.propriétés.append(terrain)
        terrain.propriétaire


    def payer(self, terrain, autre_joueur):
        """
            Le joueur paye le loyer du terrain terrain à autre_joueur
        """
        ######################
        self.compte -= terrain.loyer
        autre_joueur.compte += terrain.loyer
        ######################
    
    def paye_amelioration(self, somme) : 
        self.compte -= somme