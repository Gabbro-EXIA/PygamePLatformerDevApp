import pygame, sys
from pygame.locals import *

# création d'une fenêtre d'affichage pour le jeu

FENETRE = pygame.display.set_mode((1280, 720)) # Résolution HD, suffisant pour tester la calsse joueur
FENETRE.fill([255, 0, 0]) # On remplit la fenêtre de jeu de rouge

class Joueur:
    def __init__(self, image:str)->None:
        """Création d'un nouveau Joueur et initialisation des variables"""
        # self.image = pygame.image.load(image).convert()
        # self.image = pygame.transform.smoothscale_by(self.image, 1)
        # On dessine un rectangle pour l'instant mais on pourra charger des images plus tard
        self.image = pygame.draw.rect(FENETRE, [0, 255, 0], pygame.Rect(0, 710, 10, 10)) # valeurs arbitraires
        self.position = self.image

Test = Joueur("test")

#On teste la classe Joueur dans la boucle de jeu

while True:
    pygame.display.flip() # on affiche notre perso
    for events in pygame.event.get():
        if events.type == QUIT: #si l'utilisateur clique sur la croix pour fermer la fenêtre, on ferme le jeu
            sys.exit()