import pygame
import random
import animation

#creer et gerer monstre
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        #ifliger les degats
        self.health -= amount

        #verifier si point de vie sup ou egal a zero
        if self.health <=0:
            #Reaparaitre comme nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            #ajout du nombre de score
            #self.game.score += 20
            self.game.add_score(self.loot_amount)

            #si la barre d'ev est charge a son maximum
            if self.game.comet_event.is_full_loaded():
                #retirer du jeu
                self.game.all_monsters.remove(self)

                # appel de la methode declenchement la pluie de comette
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        #dession de la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 200, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        #deplacemen  si pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si il a collusion entre monstre et joueur
        else:
            #infliger degat au joueur
            self.game.player.damage(self.attack)

#classe de la mummy
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)

#classe pour le montre l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(80)