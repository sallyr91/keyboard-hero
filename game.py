#SALVATORE ROSA - KEYBOARD HERO

import myutil
import pygame
from pygame.locals import *
import sys
import random
import winsound
import pygame.midi

#CONSTANTS ------
#              wid  hei
SCREENSIZE  = (640, 480) 
MARGIN      = 16         #SPACE OFF SIDE OF GAME SCREEN
PADDING     = 8          #SPACE BETWEEN GAMEPAD KEYS
CELLSIZE    = (32, 32)   #SIZE OF A TYPICAL RECTANGLE
GAMEPADSIZE = (32, 16)
BUTTONSIZE  = (SCREENSIZE[0]-MARGIN*2, 128)
#CONSTANTS ------

#CLASS FOR ALL VISABLE PIECES
class Thing(Rect):
	def __init__(self, location, size, tag=None, image=None, position=None):
		super().__init__(location, size)
		self.tag   = tag
		self.image = image
		
	def draw(self, display_surface):
		display_surface.blit(self.image, self)
		
	def move_down(self, amount):
		self.move_ip(0, amount)

def get_gamepad(image):
	keys = ['c', 'C', 'd', 
	        'D', 'e', 'f', 
		    'F', 'g', 'G', 
			'a', 'A', 'b',
			'o']
			
	y_location = SCREENSIZE[1] - MARGIN - GAMEPADSIZE[0] - GAMEPADSIZE[0]
	
	for x in range(MARGIN, len(keys)*(GAMEPADSIZE[0]+PADDING), GAMEPADSIZE[0]+PADDING):
		yield keys[0], Thing((x, y_location), GAMEPADSIZE, keys.pop(0), image)
		
def get_lives(image, num_lives):
	for y in range(MARGIN, num_lives*(CELLSIZE[0]+PADDING), CELLSIZE[0]+PADDING):
		yield Thing((SCREENSIZE[0]-MARGIN-CELLSIZE[0], y), CELLSIZE, 'life', image)
		
def get_menu_buttons(button_size, num_buttons):
	for y in range(num_buttons):
		yield Thing((MARGIN, MARGIN+button_size[1]*y+(MARGIN*y)), button_size, 'song{0}.txt'.format(y))
		
def label_rects(displaysurf, rects, text, font_type, font_size, text_color):
	assert len(rects) == len(text)

	font = pygame.font.Font(font_type, font_size)
	
	for t, r in zip(text, rects):
		text_surface     = font.render(t, True, text_color)
		text_rect        = text_surface.get_rect()
		text_rect.center = (r.x+r.width/2, r.y+r.height/2)
		displaysurf.blit(text_surface, text_rect)
	

#READ FILE AND YIELD NOTES 		
def load_notes(file, note_positions, images):
	notes = {'c' : 0, 'C' : 1,  'd' : 2, 
	         'D' : 3, 'e' : 4,  'f' : 5, 
		     'F' : 6, 'g' : 7,  'G' : 8, 
		   	 'a' : 9, 'A' : 10, 'b' : 11,
			 'o' : 12,}

	with open(file) as f:
		while True:
			char = f.read(1)
			
			if char == 'x':
				yield Thing((-50, -50),  CELLSIZE, 'dummy')
			elif char == 'c':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			elif char == 'C':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			elif char == 'd':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			elif char == 'D':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			elif char == 'e':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			elif char == 'f':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			elif char == 'F':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			elif char == 'g':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			elif char == 'G':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			elif char == 'a':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			elif char == 'A':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			elif char == 'b':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			elif char == 'o':
				yield Thing(note_positions[notes[char]], CELLSIZE, 'note', random.choice(images))
			else:
				break #WHY DO I NEED THIS? SHOULD WORK WITHOUT...
							
