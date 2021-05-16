#import library
import pygame,random,time,sys
pygame.init()

#Create Cua So game
gameSurface= pygame.display.set_mode((735,475))
pygame.display.set_caption('Magic Human')

#Load hình ảnh
m=40 #kich thuoc anh
Img_human = pygame.transform.scale(pygame.image.load('D:\STUDY\[Lý Thuyết]-KTpython\human.png'),(m,m))
Img_bot = pygame.transform.scale(pygame.image.load('D:\STUDY\[Lý Thuyết]-KTpython\Bot.png'),(m,m))
#Color
red = pygame.Color(255,0,0)
blue = pygame.Color(65,105,255)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
gray = pygame.Color(128,128,128)
#Khai bao bien
humanpos= [100,60] #vi tri xuat hien
direction = 'RIGHT'
changeto = direction
score=0
#Ham tao vi tri bot
def Pos():
    botx= random.randrange(1,71) #random vi x
    boty= random.randrange(1,45)
    if botx % 2 != 0: botx += 1
    if boty % 2 != 0: boty += 1
    botpos = [botx * 10, boty * 10]
    return botpos
botx= random.randrange(1,71) #random vi x
boty= random.randrange(1,45)
if botx % 2 != 0: botx += 1
if boty % 2 != 0: boty += 1
botpos = [botx * 10, boty * 10]
# hàm gameover
def game_over():
    gfont = pygame.font.SysFont('consolas',40)
    gsurf = gfont.render('Game over!',True,red)
    grect = gsurf.get_rect()
    grect.midtop = (360,150)
    gameSurface.blit(gsurf,grect)
    show_score(0)
    pygame.display.flip()
    time.sleep(5) #time wait to exit
    pygame.quit()
    sys.exit()
# hàm show_score
def show_score(choice = 1):
    sfont = pygame.font.SysFont('consolas',20)
    ssurf = sfont.render('Score: {0}'.format(score),True,black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (70,20)
    else:
        srect.midtop = (360,230)
    gameSurface.blit(ssurf,srect)
#Create VOng lap game
while True:
    pygame.time.delay(200) #tốc độ chơi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    #Xử lý phím bấm:
    if event.type == pygame.KEYDOWN:
        if event.type == pygame.K_LEFT:
            changeto= 'LEFT'
        if event.type == pygame.K_RIGHT:
            changeto='RIGHT'
        if event.type == pygame.K_UP:
            changeto='UP'
        if event.type == pygame.K_DOWN:
            changeto='DOWN'
        if event.type == pygame.K_ESCAPE:
            pygame.event.post(pygame.evet.Event(pygame.QUIT))
    #Huong di
    if changeto== 'RIGHT' and not direction=='LEFT':
        direction= 'RIGHT'
    if changeto== 'LEFT' and not direction=='RIGHT':
        direction= 'LEFT'
    if changeto== 'UP' and not direction=='DOWN':
        direction= 'UP'
    if changeto== 'DOWN' and not direction=='UP':
        direction= 'DOWN'
    #Cap nhat vi tri moi
    if direction == 'RIGHT':
        humanpos[0] += m
    if direction == 'LEFT':
        humanpos[0] -= m
    if direction == 'UP':
        humanpos[1] -= m
    if direction == 'DOWN':
        humanpos[1] += m
    #Cap nhat di chuyen
    gameSurface.fill(white)
    for i in Pos():
        gameSurface.blit(Img_human,pygame.Rect(humanpos[0],humanpos[1],m,m))
        #gameSurface.blit(Img_human,pygame.Rect(Pos()[0],Pos()[1],m,m))
    pygame.display.flip()