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
        #font = pygame.font.Font(None, 74)hjvbdjch

        #text = font.render("Commencer", True, (255, 255, 255))

        #self.screen.blit(text, (300, 200))

        #dimension bouton commencer
        commencer = pygame.Rect(300, 200, 100, 50)

        #création bouton commencer
        pygame.draw.rect(self.screen, (0, 128, 255), commencer)

        #dimension bouton quitter
        quitter = pygame.Rect(100, 200, 100, 50)

        #création bouton quitter
        pygame.draw.rect(self.screen, (0, 128, 255), quitter)

        #évènement cliquer sur les boutons
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if commencer.collidepoint(event.pos):
                    fenetre().run()
                if quitter.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                    

menu().run()