def main():
	pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.init()
	pygame.midi.init()
	
	pygame.display.set_caption('Keyboard Hero')
	
	#IMAGES ------
	key_image      = myutil.load_image('key.png', 'images')
	key_good_image = myutil.load_image('key_good.png', 'images')
	key_bad_image  = myutil.load_image('key_bad.png', 'images')
	note_image     = myutil.load_image('note.png', 'images')
	note2_image    = myutil.load_image('note2.png', 'images')
	note3_image    = myutil.load_image('note3.png', 'images')
	note4_image    = myutil.load_image('note4.png', 'images')
	note5_image    = myutil.load_image('note5.png', 'images')
	note6_image    = myutil.load_image('note6.png', 'images')
	life_image     = myutil.load_image('life.png', 'images')
	win_image      = myutil.load_image('win.png', 'images')
	lose_image     = myutil.load_image('lose.png', 'images')
	#IMAGES ------
	
	pygame.display.set_icon(random.choice([note_image, note2_image, note3_image, 
										   note4_image, note5_image, note6_image]))
	
	#SOUNDS ------
	win_sound      = myutil.load_sound('win.ogg', 'sounds')
	lose_sound     = myutil.load_sound('lose.ogg', 'sounds')
	miss_sound     = myutil.load_sound('miss.ogg', 'sounds')
	c_sound        = myutil.load_sound('c.ogg', 'sounds')
	c_sharp_sound  = myutil.load_sound('c#.ogg', 'sounds')
	d_sound	       = myutil.load_sound('d.ogg', 'sounds')
	d_sharp_sound  = myutil.load_sound('d#.ogg', 'sounds')
	e_sound        = myutil.load_sound('e.ogg', 'sounds')
	f_sound        = myutil.load_sound('f.ogg', 'sounds')
	f_sharp_sound  = myutil.load_sound('f#.ogg', 'sounds')
	g_sound        = myutil.load_sound('g.ogg', 'sounds')
	g_sharp_sound  = myutil.load_sound('g#.ogg', 'sounds')
	a_sound        = myutil.load_sound('a.ogg', 'sounds')
	a_sharp_sound  = myutil.load_sound('a#.ogg', 'sounds')
	b_sound        = myutil.load_sound('b.ogg', 'sounds')
	c_octave_sound = myutil.load_sound('co.ogg', 'sounds')
	#SOUNDS ------
	
	#MIDI ------
	midi_note  = None
	midi_info  = []
	midi_input = pygame.midi.Input(pygame.midi.get_default_input_id())
	#MIDI ------
	
	#MENU ------
	font             = pygame.font.Font('freesansbold.ttf', 32)
	font_color       = myutil.BLUE
	menu_button_size = (SCREENSIZE[0]-MARGIN*2, 128)
	num_menu_buttons = 3
	menu_text        = ['Song 1', 'Song 2', 'Song 3']
	menu_font        = 'freesansbold.ttf'
	menu_highlight_color = myutil.BLUE
	#MENU ------
	
	#LISTS AND STUFF ------
	at_menu          = True
	displaysurf      = pygame.display.set_mode(SCREENSIZE)
	fps              = 60
	fpsclock         = pygame.time.Clock()
	num_lives        = 10
	count            = 0  #FOR TIMING THE ARRIVAL OF NOTES
	count_divisor    = 32
	move_amount      = 2  #HOW FAST NOTES MOVE TOWARD GAMEPAD
	note_images      = [note_image, 
	                    note2_image, 
					    note3_image, 
					    note4_image,
					    note5_image,
					    note6_image]
	notes_in_play  = [] #CURRENT NOTES ON BOARD
	gamepad        = dict(get_gamepad(key_image)) #YOUR PRESSABLE BUTTONS
	menu_buttons   = list(get_menu_buttons(menu_button_size, num_menu_buttons))
	lives          = list(get_lives(life_image, num_lives))
	note_positions = [] #FOR LINING UP INCOMING NOTES WITH GAMEPAD
	notes          = []
	#LINE UP INCOMING NOTES WITH GAMEPAD BUTTONS
	for k, v in gamepad.items():
		note_positions.append((v.x, MARGIN))
	note_positions = sorted(note_positions, key=lambda note : note[0])
	#LISTS AND STUFF ------
	
	while True:
		displaysurf.fill(myutil.BLACK)
		
		#GET MIDI DATA
		midi_info = midi_input.read(1000)
		#IF THERE IS DATA AND KEYDOWN EVENT STORE NOTE VALUE
		if midi_info:
			if 145 in midi_info[0][0]:
				midi_note = midi_info[0][0][1]
			else:
				midi_note = None
			
		if at_menu:
			for event in pygame.event.get():
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					myutil.terminate()
				elif event.type == MOUSEBUTTONDOWN:
					for button in menu_buttons:
						if button.collidepoint(pygame.mouse.get_pos()):
							notes = list(load_notes('songs\{0}'.format(button.tag), note_positions, note_images))
							at_menu = False
			for button in menu_buttons:
				pygame.draw.rect(displaysurf, myutil.RED, button)
				if button.collidepoint(pygame.mouse.get_pos()):
					myutil.highlight_rect(displaysurf, button, menu_highlight_color, 135)	
			label_rects(displaysurf, menu_buttons, menu_text, menu_font, 32, font_color)	
		else:
			for k, v in gamepad.items():
				v.draw(displaysurf)
				
			for life in lives:
				life.draw(displaysurf)
		
			for event in pygame.event.get():
				if event.type == QUIT:
					myutil.terminate()
				
				elif event.type == KEYDOWN and event.key == K_q:
					if notes_in_play:
						if gamepad['c'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['c'])
							notes_in_play.pop(gamepad['c'].collidelist(notes_in_play))
							c_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['c'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['c'])
						if lives:
							lives.pop()
						
				elif event.type == KEYDOWN and event.key == K_w:
					if notes_in_play:
						if gamepad['C'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['C'])
							notes_in_play.pop(gamepad['C'].collidelist(notes_in_play))
							c_sharp_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['C'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['C'])
						if lives:
							lives.pop()
						
				elif event.type == KEYDOWN and event.key == K_e:
					if notes_in_play:
						if gamepad['d'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['d'])
							notes_in_play.pop(gamepad['d'].collidelist(notes_in_play))
							d_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['d'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['d'])
						if lives:
							lives.pop()
						
				elif event.type == KEYDOWN and event.key == K_r:
					if notes_in_play:
						if gamepad['D'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['D'])
							notes_in_play.pop(gamepad['D'].collidelist(notes_in_play))
							d_sharp_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['D'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['D'])
						if lives:
							lives.pop()
						
				elif event.type == KEYDOWN and event.key == K_t:
					if notes_in_play:
						if gamepad['e'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['e'])
							notes_in_play.pop(gamepad['e'].collidelist(notes_in_play))
							e_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['e'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['e'])
						if lives:
							lives.pop()
						
				elif event.type == KEYDOWN and event.key == K_y:
					if notes_in_play:
						if gamepad['f'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['f'])
							notes_in_play.pop(gamepad['f'].collidelist(notes_in_play))
							f_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['f'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['f'])
						if lives:
							lives.pop()
						
				elif event.type == KEYDOWN and event.key == K_u:
					if notes_in_play:
						if gamepad['F'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['F'])
							notes_in_play.pop(gamepad['F'].collidelist(notes_in_play))
							f_sharp_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['F'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['F'])
						if lives:
							lives.pop()
						
				elif event.type == KEYDOWN and event.key == K_i:
					if notes_in_play:
						if gamepad['g'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['g'])
							notes_in_play.pop(gamepad['g'].collidelist(notes_in_play))
							g_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['g'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['g'])
						if lives:
							lives.pop()
						
				elif event.type == KEYDOWN and event.key == K_o:
					if notes_in_play:
						if gamepad['G'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['G'])
							notes_in_play.pop(gamepad['G'].collidelist(notes_in_play))
							g_sharp_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['G'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['G'])
						if lives:
							lives.pop()
						
				elif event.type == KEYDOWN and event.key == K_p:
					if notes_in_play:
						if gamepad['a'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['a'])
							notes_in_play.pop(gamepad['a'].collidelist(notes_in_play))
							a_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['a'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['a'])
						if lives:
							lives.pop()
						
				elif event.type == KEYDOWN and event.key == K_LEFTBRACKET:
					if notes_in_play:
						if gamepad['A'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['A'])
							notes_in_play.pop(gamepad['A'].collidelist(notes_in_play))
							a_sharp_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['A'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['A'])
						if lives:
							lives.pop()
						
				elif event.type == KEYDOWN and event.key == K_RIGHTBRACKET:
					if notes_in_play:
						if gamepad['b'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['b'])
							notes_in_play.pop(gamepad['b'].collidelist(notes_in_play))
							b_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['b'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['b'])
						if lives:
							lives.pop()
						
				elif event.type == KEYDOWN and event.key == K_BACKSLASH:
					if notes_in_play:
						if gamepad['o'].collidelist(notes_in_play) != -1:
							displaysurf.blit(key_good_image, gamepad['o'])
							notes_in_play.pop(gamepad['o'].collidelist(notes_in_play))
							c_octave_sound.play()
						else:
							displaysurf.blit(key_bad_image, gamepad['o'])
							miss_sound.play()
							if lives:
								lives.pop()
					else:
						displaysurf.blit(key_bad_image, gamepad['o'])
						if lives:
							lives.pop()
			
			#MIDI KEYDOWN EVENT ------
			if midi_note == 48:
				midi_note = None
				if notes_in_play:
					if gamepad['c'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['c'])
						notes_in_play.pop(gamepad['c'].collidelist(notes_in_play))
						c_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['c'])
						miss_sound.play()
						if lives:
							lives.pop()
							
			elif midi_note == 49:
				midi_note = None
				if notes_in_play:
					if gamepad['C'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['C'])
						notes_in_play.pop(gamepad['C'].collidelist(notes_in_play))
						c_sharp_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['C'])
						miss_sound.play()
						if lives:
							lives.pop()
							
			elif midi_note == 50:
				midi_note = None
				if notes_in_play:
					if gamepad['d'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['d'])
						notes_in_play.pop(gamepad['d'].collidelist(notes_in_play))
						d_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['d'])
						miss_sound.play()
						if lives:
							lives.pop()
							
			elif midi_note == 51:
				midi_note = None
				if notes_in_play:
					if gamepad['D'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['D'])
						notes_in_play.pop(gamepad['D'].collidelist(notes_in_play))
						d_sharp_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['D'])
						miss_sound.play()
						if lives:
							lives.pop()
							
			elif midi_note == 52:
				midi_note = None
				if notes_in_play:
					if gamepad['e'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['e'])
						notes_in_play.pop(gamepad['e'].collidelist(notes_in_play))
						e_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['e'])
						miss_sound.play()
						if lives:
							lives.pop()
							
			elif midi_note == 53:
				midi_note = None
				if notes_in_play:
					if gamepad['f'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['f'])
						notes_in_play.pop(gamepad['f'].collidelist(notes_in_play))
						f_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['f'])
						miss_sound.play()
						if lives:
							lives.pop()
							
			elif midi_note == 54:
				midi_note = None
				if notes_in_play:
					if gamepad['F'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['F'])
						notes_in_play.pop(gamepad['F'].collidelist(notes_in_play))
						f_sharp_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['F'])
						miss_sound.play()
						if lives:
							lives.pop()
							
			elif midi_note == 55:
				midi_note = None
				if notes_in_play:
					if gamepad['g'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['g'])
						notes_in_play.pop(gamepad['g'].collidelist(notes_in_play))
						g_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['g'])
						miss_sound.play()
						if lives:
							lives.pop()
							
			elif midi_note == 56:
				midi_note = None
				if notes_in_play:
					if gamepad['G'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['G'])
						notes_in_play.pop(gamepad['G'].collidelist(notes_in_play))
						g_sharp_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['G'])
						miss_sound.play()
						if lives:
							lives.pop()
							
			elif midi_note == 57:
				midi_note = None
				if notes_in_play:
					if gamepad['a'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['a'])
						notes_in_play.pop(gamepad['a'].collidelist(notes_in_play))
						a_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['a'])
						miss_sound.play()
						if lives:
							lives.pop()
							
			elif midi_note == 58:
				midi_note = None
				if notes_in_play:
					if gamepad['A'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['A'])
						notes_in_play.pop(gamepad['A'].collidelist(notes_in_play))
						a_sharp_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['A'])
						miss_sound.play()
						if lives:
							lives.pop()
							
			elif midi_note == 59:
				midi_note = None
				if notes_in_play:
					if gamepad['b'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['b'])
						notes_in_play.pop(gamepad['b'].collidelist(notes_in_play))
						b_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['b'])
						miss_sound.play()
						if lives:
							lives.pop()
							
			elif midi_note == 60:
				midi_note = None
				if notes_in_play:
					if gamepad['o'].collidelist(notes_in_play) != -1:
						displaysurf.blit(key_good_image, gamepad['o'])
						notes_in_play.pop(gamepad['o'].collidelist(notes_in_play))
						c_octave_sound.play()
					else:
						displaysurf.blit(key_bad_image, gamepad['o'])
						miss_sound.play()
						if lives:
							lives.pop()
			#MIDI KEYDOWN EVENT ------
			
			#ADD NOTE TO notes_in_play IF ITS TIME TO COME OUT
			if notes:
				if count % count_divisor == 0:
					notes_in_play.append(notes.pop(0))
			
			#DRAW AND MOVE NOTES IN PLAY, REMOVE DUMMY NOTES SO YOU CAN WIN
			if notes_in_play:
				for note in notes_in_play:
					if note.tag != 'dummy':
						note.draw(displaysurf)
						note.move_down(move_amount)
					else:
						notes_in_play.remove(note)
			
			#LOSE LIFE AND REMOVE NOTE FROM PLAY IF NOTE GOES PAST GAMEPAD
			if notes_in_play:
				for note in notes_in_play:
					if note.y + note.height >= SCREENSIZE[1]:
						if lives:
							lives.pop()
						notes_in_play.remove(note)
			
			count += move_amount
			
			#LOSE GAME
			if not lives:
				at_menu = True
				notes          = []
				notes_in_play  = []
				note_positions = []
				gamepad        = dict(get_gamepad(key_image)) #YOUR PRESSABLE BUTTONS
				menu_buttons   = list(get_menu_buttons(menu_button_size, num_menu_buttons))
				lives          = list(get_lives(life_image, num_lives))
				for k, v in gamepad.items():
					note_positions.append((v.x, MARGIN))
				note_positions = sorted(note_positions, key=lambda note : note[0])
				count = 0
				displaysurf.blit(lose_image, (0, 0))
				pygame.display.update()
				pygame.mixer.stop()
				lose_sound.play()
				pygame.time.delay(4000)
				
			#WIN GAME
			if (not notes 
				and not notes_in_play 
				and not at_menu):
					at_menu = True
					notes          = []
					notes_in_play  = []
					note_positions = []
					gamepad        = dict(get_gamepad(key_image)) #YOUR PRESSABLE BUTTONS
					menu_buttons   = list(get_menu_buttons(menu_button_size, num_menu_buttons))
					lives          = list(get_lives(life_image, num_lives))
					for k, v in gamepad.items():
						note_positions.append((v.x, MARGIN))
					note_positions = sorted(note_positions, key=lambda note : note[0])
					count = 0
					displaysurf.blit(win_image, (0, 0))
					pygame.display.update()
					#pygame.mixer.stop()
					#win_sound.play()
					pygame.time.delay(4000)
		
		pygame.display.update()
		fpsclock.tick(fps)
		
if __name__ == '__main__':
	main()