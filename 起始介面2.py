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
			font = pg.font.Font('C:\\Windows\\Fonts\\kaiu.ttf', 24)
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

def show_text(text, x, y):
	x = x 
	y = y
	font = pg.font.Font('C:\\Windows\\Fonts\\kaiu.ttf', 20)
	text = font.render(text, True, (255,255,255))
	screen.blit(text, (x,y))
	pg.display.update

#起始介面
image = pg.image.load("C:\\Users\\elain\\OneDrive\\Desktop\\商管程式設計\\island.jpg")
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
image2 = pg.image.load("C:\\Users\\elain\\OneDrive\\Desktop\\商管程式設計\\cave.jpg")
image2.convert()
image2 = pg.transform.scale(image2, (620, 520))
bg.blit(image2, (0,0))

screen.blit(bg, (0,0))
pg.display.update()

run2 = True
but_me = Button((176,224,230), 400 , 10, 50 , 40 , u"我")
but_see = Button((176,224,230), 400 , 60, 50 , 40 , u"檢視")
but_stone = Button((176,224,230), 400 , 110, 50 , 40 , u"大石頭")
but_combine = Button((176,224,230), 400 , 160, 50 , 40 , u"大石頭")
but_move = Button((176,224,230), 400 , 210, 50 , 40 , u"大石頭")
'''
but_rub = Button((176,224,230), 400 , 160, 50 , 40 , u"大石頭")
but_room = Button((176,224,230), 400 , 160, 50 , 40 , u"大石頭")
but_table = Button((176,224,230), 400 , 160, 50 , 40 , u"大石頭")
but_bat = Button((176,224,230), 400 , 160, 50 , 40 , u"大石頭")
but_metal = Button((176,224,230), 400 , 160, 50 , 40 , u"大石頭")
'''


while run2:
	show_text(u'"我"在冰冷的地板上醒來，"檢視"四周，發現似乎被關在一個被"大石頭"堵住的"洞穴"裡。',80,50)
	show_text(u'洞穴外傳來，此起彼落的尖叫聲洞穴外傳來，此起彼落的尖叫聲"結合"怒吼。',80,70)
	show_text(u'我"移動到"洞穴口的大石頭旁，從石縫中往外看見一群食人族正在攻擊受傷的同伴，並啃食他們的斷肢，牙齒與骨頭的“摩擦”聲令人毛骨悚然.....',80,90)
	but_me .redraw()
	but_see.redraw()
	but_stone.redraw()
	but_combine.redraw()
	but_move.redraw()
	pg.display.update()
	'''
	for event in pg.event.get():
		pos = pg.mouse.get_pos()
		if event.type == pg.MOUSEBUTTONDOWN:
			
			if button2.isOver(pos):
				show_text(button2.get_text(), 100 , 200)
			if button3.isOver(pos):
				show_text(button3.get_text(), 250 , 200)
			if button4.isOver(pos):
				show_text(button4.get_text() , 400, 200)
			
				
		if event.type == pg.MOUSEMOTION:
	
			if button2.isOver(pos):
				button2.color = (255,165 ,0)
				button2.draw(bg, (0,0,0))
			else:
				button2.color = (176, 224 ,230)
			if button3.isOver(pos):
				button3.color = (255,165 ,0)
				button3.draw(bg, (0,0,0))
			else:
				button3.color = (176, 224 ,230)
			if button4.isOver(pos):
				button4.color = (255,165 ,0)
				button4.draw(bg, (0,0,0))
			else:
				button4.color = (176, 224 ,230)
'''
screen.blit(bg, (0,0))
pg.display.update()

print(button2[text])

running = True
while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
			
pg.quit()                

