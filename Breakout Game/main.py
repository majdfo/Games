# breakout game - timer, lives, power-ups, and sounds
import pygame
import random
from pygame.locals import *

pygame.init()

# load sound effects
life_gain_sound = pygame.mixer.Sound('gain_life.mp3')
win_sound = pygame.mixer.Sound('win.mp3')
life_lose_sound = pygame.mixer.Sound('lose_life.mp3')
life_lose_final_sound = pygame.mixer.Sound('lose_life_final.mp3')
paddle_hit_sound = pygame.mixer.Sound('paddle_hit.mp3')
block_break_sound = pygame.mixer.Sound('paddle_hit.mp3')  # reused for block breaking

# game window setup
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('breakout - بريك أوت')

# load heart image and scale
heart_img = pygame.image.load('heart.png')
heart_img = pygame.transform.scale(heart_img, (25, 25))

# colors and font
font = pygame.font.SysFont('arial', 24)
bg = (234, 218, 184)
block_orange = (255, 165, 0)
block_light_red = (255, 102, 102)
paddle_col = (142, 135, 123)
paddle_outline = (100, 100, 100)
text_col = (78, 81, 139)

# game variables
cols = 6
rows = 4
clock = pygame.time.Clock()
fps = 60
live_ball = False
game_over = 0
lives = 3
total_time = 0
start_time = 0

# lives display
heart_spacing = 10
heart_x_start = 10
heart_y = 10

# power-up storage
power_ups = []

# power-up class (hearts only)
class PowerUp:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 25, 25)
        self.speed = 3
        self.image = heart_img

    def move(self):
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# wall of blocks
class wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 35

    def create_wall(self):
        self.blocks = []
        for row in range(rows):
            block_row = []
            for col in range(cols):
                block_x = col * self.width
                block_y = row * self.height + 50
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                strength = 2 if row < 2 else 1  # top 2 rows are harder
                block_row.append([rect, strength])
            self.blocks.append(block_row)

    def draw_wall(self):
        for row in self.blocks:
            for block in row:
                if block[1] > 0:
                    block_col = block_light_red if block[1] == 1 else block_orange
                    pygame.draw.rect(screen, block_col, block[0])
                    pygame.draw.rect(screen, bg, block[0], 2)

# paddle
class paddle():
    def __init__(self):
        self.reset()

    def move(self):
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1

    def draw(self):
        pygame.draw.rect(screen, paddle_col, self.rect)
        pygame.draw.rect(screen, paddle_outline, self.rect, 3)

    def reset(self):
        self.height = 20
        self.width = int(screen_width / cols)
        self.x = int((screen_width / 2) - (self.width / 2))
        self.y = screen_height - (self.height * 2)
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0

# ball class
class game_ball():
    def __init__(self, x, y):
        self.reset(x, y)

    def move(self):
        collision_thresh = 5
        wall_destroyed = 1
        row_count = 0
        for row in wall.blocks:
            item_count = 0
            for item in row:
                if self.rect.colliderect(item[0]) and item[1] > 0:
                    block_break_sound.play()
                    if abs(self.rect.bottom - item[0].top) < collision_thresh and self.speed_y > 0:
                        self.speed_y *= -1
                    elif abs(self.rect.top - item[0].bottom) < collision_thresh and self.speed_y < 0:
                        self.speed_y *= -1
                    elif abs(self.rect.right - item[0].left) < collision_thresh and self.speed_x > 0:
                        self.speed_x *= -1
                    elif abs(self.rect.left - item[0].right) < collision_thresh and self.speed_x < 0:
                        self.speed_x *= -1
                    if item[1] > 1:
                        wall.blocks[row_count][item_count][1] -= 1
                    else:
                        if random.random() < 0.2:
                            power_ups.append(PowerUp(item[0].x, item[0].y))
                        wall.blocks[row_count][item_count][1] = 0
                if wall.blocks[row_count][item_count][1] != 0:
                    wall_destroyed = 0
                item_count += 1
            row_count += 1

        if wall_destroyed:
            self.game_over = 1

        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.game_over = -1

        if self.rect.colliderect(player_paddle):
            paddle_hit_sound.play()
            if abs(self.rect.bottom - player_paddle.rect.top) < collision_thresh and self.speed_y > 0:
                self.speed_y *= -1
                self.speed_x += player_paddle.direction
                self.speed_x = max(-self.speed_max, min(self.speed_x, self.speed_max))
            else:
                self.speed_x *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over

    def draw(self):
        pygame.draw.circle(screen, paddle_col, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
        pygame.draw.circle(screen, paddle_outline, (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3)

    def reset(self, x, y):
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = 4
        self.speed_y = -4
        self.speed_max = 5
        self.game_over = 0

# draw text to screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# draw remaining lives (hearts)
def draw_lives(lives):
    for i in range(lives):
        x = heart_x_start + i * (heart_img.get_width() + heart_spacing)
        screen.blit(heart_img, (x, heart_y))

# draw timer (mm:ss)
def draw_timer():
    elapsed_seconds = total_time
    if live_ball:
        current_time = pygame.time.get_ticks()
        elapsed_seconds += (current_time - start_time) // 1000
    minutes = elapsed_seconds // 60
    seconds = elapsed_seconds % 60
    timer_text = f"{minutes:02}:{seconds:02}"
    text_surface = font.render(timer_text, True, text_col)
    text_rect = text_surface.get_rect(topright=(screen_width - 10, 15))
    screen.blit(text_surface, text_rect)

# game setup
wall = wall()
wall.create_wall()
player_paddle = paddle()
ball = game_ball(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)

# main loop
run = True
while run:
    clock.tick(fps)
    screen.fill(bg)

    draw_lives(lives)
    draw_timer()
    wall.draw_wall()
    player_paddle.draw()
    ball.draw()

    for power in power_ups[:]:
        power.move()
        power.draw()
        if power.rect.colliderect(player_paddle.rect):
            life_gain_sound.play()
            if lives < 3:
                lives += 1
            power_ups.remove(power)
        elif power.rect.top > screen_height:
            power_ups.remove(power)

    if live_ball:
        player_paddle.move()
        game_over = ball.move()
        if game_over != 0:
            live_ball = False
            current_time = pygame.time.get_ticks()
            total_time += (current_time - start_time) // 1000
            if game_over == -1:
                lives -= 1
                if lives == 0:
                    life_lose_final_sound.play()
                else:
                    life_lose_sound.play()
                if lives <= 0:
                    draw_text(f'game over! time: {total_time}s', font, text_col, 150, screen_height // 2 + 50)
                else:
                    ball.reset(player_paddle.x + (player_paddle.width // 2), player_paddle.y - player_paddle.height)
                    player_paddle.reset()
            elif game_over == 1:
                win_sound.play()
                draw_text('you won!', font, text_col, 240, screen_height // 2 + 50)

    if not live_ball:
        if lives > 0 and game_over != 1:
            draw_text('click to start', font, text_col, 200, screen_height // 2 + 100)
        elif lives <= 0:
            draw_text(f'game over! total time: {total_time}s', font, text_col, 150, screen_height // 2 + 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not live_ball:
            if lives <= 0 or game_over == 1:
                wall.create_wall()
                lives = 3
                total_time = 0
                power_ups.clear()
                game_over = 0
            start_time = pygame.time.get_ticks()
            live_ball = True
            player_paddle.reset()

    pygame.display.update()

pygame.quit()
