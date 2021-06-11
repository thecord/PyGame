import pygame

pygame.init()

# --- Customisation Windows:
Blue = (10, 10, 40)
white = (255, 255, 255)
width = 1080
length = 720
window = pygame.display.set_mode((width, length))
icon = pygame.image.load("images/snake_icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Wicky Snaky !!")
window.fill((Blue))
# Player --- logic
snake_x = width/2
snake_y = length/2
snake_moveY = 0
snake_moveX = 0
# pygame.draw.rect(window, (0, 255, 255), (snake_x, snake_y, 20, 20))

clock = pygame.time.Clock()

# --- Games loop
GameEnter = True

while GameEnter:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameEnter = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_moveX = -10
                snake_moveY = 0
            elif event.key == pygame.K_RIGHT:
                snake_moveX = 10
                snake_moveY = 0
            elif event.key == pygame.K_UP:
                snake_moveX = 0
                snake_moveY = -10
            elif event.key == pygame.K_DOWN:
                snake_moveX = 0
                snake_moveY = 10
    snake_x += snake_moveX
    snake_y += snake_moveY
    window.fill(Blue)
    pygame.draw.rect(window, white, (snake_x, snake_y, 20, 20))
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()
