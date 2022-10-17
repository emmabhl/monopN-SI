couleur_cout = {"marron" : [60,40,100,500], "bleu" : [100,80,100,500], "rose" : [140,120,150,700], "orange" : [180,160,150,700], "rouge" : [220,200,200,700], "jaune" : [260,240,200,900], "vert" : [300,280,300,950], "violet" : [350,330,350,1000]}

class Terrain:

    def __init__(self, nom, couleur):
        """
            Constructeur de Terrain
            à compléter
        """
        self.nom = nom
        self.couleur = couleur
        self.nombre_maisons = 0
        self.nombre_hotels = 0
        self.proprietaire = ""
        self.cout_achat = couleur_cout[couleur][0]
        self.loyer = couleur_cout[couleur][1]
        self.cout_maison = couleur_cout[couleur][2]
        self.cout_hotel = couleur_cout[couleur][3]


    def est_achetable(self):
        """
            Renvoie vrai si le terrain est achetable
        """
        return self.proprietaire == ""

    def ameliorer_terrain(self, joueur):
        """
            Améliore le terrain sur lequel le joueur joueur est
        """
        if self.nombre_maisons < 4 :
            if joueur.compte >= self.cout_maison :
                achat = input("Voulez-vous l acheter (1/0) ?")
                if achat == 1 :
                    self.nombre_maisons += 1
                    joueur.self.compte -= self.cout_maison  #################
                    print(joueur.nom + " a acheté une maison")
                else : pass
            else : 
                print("Vous n'avez pas suffisamment d'argent")
        elif self.nombre_hotels == 0 :
            if joueur.compte >= self.cout_hotel :
                achat = input("Voulez-vous l acheter (1/0) ?")
                if achat == 1 :
                    self.nombre_hotels += 1
                    joueur.self.compte -= self.cout_hotel #####################
                    print(joueur.nom + " a acheté un hotel")
                else : pass
            else : 
                print("Vous n'avez pas suffisamment d'argent")
        else : print("Vous ne pouvez plus ameliorer le terrain")
        