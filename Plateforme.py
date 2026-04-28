import pygame, sys
from pygame.locals import *

# création d'une fenêtre d'affichage pour le jeu

pygame.init() #initialisation


FENETRE = pygame.display.set_mode((1280, 720))

class Plateforme(pygame.sprite.Sprite) :
    def __init__(self,x,y,image_path):
        super().__init__()
       # self.rect = rect #utilisation avec un rectangle 
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 40))
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def afficher(self, surface):
        pygame.draw.rect(surface,(0,255,0),self.rect)

#plateformes = [Plateforme(pygame.Rect(200, 500, 300, 20)),Plateforme(pygame.Rect(600, 400, 200, 20)),Plateforme(pygame.Rect(100, 300, 150, 20))]
plateformes = pygame.sprite.Group()
plateformes.add(Plateforme(200, 500,"plateforme.png"))
plateformes.add(Plateforme(600, 400,"plateforme.png"))

while True:
    FENETRE.fill([255, 0, 0]) # On remplit la fenêtre de jeu de rouge
    for plateforme in plateformes : 
        plateforme.afficher(FENETRE)

    pygame.display.flip() # on affiche notre perso
    for events in pygame.event.get():
        if events.type == QUIT: #si l'utilisateur clique sur la croix pour fermer la fenêtre, on ferme le jeu
            pygame.quit()
            sys.exit()


