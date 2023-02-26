#створи гру "Лабіринт"!

from pygame import *
from pygame import mixer

#класс "2батя"
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        #вікно, x, y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            
    
win_width = 700
win_height = 500

window = display.set_mode((win_width, win_height))
display.set_caption('Лабіринт')
background = transform.scale(image.load("background.jpg"), (win_width, win_height))


player = GameSprite('hero.png', 5, win_height - 80, 4)
monster = GameSprite('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 2)

game = True
clock = time.Clock()
fps = 60

#вах музика
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
 
    
    window.blit(background, (0, 0))
    player.reset()
    monster.reset()

    display.update()
    clock.tick(fps)
