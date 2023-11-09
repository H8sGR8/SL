import pygame
from sys import exit
import math
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("PONG")
table = pygame.Surface((1000, 600))
table.fill((10, 50, 10))
score = pygame.Surface((1000, 100))
score.fill((50, 50, 50))
font1 = pygame.font.Font(None, 80)
font2 = pygame.font.Font(None, 200)
win = font2.render('WINNER', False, 'White')
win_coll = win.get_rect(center=(500, 300))
lose = font2.render('LOOSER', False, 'White')
lose_coll = lose.get_rect(center=(500, 300))
player = pygame.Surface((20, 100))
player_coll = player.get_rect(center=(960, 300))
player.fill('White')
opponent = pygame.Surface((20, 100))
opponent_coll = opponent.get_rect(center=(40, 300))
opponent.fill('White')
ball = pygame.Surface((20, 20))
ball_coll = ball.get_rect(center=(500, 300))
ball.fill('White')
clock = pygame.time.Clock()
X_movement = 10
Y_movement = 0
p_score = 0
o_score = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(table, (0, 0))
    screen.blit(score, (0, 600))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_coll.top > 0 and (p_score < 5 and o_score < 5):
        player_coll.y -= 4
    if keys[pygame.K_DOWN] and player_coll.bottom < 600 and (p_score < 5 and o_score < 5):
        player_coll.y += 4
    screen.blit(player, player_coll)
    if player_coll.colliderect(ball_coll):
        Y_movement += (ball_coll.bottom - 10 - player_coll.top - 50) / 75
        if Y_movement > 6:
            Y_movement = 6
        elif Y_movement < -6:
            Y_movement = -6
        X_movement = -(math.sqrt(100-Y_movement**2))
    elif opponent_coll.colliderect(ball_coll):
        Y_movement += (ball_coll.bottom - 10 - opponent_coll.top - 50) / 75
        if Y_movement > 6:
            Y_movement = 6
        elif Y_movement < -6:
            Y_movement = -6
        X_movement = (math.sqrt(64 - Y_movement ** 2))
    if ball_coll.bottom > 600 or ball_coll.top < 0:
        Y_movement *= -1
    if ball_coll.left < 0:
        p_score = p_score + 1
        clock.tick(1)
        ball_coll.center = (500, 300)
        player_coll.center = (960, 300)
        opponent_coll.center = (40, 300)
        X_movement = -10
        Y_movement = 0
    if ball_coll.right > 1000:
        o_score = o_score + 1
        clock.tick(1)
        ball_coll.center = (500, 300)
        player_coll.center = (960, 300)
        opponent_coll.center = (40, 300)
        X_movement = 10
        Y_movement = 0
    if p_score < 5 and o_score < 5:
        ball_coll.x += X_movement
        ball_coll.y += Y_movement
    score_text = font1.render(f'{o_score}-{p_score}', False, 'White')
    score_text_coll = score_text.get_rect(center=(500, 650))
    screen.blit(score_text, score_text_coll)
    screen.blit(ball, ball_coll)
    screen.blit(opponent, opponent_coll)
    if ball_coll.top - 30 > opponent_coll.top and opponent_coll.bottom < 600 and (p_score < 5 and o_score < 5):
        opponent_coll.y += 4
    if ball_coll.bottom + 30 < opponent_coll.bottom and opponent_coll.top > 0 and (p_score < 5 and o_score < 5):
        opponent_coll.y -= 4
    if o_score == 5:
        screen.blit(lose, lose_coll)
    elif p_score == 5:
        screen.blit(win, win_coll)
    pygame.display.update()
    clock.tick(60)
