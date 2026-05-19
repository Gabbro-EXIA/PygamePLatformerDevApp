import sys

import pygame
from pygame.locals import *

from Joueur import *

LARGEUR = 1280
HAUTEUR = 720

class fenetre:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Astronaut Rescuer')
        self.screen = pygame.display.set_mode((LARGEUR, HAUTEUR))

        self.clock = pygame.time.Clock()
    

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
#création de la fenetre
            
            pygame.display.update()
            self.clock.tick(60)




class menu:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Astronaut Rescuer')
        self.screen = pygame.display.set_mode((LARGEUR, HAUTEUR))

        

        self.clock = pygame.time.Clock()
    

    def run(self):
        
        son = pygame.mixer.Sound("./Son/idoberg-deep-space-loop-401165.mp3")
        son.play(-1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
#création de la fenetre
            
            pygame.display.update()
            self.clock.tick(60)

            self.bouton()
            


    #c'est le plus important (bouton + fond)
    def bouton(self):
        #creation du fond d'écran
        ecran = pygame.image.load("./Fond/fond_galaxy_Getty_image.jpg").convert()
        ecran = pygame.transform.scale(ecran, (LARGEUR, HAUTEUR))
        self.screen.blit(ecran, (0, 0))


        font = pygame.font.Font(None, 74)

        text = font.render("ASTRONAUT RESCUER", True, (200, 200, 200))
        text_pos = text.get_rect(center = (LARGEUR/2, HAUTEUR/5))

        self.screen.blit(text, text_pos)


        font_bouton = pygame.font.Font(None, 60)

        #bouton commencer
        text_commencer = font_bouton.render("Commencer", True, (100, 255, 100))

        # Rectangle du texte
        commencer = text_commencer.get_rect(center=(LARGEUR/3, HAUTEUR/2))

        self.screen.blit(text_commencer, commencer)


        #bouton quitter
        text_quitter = font_bouton.render("Quitter", True, (255, 100, 100))

        # Rectangle du texte
        quitter = text_quitter.get_rect(center=((2/3)*LARGEUR, HAUTEUR/2))

        self.screen.blit(text_quitter, quitter)
        
        #évènement cliquer sur les boutons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if commencer.collidepoint(event.pos):
                    pygame.mixer.stop()
                    jouer()
                if quitter.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                sys.exit()
                    

menu().run()