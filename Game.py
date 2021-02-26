# pygame template
import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT
import random as rand

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Clicky game")
# ---------------------------
# Initialize global variables

circle_x1 = 200
circle_y1 = 200
circle_x2 = 100
circle_y2 = 100
circle_x3 = 300
circle_y3 = 300
score = 0
rgb1 = (0, 0, 255)
rgb2 = (0, 255, 0)
rgb3 = (255, 0, 0)
missed = False
font_score = pygame.font.SysFont('Arial', 20, True, False)
font_play = pygame.font.SysFont('Arial', 40, True, False)
font_time = pygame.font.SysFont('Arial', 10, True, False)
xoffset = 0
bounce1 = False
bounce2 = False
bounce3 = False
play = False
difficulty = "Easy"
medium = False
hard = False
insane = False
last_played = "easy"
total_clicks = 0
# ---------------------------
pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            positionx, positiony = pygame.mouse.get_pos()
            if play == False:
                if 250 <= positionx <= 390 and 190 <= positiony <= 250 and difficulty == "Easy":
                    play = True
                    xoffset = 0
                if 250 <= positionx <= 390 and 190 <= positiony <= 250 and difficulty == "Medium" and medium:
                    play = True
                    xoffset = 2
                    last_played = "medium"
                if 250 <= positionx <= 390 and 190 <= positiony <= 250 and difficulty == "Hard" and hard:
                    play = True
                    xoffset = 5
                    last_played = "hard"
                if 250 <= positionx <= 390 and 190 <= positiony <= 250 and difficulty == "Insane" and insane:
                    play = True
                    xoffset = 10
                    last_played = "insane"
                elif 220 <= positionx <= 240:
                    if difficulty == "Easy":
                        difficulty = "Insane"
                    elif difficulty == "Insane":
                        difficulty = "Hard"
                    elif difficulty == "Hard":
                        difficulty = "Medium"
                    elif difficulty == "Medium":
                        difficulty = "Easy"
                elif 400 <= positionx <= 420:
                    if difficulty == "Easy":
                        difficulty = "Medium"
                    elif difficulty == "Medium":
                        difficulty = "Hard"
                    elif difficulty == "Hard":
                        difficulty = "Insane"
                    elif difficulty == "Insane":
                        difficulty = "Easy"
            else:
                total_clicks += 1
                if circle_x1-20 <= positionx <= circle_x1+20 and circle_y1-20 <= positiony <= circle_y1+20:
                    score += 1
                    circle_x1,circle_y1 = rand.randrange(20, 610), rand.randrange(40, 450)
                    rgb1 = (rand.randrange(0,254),rand.randrange(0,254),rand.randrange(0,254))
                elif circle_x2-20 <= positionx <= circle_x2+20 and circle_y2-20 <= positiony <= circle_y2+20:
                    score += 1
                    circle_x2,circle_y2 = rand.randrange(20, 610), rand.randrange(40, 450)
                    rgb2 = (rand.randrange(0,254),rand.randrange(0,254),rand.randrange(0,254))
                elif circle_x3-20 <= positionx <= circle_x3+20 and circle_y3-20 <= positiony <= circle_y3+20:
                    score += 1
                    circle_x3,circle_y3 = rand.randrange(20, 610), rand.randrange(40, 450)
                    rgb3 = (rand.randrange(0,254),rand.randrange(0,254),rand.randrange(0,254))
                else:
                    missed = True
    # GAME STATE UPDATES
    # All game math and comparisons happen here
    if circle_x1 + 20 >= 640:
        bounce1 = True
    elif circle_x1 - 20 <= 0:
        bounce1 = False
    if circle_x2 + 20 >= 640:
        bounce2 = True
    elif circle_x2 - 20 <= 0:
        bounce2 = False
    if circle_x3 + 20 >= 640:
        bounce3 = True
    elif circle_x3 - 20 <= 0:
        bounce3 = False
    if bounce1 == False:
        circle_x1 += xoffset
    else:
        circle_x1 -= xoffset
    if bounce2 == False:
        circle_x2 += xoffset
    else:
        circle_x2 -= xoffset
    if bounce3 == False:
        circle_x3 += xoffset
    else:
        circle_x3 -= xoffset
    # DRAWING
    screen.fill((0, 255, 0))  # always the first drawing command
    if play == False:
        pygame.draw.rect(screen, (0,0,0), [250, 190, 140, 60], 1)
        pygame.draw.polygon(screen, (20, 20, 20), [[220, 220], [240, 190], [240, 250]])
        pygame.draw.polygon(screen, (20, 20, 20), [[420, 220], [400, 190], [400, 250]])

        scoretext = font_score.render(f"Last score on {last_played}: {score}", True, (0, 0, 0))
        clicktext = font_score.render(f"Total clicks: {total_clicks}", True, (0, 0, 0))
        screen.blit(scoretext, [0,0])
        screen.blit(clicktext, [0,20])
        if difficulty == "Easy":
            if score >= 10:
                medium = True
            difftext = font_play.render(difficulty, True, (0, 0, 0))
        elif difficulty == "Medium":
            if last_played == "medium" and score >= 10:
                hard = True
            if medium == True:
                difftext = font_play.render(difficulty, True, (0, 0, 0))
            else:
                difftext = font_play.render("Locked", True, (0, 0, 0))
        elif difficulty == "Hard":
            if last_played == "hard" and score >= 10:
                insane = True
            if hard == True:
                difftext = font_play.render(difficulty, True, (0, 0, 0))
            else:
                difftext = font_play.render("Locked", True, (0, 0, 0))
        elif difficulty == "Insane":
            if insane == True:
                difftext = font_play.render(difficulty, True, (0, 0, 0))
            else:
                difftext = font_play.render("Locked", True, (0, 0, 0))
        screen.blit(difftext, [260, 200])
        seconds = 0
        nextiter = False
        circle_x1 = 200
        circle_y1 = 200
        circle_x2 = 100
        circle_y2 = 100
        circle_x3 = 300
        circle_y3 = 300        
    else:
        if nextiter == False:
            score = 0
            total_clicks = 0
            nextiter = True
        seconds += 1/60
        screen.fill((255, 255, 255))
        text = font_score.render(str(score), True, (0, 0, 0))
        time_text = font_time.render(f"Time left: {10-int(seconds)}", True, (0, 0, 0))
        screen.blit(text, [318, 0])
        screen.blit(time_text, [590, 0])
        pygame.draw.circle(screen, rgb1, (circle_x1, circle_y1), 20)
        pygame.draw.circle(screen, rgb2, (circle_x2, circle_y2), 20)
        pygame.draw.circle(screen, rgb3, (circle_x3, circle_y3), 20)
        if missed == True:
            screen.fill((255,0,0))
            missed = False
        if seconds > 10:
            play = False
    # Must be the last two lines
    # of the game loop

    pygame.display.flip()
    clock.tick(60)
    #---------------------------


pygame.quit()
