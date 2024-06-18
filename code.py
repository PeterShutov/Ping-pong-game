from PyGame import *

class GameSprite(sprite.Sprite):
    def __init__(self, picture, rect_x, rect_y, w, h, speed):
        super().__init__()
        self.picture = transform.scale(image.load(picture), (w, h))
        self.rect = self.picture.get_rect()
        self.speed = speed
        self.rect.x = rect_x
        self.rect.y = rect_y

    def reset(self):
        window.blit(self.picture, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 15:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed  

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_o] and self.rect.y > 15:
            self.rect.y -= self.speed

        if keys[K_l] and self.rect.y < 400:
            self.rect.y += self.speed
#I wrote the player's class

window = display.set_mode((700, 500))
display.set_caption('Ping Pong')

background = transform.scale(image.load('tennis-court-top-view-illustration-vector.jpg'), (700, 500))
#Added a window and background

player_left = Player('tennis_rocket.png', 30, 230, 90, 90, 10)
player_right = Player('tennis_rocket.png', 600, 230, 90, 90, 10)
sfera = GameSprite('Ball-PNG.png', 330, 230, 50, 50, 10)
#Instances of the class

game = True
finish = False

while game:
    

    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player_left.reset()
        player_right.reset()
        sfera.reset()
        player_left.update_left()
        player_right.update_right()

    sfera.rect.x += speed_x
        sfera.rect.y += speed_y

        if sfera.rect.y > 400 or sfera.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(player_left, sfera) or sprite.collide_rect(player_right, sfera):
            speed_x *= -1

        if sfera.rect.x < 0:
            finish = True
            window.blit(loose_1, (250, 230))

        if sfera.rect.x > 700:
            finish = True
            window.blit(loose_2, (250, 230))

    display.update()
#Game cycle
