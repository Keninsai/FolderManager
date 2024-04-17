#Math used for rotation(def rotate)
import pygame, math


class player:

    def __init__(self, loadSprite, x=0, y=0, w=25, h=25, speed=0.2):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.original_sprite = pygame.image.load(loadSprite)#Replace with funciton to chose sprite    
        self.sprite = self.original_sprite    
        self.rect = self.sprite.get_rect(center = (x, y))
    #These are the default buttons for movement
        self.move_up = pygame.K_UP
        self.move_down = pygame.K_DOWN
        self.move_right = pygame.K_RIGHT
        self.move_left = pygame.K_LEFT

    #Fucntion for setting keybindings
    #Keybindings are up,down,right and left
    #WASD Exemple: player.keybinds(pygame.K_w, pygame.K_s, pygame.K_d, pygame.K_a)
    def keybinds(self, keyup, keydown, keyright, keyleft):
        self.move_up = keyup
        self.move_down = keydown
        self.move_right = keyright
        self.move_left = keyleft
        
    #This will rotate the player towards the cursor
    #Works only if the cursor is inside the window
    #The Sprite used needs to look downwards, else change the angle from 90 degrees to what you need
    def rotate(self):
        mosx, mosy = pygame.mouse.get_pos()
        dist_x = mosx - self.x 
        dist_y = -(mosy - self.y)
        angle = math.degrees(math.atan2(dist_y, dist_x))
        self.sprite = pygame.transform.rotate(self.original_sprite, angle + 90)
        self.rect = self.sprite.get_rect(center = (self.x, self.y))
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.move_up]:
            self.y -= self.speed
        if keys[self.move_down]:
            self.y += self.speed
        if keys[self.move_right]:
            self.x += self.speed
        if keys[self.move_left]:
            self.x -= self.speed
        self.rect = self.sprite.get_rect(center = (self.x, self.y))

    def draw(self, scene):
        scene.blit(self.sprite, self.rect)


    
        






