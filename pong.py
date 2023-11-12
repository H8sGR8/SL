"""
PONG amazing game
"""

import pygame
from sys import exit
import math


def create_surf(width, height, color, hit_box, cords):
    """
    Creating surfaces that will be on the screen
    To use get_rect hit_box need to be True
    """
    surf = pygame.Surface((width, height))
    surf.fill(color)
    if hit_box:
        surf_hit_box = surf.get_rect(center=cords)
        return surf, surf_hit_box
    return surf


def create_text(content, color, font, cords):
    """
    Creating texts that will be on the screen
    font = 1 for font1 or 2 for font2 or 3 for font3
    """
    if font == 1:
        text = font1.render(content, True, color)
        text_hit_box = text.get_rect(center=cords)
        return text, text_hit_box
    elif font == 2:
        text = font2.render(content, True, color)
        text_hit_box = text.get_rect(center=cords)
        return text, text_hit_box
    elif font == 3:
        text = font3.render(content, True, color)
        text_hit_box = text.get_rect(center=cords)
        return text, text_hit_box


def restart_game():
    """
    Resetting a game to starting point
    """
    ball_hit_box.center = (500, 300)
    player_hit_box.center = (960, 300)
    opponent_hit_box.center = (40, 300)


def player_movement(key):
    """
    Moving player by pressing arrow up and down
    key = key pressed
    """

    if key[pygame.K_UP] and player_hit_box.top > 0 and (p_score < 5 and o_score < 5):
        return -5
    if key[pygame.K_DOWN] and player_hit_box.bottom < 600 and (p_score < 5 and o_score < 5):
        return 5
    else:
        return 0


def set_ball_movement(x, y):
    """
    Changing an angle of ball's velocity after a contact with player or opponent
    Farther from center the ball hits higher the Y velocity (max 6)
    Whole velocity is allways 10
    x, y = ball's velocities
    """
    if player_hit_box.colliderect(ball_hit_box):
        y += (ball_hit_box.bottom - 10 - player_hit_box.top - 50) / 50
        if y > 6:
            y = 6
        elif y < -6:
            y = -6
        x = -(math.sqrt(100 - y ** 2))
    elif opponent_hit_box.colliderect(ball_hit_box):
        y += (ball_hit_box.bottom - 10 - opponent_hit_box.top - 50) / 50
        if y > 6:
            y = 6
        elif y < -6:
            y = -6
        x = (math.sqrt(100 - y ** 2))
    return x, y


def wall_bounce(y):
    """
    After hitting a top or bottom wall bouncing off with the same angle
    y = ball's Y velocity
    """
    if ball_hit_box.bottom > 600 or ball_hit_box.top < 0:
        return -y
    return y


def ball_movement(x, y):
    """
    Changing position of a ball using date from previous functions
    x, y = exact ball's cords
    """
    if p_score < 5 and o_score < 5:
        x += X_movement
        y += Y_movement
    return x, y


def point_counter(p_s, o_s, x, y):
    """
    After hitting left or right wall giving points to player or to opponent
    Resetting game to starting point using function
    o_s, p_s = places for scores
    x, y ball's velocities
    """
    if ball_hit_box.left < 0:
        p_s = p_s + 1
        clock.tick(1)
        restart_game()
        x = -10
        y = 0
    if ball_hit_box.right > 1000:
        o_s = o_s + 1
        clock.tick(1)
        restart_game()
        x = 10
        y = 0
    return p_s, o_s, x, y


def opponent_movement(y, key, p):
    """
    Moving opponent by forcing it to follow a ball when Y position goes 20px away from center
    While ball has low Y velocity opponent will also reduce it not to glitch
    y = ball's Y velocity
    p = choosing between playing against AI or another player
    """
    move = 0
    if p:
        if key[pygame.K_w] and opponent_hit_box.top > 0 and (p_score < 5 and o_score < 5):
            move = -5
        if key[pygame.K_s] and opponent_hit_box.bottom < 600 and (p_score < 5 and o_score < 5):
            move = 5
    else:
        if (ball_hit_box.top - 30 < opponent_hit_box.top and
                opponent_hit_box.top > 0 and (p_score < 5 and o_score < 5)):
            if 0 > ball_hit_box.top - 30 - opponent_hit_box.top > -5 and abs(y) < 4:
                move = ball_hit_box.top - 30 - opponent_hit_box.top
            else:
                move = -5
        if (ball_hit_box.bottom + 30 > opponent_hit_box.bottom and
                opponent_hit_box.bottom < 600 and (p_score < 5 and o_score < 5)):
            if 5 > ball_hit_box.bottom + 30 - opponent_hit_box.bottom > 0 and abs(y) < 4:
                move = ball_hit_box.bottom + 30 - opponent_hit_box.bottom
            else:
                move = 5
    return move


