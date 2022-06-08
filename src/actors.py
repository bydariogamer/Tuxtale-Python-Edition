import pygame as pg
pg.font.init()
import math
from .gmglobal import*

class Map():
	def __init__(self, _a):
		self.actlast = 0
		self.actor = []
		self.actor_empty = {}
		self.a = _a

gmMap = Map(5)

class Actor():
	id = 0
	def __init__(self, _x, _y, _arr = None):
		self.x = _x
		self.y = _y
		self.arr = _arr
		self.anim = None
		self.frame = None
		self.shape = None
		self.frameIndex = 0
		self.id = Actor.id
		self.frame = []
		if(not self.arr):
			return
		if self.arr.len() == 1:
			pass
	
	def loadSprite(self, _spr):
		sprSize = _spr.get_size()
		sprW = int(sprSize[0])
		sprH = int(sprSize[1])

		for i in range(0, int(sprH/16)):
			for j in range(0, int(sprW/16)):
				self.frame.append((j*16, i*16, 16, 16))
	
	def run(self):
		pass

	def destructor():
		pass

	def _typeof():
		return "Actor"
	
def runActors():
	for i in gmMap.actor:
		i.run()

def newActor(_type, _x, _y, _arr = None):
	na = _type(_x, _y, _arr)
	na.id = gmMap.actlast
	gmMap.actor.append(na)
	##gmMap.actor[gmMap.actlast] = na
	gmMap.actlast += 1

class Tux(Actor):
	def __init__(self, _x, _y, _arr = None):
		super().__init__(_x, _y, _arr = None)
		self.x = _x
		self.y = _y
		self.arr = _arr
		self.frame = []
		self.walkRight = [0.0, 3.0]
		self.walkUp = [4.0, 7.0]
		self.walkDown = [8.0, 11.0]
		self.walkLeft = [12.0, 15.0]
		self.standRight = [0]
		self.standLeft = [12]
		self.standUp = [4]
		self.standDown = [8]
		self.anim = self.walkRight
		self.standStillAnim = self.standRight
		self.xspeed = 0
		self.yspeed = 0
		self.autocon = False
		self.stepCount = 0
		self.loadSprite(sprTux)
		if not _arr:
			return

	def run(self):
		key = pg.key.get_pressed()

		if not key[config["key"]["right"]] and not key[config["key"]["left"]] and not self.autocon == True:
			self.xspeed = 0
			self.anim = self.standStillAnim

		if not key[config["key"]["up"]] and not key[config["key"]["down"]] and not self.autocon == True:
			self.yspeed = 0
			self.anim = self.standStillAnim

		if key[config["key"]["right"]]:
			self.xspeed = 1
			self.anim = self.walkRight
			self.standStillAnim = self.standRight
		
		if key[config["key"]["left"]]:
			self.xspeed = -1
			self.anim = self.walkLeft
			self.standStillAnim = self.standLeft
		
		if key[config["key"]["up"]]:
			self.yspeed = -1
			self.anim = self.walkUp
			self.standStillAnim = self.standUp
		
		if key[config["key"]["down"]]:
			self.yspeed = 1
			self.anim = self.walkDown
			self.standStillAnim = self.standDown
		
		for event in pg.event.get():
			if event.type == pg.KEYDOWN:
				print("Is it working at all???")
				if key[config["key"]["left"]]:
					self.frameIndex = self.stepCount % 2
					print("Test")
				

		self.x += self.xspeed
		self.y += self.yspeed

		self.frameIndex += 0.05
		drawSprite(sprTux, self.frame[int(self.anim[0]) + math.floor(self.frameIndex % (self.anim[-1] - self.anim[0] + 1))], self.x, self.y)


