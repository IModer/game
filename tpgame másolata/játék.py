import pygame
#Init

pygame.init()
WINDOW_SIZE = (700,500)
screen = pygame.display.set_mode(WINDOW_SIZE)
display = pygame.Surface((300,200))
pygame.display.set_caption("First Game")

#Pálya

game_map = [['2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','2'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

#Spriteok

player = pygame.image.load('./sp/player.png')
grass_img = pygame.image.load('./sp/grass.png')
dirt_img = pygame.image.load('./sp/dirt.png')

#Változók

isJump = False
jumpCount = 10
vel = 5
run = True

while run:
    y = 0
    #pygame.time.delay(25)
    
    display.fill((153,217,234)) 
    
    #Pálya betöltése

    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_img,(x*16,y*16))
            if tile == '2':
                display.blit(grass_img,(x*16,y*16))
            x += 1
        y += 1

    #Kilépés

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Irányítás

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if not(isJump):
        if keys[pygame.K_DOWN]:
            y += vel   
        if keys[pygame.K_UP]: 
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.3 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    screen.blit(player, (x+50, y))
    pygame.display.update()

    

pygame.quit()
