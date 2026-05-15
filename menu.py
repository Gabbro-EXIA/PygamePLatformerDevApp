import sys

import pygame

class fenetre:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Astronaut Rescuer')
        self.screen = pygame.display.set_mode((640, 480))

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
        self.screen = pygame.display.set_mode((640, 480))

        

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

            self.bouton()
            



    def bouton(self):
        #creation du fond d'écran
        ecran = pygame.image.load("visuel/fond_galaxy_Getty_image.jpg").convert()
        self.screen.blit(ecran, (0, 0))


        font = pygame.font.Font(None, 74)

        text = font.render("ASTRONAUT RESCUE", True, (200, 200, 200))

        self.screen.blit(text, (50, 125))


        font_bouton = pygame.font.Font(None, 60)

        #bouton commencer
        text_commencer = font_bouton.render("Commencer", True, (100, 255, 100))

        # Rectangle du texte
        commencer = text_commencer.get_rect(center=(50, 300))

        self.screen.blit(text_commencer, (50, 300))


        #bouton quitter
        text_quitter = font_bouton.render("Quitter", True, (255, 100, 100))

        # Rectangle du texte
        quitter = text_quitter.get_rect(center=(400, 300))

        self.screen.blit(text_quitter, (400, 300))

        #évènement cliquer sur les boutons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if commencer.collidepoint(event.pos):
                    fenetre().run()
                if quitter.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                    

menu().run()