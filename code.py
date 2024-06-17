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
