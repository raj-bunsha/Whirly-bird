import pygame
class Platform1(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.x=x
		self.y=y
		self.speed=0
		self.plat=pygame.image.load('assets/plat.png')
		self.rect=self.plat.get_rect()

	def draw(self,win,camera):
		self.rect=win.blit(self.plat,(self.x,self.y-camera[1]))

