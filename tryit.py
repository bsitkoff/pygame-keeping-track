import pgzrun
import random

WIDTH = 800
HEIGHT = 600

score = 0

player = Actor('happy')
player.pos = (WIDTH // 2, HEIGHT // 2)

alien = Actor('alien')
alien.pos = (100, 100)

cookie = Actor('cookie')
cookie.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

def update():
    global score

    if keyboard.left:
        player.x -= 4
    if keyboard.right:
        player.x += 4
    if keyboard.up:
        player.y -= 4
    if keyboard.down:
        player.y += 4

    # Keep player on screen
    player.x = max(0, min(WIDTH, player.x))
    player.y = max(0, min(HEIGHT, player.y))

    # Alien chases player
    if alien.x < player.x:
        alien.x += 1
    elif alien.x > player.x:
        alien.x -= 1
    if alien.y < player.y:
        alien.y += 1
    elif alien.y > player.y:
        alien.y -= 1

    # Collect cookie
    if player.colliderect(cookie):
        score += 1
        cookie.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))

    # TODO: detect collision with alien and change state to "game_over"

def draw():
    screen.fill((0, 0, 0))
    player.draw()
    alien.draw()
    cookie.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=24, color="white")

pgzrun.go()
