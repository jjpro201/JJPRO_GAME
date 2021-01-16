import pygame

#classe occupant des animations
class AnimateSprite(pygame.sprite.Sprite):

    #choses a faire a la creation de l'entite
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 #commencer l'anim a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #methode de demaration l'animation
    def start_animation(self):
        self.animation = True

    #definir une methode oiur animer le sprite
    def animate(self, loop=False):

        #passer a l'image suivante
        if self.animation:

            #passer a l'image suivante
            self.current_image += 1

            #verifie atteinte de la fin
            if self.current_image >= len(self.images):
                #remetre l'animation au depart
                self.current_image = 0

                #verifier si l'animation n'est pas en boucle
                if loop is False:
                    # desactivation de l'animation
                    self.animation = False

            #modifier l'image precedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

#fonction pour charger les images spirte
def load_animation_images(sprite_ame):
    #charger lees images de ce sprite dans le dossier correspondant
    images = []
    #recupere le chemin du dossier pour un sprite
    path = f"assets/{sprite_ame}/{sprite_ame}"

    #boucler sur chaque image de ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    #renvoyer le contenu
    return images


#definir un dictionnaire contenir les images chager de chauqe image
animations ={
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}