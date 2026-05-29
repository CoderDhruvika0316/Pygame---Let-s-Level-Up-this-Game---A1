import pygame 
import random

s_width, s_height = 800, 600
move_speed = 5
font_size  = 40

pygame.init()

bg_image = pygame.transform.scale(pygame.image.load("White.jpg"), (s_width, s_height))
font = pygame.font.SysFont("Comic Sans MS", font_size)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color("pink"))

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, s_width - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, s_height - self.rect.height), 0)

screen = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Colliding Sprites")

all_sprites = pygame.sprite.Group()

Me_1 = Sprite(pygame.Color("green"), 20, 20)
Me_1.rect.x, Me_1.rect.y = random.randint(0, s_width - Me_1.rect.width), random.randint(0, s_height - Me_1.rect.height)

all_sprites.add(Me_1)

Me_2 = Sprite(pygame.Color("red"), 20, 20)
Me_2.rect.x, Me_2.rect.y = random.randint(0, s_width - Me_2.rect.width), random.randint(0, s_height - Me_2.rect.height)

all_sprites.add(Me_2)

running, won = True, False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.K_DOWN and event.key == pygame.K_x):
            running = False

    if not won:
        key = pygame.key.get_pressed()

        x_change = (key[pygame.K_RIGHT] - key[pygame.K_LEFT]) * move_speed
        y_change = (key[pygame.K_DOWN] - key[pygame.K_UP]) * move_speed

        Me_1.move(x_change, y_change)
        if Me_1.rect.colliderect(Me_2.rect):
            all_sprites.remove(Me_2)

            won = True

    screen.blit(bg_image, (0, 0))
    all_sprites.draw(screen)

    if won:
        win_text = font.render("You kicked out Player 2! Well done!", True, pygame.Color("purple"))
        screen.blit(win_text, ((s_width - win_text.get_width()) // 2, (s_height - win_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()    