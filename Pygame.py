import pygame

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 155,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
CROSS = "x"
NOUGHT = "o"
EMPTY = " "
pygame.init()
pygame.font.init

def provjera_redaka(polje,igrac_na_potezu):
    for redak in range(0,3):
        je_li_redak_pobjeda = True
        for stupac in range(0,3):
            if polje[redak][stupac] != igrac_na_potezu:
                je_li_redak_pobjeda = False
                break
        if je_li_redak_pobjeda:
            return True
    return False

def provjera_stupaca(polje,igrac_na_potezu):
    for stupac in range(0,3):
        stupac_pobjeda = True
        for redak in range(0,3):
            if polje[redak][stupac] != igrac_na_potezu:
                stupac_pobjeda = False
                break
        if stupac_pobjeda:
            return True
    return False


def provjera_dijagonala(polje,igrac_na_potezu):
    pobjeda=True
    for i in range(0, 3):
        if polje[i][i] != igrac_na_potezu:
            pobjeda=False
    if pobjeda:
        return True

    pobjeda=True
    for i in range(0, 3):
        if polje[i ][2-i] != igrac_na_potezu:
            pobjeda=False
    if pobjeda:
        return True
    return False

def provjera_pobjede(polje,igrac_na_potezu):
    return provjera_dijagonala(polje,igrac_na_potezu) or provjera_stupaca(polje,igrac_na_potezu) or provjera_redaka(polje,igrac_na_potezu)

def crt_o(x,y):
    pygame.draw.circle(screen,BLACK,[150*x+75,150*y+75],72,7)
    pygame.display.flip()
def crt_x(x,y):
    k = 5
    pygame.draw.line(screen,BLACK, [150*x+k,150*y+k],[150+150*x-k,150+150*y-k],10)
    pygame.draw.line(screen,BLACK, [x*150+k,150*y+150-k],[150+150*x-k,y*150+k],10)    
    pygame.display.flip()
    
        
    
def crt_polja():
    screen.fill(WHITE)
    pygame.draw.line(screen,BLACK, [150,0],[150,450],5)
    pygame.draw.line(screen,BLACK, [300,0],[300,450],5)
    pygame.draw.line(screen,BLACK, [0,150],[450,150],5)
    pygame.draw.line(screen,BLACK, [0,300],[450,300],5)
 
    pygame.display.flip()

def nalazak(a):
    if a<=150:
        return 0
    if a>=300:
        return 2
    else:
        return 1

   
font = pygame.font.SysFont(None,70)

size = (450, 450)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TicTacToe")

crt_polja()
trenutni = crt_x
trenutni_igrac = CROSS
polja = [[" "," "," "],[" "," "," "],[" "," "," "]]
count = 0
pygame.init()
pygame.font.init

while 1:
    if pygame.mouse.get_pressed()[0] == 1:
        x,y = pygame.mouse.get_pos() 
        stupac = nalazak(x)
        red = nalazak(y)
        
        #print(polja)

        if polja[stupac][red] == EMPTY:
            trenutni(stupac,red)
            count = count+1
            polja[stupac][red] =  trenutni_igrac
            if provjera_pobjede(polja,trenutni_igrac):
                textRect = font.render(trenutni_igrac.upper() + ' JE POBIJEDIO', True, GREEN).get_rect()  
                textRect.center = (225,225) 
                screen.blit(font.render(trenutni_igrac.upper() + ' JE POBIJEDIO', True, GREEN), textRect) 
                pygame.display.update()  
                break
            elif count == 9:
                text = font.render('REMI', True, GREEN) 
                textRect = text.get_rect()  
                textRect.center = (225,225) 
                screen.blit(text, textRect) 
                pygame.display.update()                
            
            if trenutni == crt_x:

                trenutni = crt_o
                trenutni_igrac = NOUGHT
            else:

                
                trenutni = crt_x
                trenutni_igrac = CROSS

        
        
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()



while 1:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            
