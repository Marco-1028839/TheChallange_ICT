import pygame
import time
pygame.init()

screen = pygame.display.set_mode((0,0),pygame.RESIZABLE)
clock = pygame.time.Clock()

code = "021-420-069"

user_input = "***-***-***"

def text_objects(text,font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def message_display(text,x,y,w,h):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(TextSurf, TextRect)
def check_code_valid():
    for char in user_input:
        if char == "*":
            return 0
        else:
            if user_input == code:
                return 1
    return 2


def change_user_input(number):
    global user_input
    string = list(user_input)
    for index, char in enumerate(string):
        if char == "*":
            string[index] = str(number)
            break
    result = "".join(string)
    user_input = result

def button(msg,x,y,w,h,ic,ac,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0]==1:
            change_user_input(action)
            time.sleep(0.5)
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    screen.blit(textSurf, textRect)
    

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.FINGERDOWN:
            print("Finger touched the screen")
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        running = False
    
    ic1 = (5, 162, 230)
    ic2 = (5, 230, 69)
    ac = (245, 0, 20)
    
    screen.fill((54,53,53))
    button("0",0,300,78,78,ic1,ac,"0")
    button("1",80,300,78,78,ic2,ac,"1")
    button("2",158,300,78,78,ic1,ac,"2")
    button("3",236,300,78,78,ic2,ac,"3")
    button("4",314,300,78,78,ic1,ac,"4")
    button("5",392,300,78,78,ic2,ac,"5")
    button("6",470,300,78,78,ic1,ac,"6")
    button("7",548,300,78,78,ic2,ac,"7")
    button("8",626,300,78,78,ic1,ac,"8")
    button("9",706,300,78,78,ic2,ac,"9")
    
    
    if user_input == "correct":
        time.sleep(10)
        user_input = "***-***-***"
    
    result = check_code_valid()
    if result == 1:
        user_input = "correct"
    elif result == 2: 
        user_input = "***-***-***"
    
    message_display(user_input,200,0,300,300)
    
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()