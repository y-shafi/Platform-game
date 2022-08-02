import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'{current_time}', False, ('dark green') )
    score_rect = score_surf.get_rect(center = (400, 60))
    display.blit(score_surf, score_rect) 
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

        if obstacle_rect.bottom == 300:
            display.blit(snail_surf,obstacle_rect)
        else:
            display.blit(fly_surf,obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []

pygame.init()

display = pygame.display.set_mode((800,450))
pygame.display.set_caption("Mario Bros remix")
clock = pygame.time.Clock()
test_font = pygame.font.Font('spritesheet/font/dpcomic.ttf',50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('spritesheet/texture/sky.png').convert_alpha()
ground_surface = pygame.image.load('spritesheet/texture/ground.png').convert_alpha()

# score_surf = test_font.render('100', False,'Dark Green', )
# score_rect =  score_surf.get_rect(center  = (400,60))

# enemie obstacles
snail_surf = pygame.image.load('spritesheet/enemies/snail1.png').convert_alpha()
# enemie1_rect = enemie1_surf.get_rect(topright = (780, 224))
fly_surf = pygame.image.load('spritesheet/enemies/fly1.png').convert_alpha()

obstacle_rect_list = []


player1_surf = pygame.image.load('spritesheet/players/jameela/jam2frm1.png').convert_alpha()
player1_rect = player1_surf.get_rect(topleft = (80, 252))
player1_gravity = 0

# intro screen
player1_stand = pygame.image.load('spritesheet/players/jameela/jameela2STANDING.png').convert_alpha()
player1_stand = pygame.transform.rotozoom(player1_stand, 0,1 )
player1_stand_rect = player1_stand.get_rect(center = (400, 225))

game_name = test_font.render('Khalisa Quest Runner',False, ('#012d3d'))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press The Space Bar To Run',False,('#012d3d'))
game_message_rect = game_message.get_rect(center = (400,390))

# timer
obstacle_timer =  pygame.USEREVENT + 1 
pygame.time.set_timer(obstacle_timer, 1700)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.QUIT()
            exit()
        if game_active: 
                # mouse motion 
            if event.type == pygame.MOUSEBUTTONDOWN:  
                if player1_rect.collidepoint(event.pos) and player1_rect.bottom >= 300:
                    player1_gravity = -20

                # key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player1_rect.bottom >= 300:
                    player1_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                
                start_time = int(pygame.time.get_ticks() / 1000) 

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100), 300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100), 210 )))

    if game_active: 
        display.blit(sky_surface,(0,0))
        display.blit(ground_surface,(0,300))
        # pygame.draw.rect(display,'lime green ', score_rect)
        # pygame.draw.rect(display,'lime green', score_rect, 10)
        # display.blit(score_surf,score_rect)
        score = display_score()

        # # enemie1
        # enemie1_rect.x -= 3
        # if enemie1_rect.right <=  0: enemie1_rect.left  = 800
        # display.blit(enemie1_surf,enemie1_rect,) 

        # Player
        player1_gravity += 1  
        player1_rect.y += player1_gravity  
        if player1_rect.bottom >= 300: player1_rect.bottom = 300  
        display.blit(player1_surf,player1_rect)

        # enemie obstacle movements
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision
    else:
        display.fill((94,129,162))
        display.blit(player1_stand , player1_stand_rect)

        score_message = test_font.render(f'Your Score: {score}',False,('#012d3d'))
        score_message_rect = score_message.get_rect(center = (400, 340))

        if score == 0:
            display.blit(game_message,game_message_rect)
        else:
            display.blit(score_message,score_message_rect)

        display.blit(game_name, game_name_rect)
        display.blit(game_message, game_message_rect)


    pygame.display.update()
    clock.tick(60) 

    # obstacle stuff stuck refer to YouTube vid @ 2:31:05