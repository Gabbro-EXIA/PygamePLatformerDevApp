import pygame, sys
from pygame.locals import *

# création d'une fenêtre d'affichage pour le jeu

pygame.init() #initialisation

FPS = pygame.time.Clock()

FENETRE = pygame.display.set_mode((1280, 720)) # Résolution HD, suffisant pour tester la classe joueur

class Plateforme(pygame.sprite.Sprite) :
    def __init__(self,x,y,image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (200, 40))
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def afficher(self, surface : pygame.surface.Surface):
        surface.blit(self.image, self.rect)

class Joueur(pygame.sprite.Sprite):
    def __init__(self, image : str = "neutre_D")->None:
        """Création d'un nouveau Joueur et initialisation des variables"""
        super().__init__() # On fait de notre Joueur un objet utilisable par la classe Sprite
        self.etat = ["neutre_D", "neutre_G", "saut_D", "saut_G", "mouv_D", "mouv_G"]
        self.etat = {k : f"./Perso/{k}.png" for k in self.etat}
        self.source = image
        self.image = pygame.image.load(self.etat[image]).convert_alpha()
        self.position = self.image.get_rect()
        self.position.bottomleft = (0, 720) # On place notre perso en bas à gauche
        self.saut = False # En train de sauter ? (Par défaut non)
        self.hauteur = 250 # Permet de savoir l'état du saut + hauteur
        self.rect = self.position # Pour la fonction de collision

    def deplacement(self):
        """Gére les déplacements du Joueur :\n
        - q ou ← (flèche gauche) pour se déplacer à gauche\n
        - d ou → (flèche droite) pour se déplacer à droite"""
        touche = pygame.key.get_pressed()

        if touche[K_q] or touche[K_LEFT]:
            if not self.saut:
                self.maj("mouv_G")
            self.position.left -= 1
        elif touche[K_d] or touche[K_RIGHT]:
            if not self.saut:
                self.maj("mouv_D")
            self.position.left += 1 
    
    def maj(self, image : str)->None:
        """Met à jour l'image du Joueur (pendant le déplacement ou pas)"""
        self.image = pygame.image.load(self.etat[image]).convert_alpha()
        self.source = image

    def tomber(self)->None:
        """Gère le système de gravité pour le Joueur et les images"""
        touche = pygame.key.get_pressed()

        if touche[K_q] or touche[K_LEFT]:
            self.maj("saut_G")
        elif touche[K_d] or touche[K_RIGHT]:
            self.maj("saut_D")
        else:
            self.maj("saut_G") if self.source[-1] == 'G' else self.maj("saut_D")

        self.position.bottom += 1
        self.saut = True
    
    def sauter(self)->None:
        """Permet au Joueur de sauter tout en metant à jour l'image"""
        touche = pygame.key.get_pressed()

        if touche[K_q] or touche[K_LEFT]:
            self.maj("saut_G")
        elif touche[K_d] or touche[K_RIGHT]:
            self.maj("saut_D")
        else:
            self.maj("saut_G") if self.source[-1] == 'G' else self.maj("saut_D")

        self.position.top -= 1
        self.saut = True
        
def jouer()->None:
    """Boucle de jeu principale"""

# On initilialise les variables nécessaires

    joueur = Joueur()

    sol = pygame.image.load("./Sol/sol.png").convert()
    sol = pygame.transform.scale(sol, (1280, 40))

    plateformes = pygame.sprite.Group()
    plateformes.add(Plateforme(200, 500,"./Plateforme/plateforme.png"))
    plateformes.add(Plateforme(600, 400,"./Plateforme/plateforme.png"))

    son = pygame.mixer.Sound("./Son/freesound_community-space-ambience-56265.mp3")
    son.play(-1) # On joue le son en boucle

    fond = pygame.image.load("./Fond/fond_galaxy_Getty_image.jpg").convert()
    fond = pygame.transform.scale(fond, (1280, 720))


#On teste la classe Joueur dans la boucle de jeu


    while True:
        FENETRE.blit(fond, (0, 0)) # On remplit la fenêtre de jeu de rouge
        for plateforme in plateformes : 
            plateforme.afficher(FENETRE)
        FENETRE.blit(sol, (0, 680))
        FENETRE.blit(joueur.image, joueur.position)
        pygame.display.flip() # on affiche notre perso
        for events in pygame.event.get():
            if events.type == QUIT: #si l'utilisateur clique sur la croix pour fermer la fenêtre, on ferme le jeu
                sys.exit()
            elif events.type == KEYDOWN:
                if events.key == K_SPACE or events.key == K_UP:
                    if joueur.position.bottom == 720 or any(pygame.sprite.spritecollide(joueur, plateformes, False, collision)):
                        joueur.hauteur = 0
        if joueur.hauteur < 250:
            joueur.sauter()
            joueur.hauteur+=1
        if joueur.hauteur == 250:
            if joueur.position.bottom != 720 and not any(pygame.sprite.spritecollide(joueur, plateformes, False, collision)):
                joueur.tomber()
            else:
                joueur.saut = False
                joueur.maj("neutre_G") if joueur.source[-1] == "G" else joueur.maj("neutre_D")
        if joueur.position.right < 0:
            joueur.position.right = 1280
        elif joueur.position.left > 1280:
            joueur.position.left = 0
        joueur.deplacement()
        FPS.tick(60) # Gère la vitesse à laquelle se déplace le perso 

def collision(Sprite1 : pygame.sprite.Sprite, Sprite2 : pygame.sprite.Sprite)->bool:
    """On vérifie si 2 Sprite sont en collision"""
    if Sprite1.rect.bottom == Sprite2.rect.top and Sprite1.rect.centerx >= Sprite2.rect.left and Sprite1.rect.centerx <= Sprite2.rect.right:
        return True
    return False
