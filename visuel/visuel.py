import sys

import pygame

class fenetre:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Astronaut Rescuer')
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()
    
        self.img = pygame.image.load('visuel/astro_neutre.png')

    def run(self):
        while True:
            self.screen.blit(self.img, (100, 200))
#affichage de l'astronaute neutre

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
#création de la fenetre
            
            pygame.display.update()
            self.clock.tick(60)
            
    


fenetre().run()