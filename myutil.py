import os
import sys
import pygame

#OTHER ------
UP        = 'up'
DOWN      = 'down'
LEFT      = 'left'
RIGHT     = 'right'
#OTHER ------

#COLORS ------
#           R--  G--  B--
BLACK    = (  0,   0,   0)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (0,   255,   0)
BLUE     = (0,     0, 255)
PURPLE   = (255,   0, 255)
YELLOW   = (255, 255,   0)
AQUA     = (  0, 255, 255)
BROWN    = (165,  42,  42)
PINK     = (255, 192, 203)
COLORKEY = (244, 244, 244)
#COLORS ------

#FUNCTIONS ------
def cc(x, y, cell_size):
		return (x * cell_size, y * cell_size)

def load_image(name, folder='', colorkey=None):
	fullname = os.path.join(folder, name)
	
	try:
		image = pygame.image.load(fullname) #.convert()
	except pygame.error as message:
		print('Cannot load image:', name)
		print(message)
		raise SystemExit
	
	if colorkey != None:
		#colorkey = image.get_at((0,0)) #get pixel in corner to use as colorkey?
		image.set_colorkey(colorkey, pygame.RLEACCEL)
		
	return image #, image.get_rect()
	
def load_sound(name, folder=''):
	class NoneSound:
		def play(self): pass
		
	if not pygame.mixer:
		return NoneSound()
		
	fullname = os.path.join(folder, name)
	
	try:
		sound = pygame.mixer.Sound(fullname)
	except pygame.error as message:
		print('Cannot load sound:', name)
		print(message)
		raise SystemExit
		
	return sound

#chop image into individual sprites
def chop_image(image, sub_image_size):
	#change to yield ?
	image_list = []
	index      = 0 
	
	for x in range(0, image.get_width(), sub_image_size[0]):
		image_list.append([])
		for y in range(0, image.get_height(), sub_image_size[1]):
			image_list[index].append(image.subsurface(pygame.Rect((x, y), 
			                                             sub_image_size)))
		index += 1
		
	return image_list

def highlight_rect(surface, destination_rect, color, alpha_value):
	highlighter = pygame.Surface(destination_rect.size)
	highlighter.set_alpha(alpha_value)
	highlighter.fill(color)
	
	surface.blit(highlighter, destination_rect)
	
	return highlighter

def terminate():
	pygame.quit()
	sys.exit()
#FUNCTIONS ------