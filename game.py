import pygame
import math
import random
from platforms import*
# from pygame.utils import*
pygame.init() 
win=pygame.display.set_mode((500,800))
clock=pygame.time.Clock()
camera=[0,0]
class Bird(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.x=x
		self.y=y
		self.speed=10
		self.bird=pygame.image.load('assets/bird.png')
		self.vy=0
		self.g=0.98/5
		self.rect=self.bird.get_rect()

	def draw(self):
		self.rect=win.blit(self.bird,(self.x,self.y-camera[1]))
		

	def move(self,x):
		self.x+=x*self.speed
		if self.x>=500:
			self.x-=500

	def fall(self):
		self.vy-=self.g
		self.y-=self.vy

	def collide(self):
		self.vy=14

class Platforms:
	def __init__(self):
		self.k=50
		self.platforms=[]
		self.dist=90
		for i in range(0,self.k):
			
			y=750-self.dist*i
			self.platforms.append(Platform1(random.randint(0,500-57),y))

	def createplatform(self):
		while len(self.platforms)<50:
			self.k+=1
			y=750-self.dist*self.k
			self.platforms.append(Platform1(random.randint(0,500-57),y))

	def removeplatform(self):
		for plat in self.platforms:
			if plat.y-camera[1]>=800:
				self.platforms.remove(plat)
			if pygame.sprite.collide_rect(bird,plat) and bird.vy<0:
				bird.collide()

	def drawplatform(self):
		for plat in self.platforms:
			plat.draw(win,camera)

bird=Bird(0,500)
platforms=Platforms()
while True:
	win.fill((255,255,255))
	clock.tick(60)
	fo= pygame.font.SysFont('Comic Sans MS', 20)
	textsurface = fo.render(f"Score:{int(-camera[1])}", True, (0,0,0))
	win.blit(textsurface,(0,0))
	if bird.y-camera[1]<=400:
		camera[1]+=(bird.y-camera[1]-400)
	if bird.y-camera[1]>800:
		fo= pygame.font.SysFont('Comic Sans MS', 28)
		textsurface = fo.render(f"Game over! Your score is {int(-camera[1])}", True, (0,0,0))
		platforms.platforms=[]
		win.blit(textsurface,(200-textsurface.get_rect().width//2,360))
	else:
		platforms.removeplatform()
		platforms.createplatform()
		platforms.drawplatform()
	bird.draw()
	bird.fall()
	
	keys=pygame.key.get_pressed()
	if keys[pygame.K_RIGHT]:
		bird.move(1)
	if keys[pygame.K_LEFT]:
		bird.move(-1)
	# if keys[pygame.K_UP]:
	# 	camera[1]-=5
	# if keys[pygame.K_DOWN]:
	# 	camera[1]+=5

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()

	pygame.display.update()
