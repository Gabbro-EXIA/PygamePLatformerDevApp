import pygame
from pygame.locals import *

# création d'une fenêtre d'affichage pour le jeu

FENETRE = pygame.display.set_mode(1280, 720) # Résolution HD, suffisant pour tester la calsse joueur
FENETRE.fill([255, 0, 0]) # On remplit la fenêtre de jeu de rouge
