import pygame, sys
from pygame.locals import *

# création d'une fenêtre d'affichage pour le jeu

pygame.init() #initialisation

#pygame.key.set_repeat(10) # en ms | 10 fluide

FPS = pygame.time.Clock()

FENETRE = pygame.display.set_mode((1280, 720)) # Résolution HD, suffisant pour tester la classe joueur

class Joueur(pygame.sprite.Sprite):
    def __init__(self, image : str = "neutre_D")->None:
        """Création d'un nouveau Joueur et initialisation des variables"""
        super().__init__() # On fait de notre Joueur un objet utilisable par la classe Sprite
        self.etat = ["neutre_D", "neutre_G", "saut_D", "saut_G", "mouv_D", "mouv_G"]
        self.etat = {k : f"./Perso/{k}.png" for k in self.etat}
        self.source = image
        self.image = pygame.image.load(self.etat[image]).convert_alpha()
        self.image = pygame.transform.smoothscale_by(self.image, 1) # 1 = taille de base
        self.position = self.image.get_rect()
        self.position.bottomleft = (0, 720) # On place notre perso en bas à gauche

    def deplacement(self)->None:
        """Gére les déplacements du Joueur :\n
        - q ou ← (flèche gauche) pour se déplacer à gauche\n
        - d ou → (flèche droite) pour se déplacer à droite\n
        - espace ou ↑ (flèche du haut) pour sauter"""
        touche = pygame.key.get_pressed()

        if touche[K_q] or touche[K_LEFT]:
            if touche[K_SPACE] or touche[K_UP]:
                self.position.top -= 1 # permet de sauter et de se déplacer vers la gauche
                self.maj("saut_G")
            else:
                self.maj("mouv_G")
            self.position.left -= 1
        elif touche[K_d] or touche[K_RIGHT]:
            if touche[K_SPACE] or touche[K_UP]:
                self.position.top -= 1 # permet de sauter et de se déplacer vers la droite
                self.maj("saut_D")
            else:
                self.maj("mouv_D")
            self.position.left += 1 
        elif touche[K_SPACE] or touche[K_UP]:
            self.maj("saut_G") if self.source[-1] == "G" else self.maj("saut_D")
            self.position.top -= 1
        else:
            self.maj("neutre_G") if self.source[-1] == "G" else self.maj("neutre_D")
    
    def maj(self, image : str)->None:
        """Met à jour l'image du Joueur (pendant le déplacement ou pas)"""
        self.image = pygame.image.load(self.etat[image]).convert_alpha()
        self.source = image

    def tomber(self)->None:
        """Gère le système de gravité pour le Joueur"""
        #if pygame.sprite.spritecollide(self, plateforme): A utiliser avec les objets de la classe Plateforme
            # while self.position.bottom != 720:
            #     self.position.top += 1


# Tab_Test = ["neutre_D", "neutre_G", "saut_D", "saut_G", "mouv_D", "mouv_G"] # Nom des images
# l = [f"./Perso/{k}.png" for k in Tab_Test]
# Tab_Sprite = [Joueur(perso) for perso in l] # Un joueur différent par image
# for i in range(len(Tab_Sprite)-1):
#     Tab_Sprite[i+1].position.left = Tab_Sprite[i].position.right # Pour vérifier la taille
Test = Joueur()

#On teste la classe Joueur dans la boucle de jeu

while True:
    FENETRE.fill([255, 0, 0]) # On remplit la fenêtre de jeu de rouge
    FENETRE.blit(Test.image, Test.position)
    # for elt in Tab_Sprite:
    #     FENETRE.blit(elt.image, elt.position)
    pygame.display.flip() # on affiche notre perso
    for events in pygame.event.get():
        if events.type == QUIT: #si l'utilisateur clique sur la croix pour fermer la fenêtre, on ferme le jeu
            sys.exit()
        # elif events.type == KEYDOWN:
    Test.deplacement()
    FPS.tick(60) # Gère la vitesse à laquelle se déplace le perso 