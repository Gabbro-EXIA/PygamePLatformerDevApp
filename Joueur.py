import pygame, sys
from pygame.locals import *

# création d'une fenêtre d'affichage pour le jeu

pygame.init() #initialisation

pygame.key.set_repeat(100) # en ms

FENETRE = pygame.display.set_mode((1280, 720)) # Résolution HD, suffisant pour tester la classe joueur
FENETRE.fill([255, 0, 0]) # On remplit la fenêtre de jeu de rouge

class Joueur:
    def __init__(self, image:str)->None:
        """Création d'un nouveau Joueur et initialisation des variables"""
        # self.image = pygame.image.load(image).convert()
        # self.image = pygame.transform.smoothscale_by(self.image, 1)
        # On dessine un rectangle pour l'instant mais on pourra charger des images plus tard
        self.image = pygame.draw.rect(FENETRE, [0, 255, 0], pygame.Rect(0, 710, 10, 10)) # valeurs arbitraires
        self.position = self.image
    def __deplacement__(self)->None:
        """Gére les déplacements du Joueur :\n
        - q ou ← (flèche gauche) pour se déplacer à gauche\n
        - d ou → (flèche droite) pour se déplacer à droite\n
        - espace ou ↑ (flèche du haut) pour sauter"""
        touche = pygame.key.get_pressed()

        if touche[K_q] or touche[K_LEFT]:
            self.position.left -= 1
        elif touche[K_d] or touche[K_RIGHT]:
            self.position.left += 1
        elif touche[K_SPACE] or touche[K_UP]:
            self.position.top -= 1
        FENETRE.fill([255, 0, 0])
        self.image = pygame.draw.rect(FENETRE, [0, 255, 0], self.position)
        #FENETRE.blit(self.image, self.position) pour l'image


Test = Joueur("test")

#On teste la classe Joueur dans la boucle de jeu

while True:
    pygame.display.flip() # on affiche notre perso
    for events in pygame.event.get():
        if events.type == QUIT: #si l'utilisateur clique sur la croix pour fermer la fenêtre, on ferme le jeu
            sys.exit()
        elif events.type == KEYDOWN:
            Test.__deplacement__()