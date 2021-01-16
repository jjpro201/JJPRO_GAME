import pygame
import random

#creer classe de gestion comette
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #definir image associee a cette comette
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        #jouer le son
        self.comet_event.game.sound_manager.play('meteorite')

        #si le nombre de comette est de 0
        if len(self.comet_event.all_comets) == 0:
            print("Evenement fini")
            #remettre la barre a 0
            self.comet_event.reset_percent()
            #aparaitre les 2 premiers monstres
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        #ne tombe pas sur le sol
        if self.rect.y >= 500:
            print("Sol")
            #retirer la boule de feu
            self.remove()

            #si il n'y a plus de boule de feu sur le jeu
            if len(self.comet_event.all_comets) == 0:
                print("L'Evenement est fini ")
                #remetre la jauge au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        #verifier si la boule de feu touche le joueur
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            print("Joueur touche !")
            #retirer la boule de feu
            self.remove()
            #subir 20 points de degats
            self.comet_event.game.player.damage(20)
