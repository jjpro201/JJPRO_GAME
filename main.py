import pygame
import math
from game import Game
from player import Player
pygame.init()

#definir une clock
clock = pygame.time.Clock()
FPS = 60


#Fenetre
pygame.display.set_caption("JJPRO GAME")
screen = pygame.display.set_mode((1080, 720)) #1080, 720

#background
background = pygame.image.load('assets/bg.jpg')

#importer / charger la banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#importer ou charger bouton de lancement
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

#chargement jeu
game = Game()

#charge= ment joueur
#player = Player()

running = True

#Boucle
while running:

    #fond
    screen.blit(background, (0, -200))

    #verifier si le jeu commence ou non
    if game.is_playing:
        #declecher les instructions de la partie
        game.update(screen)
    #verifier si le jeu n'as pas commence
    else:
        #ajouter ecran bienvenue
        screen.blit(play_button, (play_button_rect))
        screen.blit(banner, (banner_rect))

    #update fenetre
    pygame.display.flip()

    #fermeture
    for event in pygame.event.get():
        #Femeture event
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture")
        #detection lachement touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detect si la touche espace est declenchee pour le projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # mettre le jeu en mode lance
                    game.start()
                    # jouer le son
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier si la souris est en collusion avec le bouton du jeu
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lance
                game.start()

                #jouer le son
                game.sound_manager.play('click')

    #fixer le nombre de FPS sur ma clock
    clock.tick(FPS)