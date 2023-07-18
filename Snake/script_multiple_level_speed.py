import pygame
import time
import random
 
# Window size
window_x = 720
window_y = 480

# defining colors
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)  # defining green color
 
pygame.init()
 
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# Font settings
score_font = pygame.font.Font(None, 35)
 
clock = pygame.time.Clock()
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0
level = 1
snake_speed = 15  # Base speed
 
def game_over():
    pygame.quit()
    quit()

def score_display(score, level):
    score_text = score_font.render('Score: ' + str(score) + ' Level: ' + str(level), True, white)
    game_window.blit(score_text, [0, 0])

while True:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
 
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_UP]:
                change_to = 'UP'
            if keys[pygame.K_DOWN]:
                change_to = 'DOWN'
            if keys[pygame.K_LEFT]:
                change_to = 'LEFT'
            if keys[pygame.K_RIGHT]:
                change_to = 'RIGHT'
            if keys[pygame.K_SPACE]:  # Added speed control
                snake_speed = 25 if snake_speed == 15 else 15
 
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
     
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
     
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
 
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    if score >= 300 * level:  # Level up every 300 points
        level += 1
        if level > 10:  # Maximum level is 10
            game_over()

    score_display(score, level)

    pygame.display.update()

    clock.tick(snake_speed)