def show(g):
    """
    Showing  all essential graphics to the game
    g = changing game status on false to restart whole game and choose game mode again
    """
    if o_score < 5 and p_score < 5:
        screen.blit(player, player_hit_box)
        screen.blit(opponent, opponent_hit_box)
        screen.blit(ball, ball_hit_box)
    score_text, score_text_hit_box = create_text(f'{o_score}-{p_score}', 'White', 1, (500, 650))
    screen.blit(score_text, score_text_hit_box)
    if o_score == 5 and not player2:
        screen.blit(lose, lose_hit_box)
        pygame.display.update()
        clock.tick(0.25)
        g = False
    elif p_score == 5 and not player2:
        screen.blit(win, win_hit_box)
        pygame.display.update()
        g = False
        clock.tick(0.25)
    elif o_score == 5 and player2:
        screen.blit(left_player, left_player_hit_box)
        pygame.display.update()
        clock.tick(0.25)
        g = False
    elif p_score == 5 and player2:
        screen.blit(right_player, right_player_hit_box)
        pygame.display.update()
        g = False
        clock.tick(0.25)
    return g


def event_game(key):
    """
    Quiting a game by clicking X in right corner of pressing escape on keyboard
    Showing and hiding cursor during a game
    key = key pressed
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
        if game and pygame.mouse.get_pressed() == (True, False, False):
            if pygame.mouse.get_visible() == 0:
                pygame.mouse.set_visible(1)
            else:
                pygame.mouse.set_visible(0)


def choose_game_mode(p, g):
    """
    Choosing between PvP and PvE mode
    changing colors of buttons when cursor is on them
    Starting game
    p = False to PvE mode and True for PvP mode
    """
    button1.fill((150, 150, 150))
    button2.fill((150, 150, 150))
    color1 = (50, 50, 50)
    color2 = (30, 30, 30)
    pvp, pvp_hit_box = create_text('PvP', color1, 1, (300, 300))
    pve, pve_hit_box = create_text('PvE', color1, 1, (700, 300))
    pygame.mouse.set_visible(1)
    mouse_pos = pygame.mouse.get_pos()
    if button1_hit_box.collidepoint(mouse_pos):
        button1.fill((100, 100, 100))
        pvp, pvp_hit_box = create_text('PvP', color2, 1, (300, 300))
        if pygame.mouse.get_pressed() == (True, False, False):
            pygame.mouse.set_visible(0)
            clock.tick(4)
            p = True
            g = True
    elif button2_hit_box.collidepoint(mouse_pos):
        button2.fill((100, 100, 100))
        pve, pve_hit_box = create_text('PvE', color2, 1, (700, 300))
        if pygame.mouse.get_pressed() == (True, False, False):
            pygame.mouse.set_visible(0)
            clock.tick(4)
            p = False
            g = True
    screen.blit(button1, button1_hit_box)
    screen.blit(pvp, pvp_hit_box)
    screen.blit(button2, button2_hit_box)
    screen.blit(pve, pve_hit_box)
    return p, g


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("PONG")
    X_movement,  Y_movement, p_score, o_score, game, player2 = 10, 0, 0, 0, False, False
    button1, button1_hit_box = create_surf(200, 100, (150, 150, 150), True, (300, 300))
    button2, button2_hit_box = create_surf(200, 100, (150, 150, 150), True, (700, 300))
    table = create_surf(1000, 600, (10, 50, 10), False, None)
    score = create_surf(1000, 100, (50, 50, 50), False, None)
    player, player_hit_box = create_surf(20, 100, 'White', True, (960, 300))
    opponent, opponent_hit_box = create_surf(20, 100, 'White', True, (40, 300))
    ball, ball_hit_box = create_surf(20, 20, 'White', True, (500, 300))
    font1 = pygame.font.Font(None, 80)
    font2 = pygame.font.Font(None, 200)
    font3 = pygame.font.Font(None, 120)
    win, win_hit_box = create_text('WINNER', 'White', 2, (500, 300))
    lose, lose_hit_box = create_text('LOOSER', 'White', 2, (500, 300))
    left_player, left_player_hit_box = create_text('LEFT PLAYER WON', 'White', 3, (500, 300))
    right_player, right_player_hit_box = create_text('RIGHT PLAYER WON', 'White', 3, (500, 300))
    clock = pygame.time.Clock()
    while True:
        keys = pygame.key.get_pressed()
        screen.blit(table, (0, 0))
        screen.blit(score, (0, 600))
        event_game(keys)
        if game:
            player_hit_box.y += player_movement(keys)
            p_score, o_score, X_movement, Y_movement = point_counter(p_score, o_score, X_movement, Y_movement)
            X_movement, Y_movement = set_ball_movement(X_movement, Y_movement)
            Y_movement = wall_bounce(Y_movement)
            ball_hit_box.x, ball_hit_box.y = ball_movement(ball_hit_box.x, ball_hit_box.y)
            opponent_hit_box.y += opponent_movement(Y_movement, keys, player2)
            game = show(game)
        else:
            X_movement,  Y_movement, p_score, o_score = 10, 0, 0, 0
            player2, game = choose_game_mode(player2, game)
        pygame.display.update()
        clock.tick(60)
        
