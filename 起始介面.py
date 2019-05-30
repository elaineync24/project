# -*- coding:utf-8 -*-
import pygame as pg
#pygame初始化
pg.init()

#設定視窗
width, height = 620, 520                       #遊戲畫面寬和高
screen = pg.display.set_mode((width, height))   #依設定顯示視窗
pg.display.set_caption("GAME")           #設定程式標題

#建立background
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))

#按鈕
class Button():
	def __init__(self, color, x, y, width, height, text= ""):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text
		
	def draw(self, screen ,outline=None):
		if outline:
			pg.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
		pg.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
		if self.text != '':
			font = pg.font.Font('C:\\Windows\\Fonts\\Ulei00m.ttf', 18)
			text = font.render(self.text, 1, (0,0,0))
			screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

	def redraw(self):
		self.draw(screen, (0,0,0))

	def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
		return False

	def get_text(self):
		return str(self.text)
		
	def change_place(self,change_x,change_y):
		self.x = change_x
		self.y = change_y

def show_text(text, x, y):
	x = x 
	y = y
	font = pg.font.Font('C:\\Windows\\Fonts\\Ulei00m.ttf', 20)
	text = font.render(text, True, (255,255,255))
	screen.blit(text, (x,y))
	pg.display.update

#起始介面
image = pg.image.load("C:\\Users\\E5-572G\\Desktop\\商程project\\island.jpg")
image.convert()
image = pg.transform.scale(image, (620, 520))
bg.blit(image, (0,0))
	
#顯示
screen.blit(bg, (0,0))
pg.display.update()

run = True
button1 = Button((176,224,230), 250 , 440, 100 , 50 , "START:)")
while run:
	button1.redraw()
	pg.display.update()
	for event in pg.event.get():
		pos = pg.mouse.get_pos()
			
		if event.type == pg.MOUSEMOTION:
	
			if button1.isOver(pos):
				button1.color = (255,165 ,0)
				button1.draw(bg, (0,0,0))
			else:
				button1.color = (176, 224 ,230)
		
		if event.type == pg.MOUSEBUTTONDOWN:
			if button1.isOver(pos):
				run = False
screen.blit(bg, (0,0))
pg.display.update()


#第一關 (洞穴)
image2 = pg.image.load("C:\\Users\\E5-572G\\Desktop\\商程project\\cave.jpg")
image2.convert()
image2 = pg.transform.scale(image2, (620, 520))
bg.blit(image2, (0,0))

screen.blit(bg, (0,0))
pg.display.update()

run2 = True
but_me = Button((176,224,230), 400 , 10, 50 , 40 , u"我")
but_see = Button((176,224,230), 400 , 60, 50 , 40 , u"檢視")
but_stone = Button((176,224,230), 400 , 110, 50 , 40 , u"大石頭")
but_combine = Button((176,224,230), 400 , 160, 50 , 40 , u"結合")
but_move = Button((176,224,230), 400 , 210, 50 , 40 , u"移動到")
but_rub = Button((176,224,230), 400 , 260, 50 , 40 , u"摩擦")
'''
but_room = Button((176,224,230), 400 , 160, 50 , 40 , u"房間")
but_table = Button((176,224,230), 400 , 160, 50 , 40 , u"桌子")
but_bat = Button((176,224,230), 400 , 160, 50 , 40 , u"木棒")
but_metal = Button((176,224,230), 400 , 160, 50 , 40 , u"金屬")
'''

i = 0
while run2:
	show_text(u'"我"在冰冷的地板上醒來，"檢視"四周，發現似乎被關在一個被"大石頭"堵住的"洞穴"裡。',50,300)
	show_text(u'洞穴外傳來，此起彼落的尖叫聲"結合"怒吼。',50,350)
	show_text(u'我"移動到"洞穴口的大石頭旁，從石縫中往外看見一群食人族正在攻擊受傷的同伴，並啃食他們的斷肢，牙齒與骨頭的“摩擦”聲令人毛骨悚然.....',50,400)
	but_me .redraw()
	but_see.redraw()
	but_stone.redraw()
	but_combine.redraw()
	but_move.redraw()
	but_rub.redraw()
	pg.display.update()
	
	x1, y1 = 50 ,70
	x2,y2 = 170 ,70
	x3,y3 = 280 ,70
	
	if i == 0:
			x,y = 50 ,70
	elif i == 1:
			x,y = 170 ,70
	else: 
			x,y = 280 ,70
			
	
	for event in pg.event.get():
		pos = pg.mouse.get_pos()
		
		
		if event.type == pg.MOUSEBUTTONDOWN:
		
			if but_me.isOver(pos):
				#show_text(but_me.get_text(), 50 , 70)
				but_me.change_place(x,y)
				i += 1
			if but_see.isOver(pos):
				#show_text(but_see.get_text(), 120 , 100)
				but_see.change_place(x,y)
				i += 1
			if but_stone.isOver(pos):
				#show_text(but_stone.get_text() , 160, 100)
				but_stone.change_place(x,y)
				i += 1
			if but_rub.isOver(pos):
				but_rub.change_place(x,y)
				i += 1
				
				
		if event.type == pg.MOUSEMOTION:
	
			if but_me.isOver(pos):
				but_me.color = (255,165 ,0)
				but_me.draw(bg, (0,0,0))
			else:
				but_me.color = (176, 224 ,230)
			if but_see.isOver(pos):
				but_see.color = (255,165 ,0)
				but_see.draw(bg, (0,0,0))
			else:
				but_see.color = (176, 224 ,230)
			if but_stone.isOver(pos):
				but_stone.color = (255,165 ,0)
				but_stone.draw(bg, (0,0,0))
			else:
				but_stone.color = (176, 224 ,230)
	
	if i == 3:
		
		#要把所有button消掉
		if but_me.x == x1 and but_me.y == y1 and but_see.x == x2 and but_see.y == y2 and but_stone.x == x3 and but_stone.y == y3:
			show_text(u"爽", 250, 160)
		

screen.blit(bg, (0,0))
pg.display.update()


running = True
while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False	
pg.quit()                