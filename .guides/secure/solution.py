import pgzrun
import random

WIDTH = 800
HEIGHT = 600

state = "start"
score = 0

player = Actor('happy')
player.pos = (WIDTH // 2, HEIGHT // 2)

alien = Actor('alien')
alien.pos = (100, 100)

cookie = Actor('cookie')
cookie.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))


def update():
    global state, score

    if state == "start":
        if keyboard.space:
            score = 0
            player.pos = (WIDTH // 2, HEIGHT // 2)
            alien.pos = (100, 100)
            cookie.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
            state = "playing"

    elif state == "playing":
        # Player movement
        if keyboard.left:
            player.x -= 5
        if keyboard.right:
            player.x += 5
        if keyboard.up:
            player.y -= 5
        if keyboard.down:
            player.y += 5

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

        # Caught by alien — game over
        if player.colliderect(alien):
            state = "game_over"

    elif state == "game_over":
        if keyboard.r:
            state = "start"


def draw():
    screen.fill((30, 30, 30))

    if state == "start":
        screen.draw.text("DODGE AND COLLECT",
                         center=(WIDTH // 2, HEIGHT // 2 - 40),
                         fontsize=40, color="white")
        screen.draw.text("Collect cookies. Avoid the alien.",
                         center=(WIDTH // 2, HEIGHT // 2 + 10),
                         fontsize=24, color="white")
        screen.draw.text("Press SPACE to begin",
                         center=(WIDTH // 2, HEIGHT // 2 + 60),
                         fontsize=24, color="yellow")

    elif state == "playing":
        player.draw()
        alien.draw()
        cookie.draw()
        screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")

    elif state == "game_over":
        screen.draw.text("GAME OVER",
                         center=(WIDTH // 2, HEIGHT // 2 - 40),
                         fontsize=50, color="red")
        screen.draw.text(f"Final Score: {score}",
                         center=(WIDTH // 2, HEIGHT // 2 + 20),
                         fontsize=30, color="white")
        screen.draw.text("Press R to play again",
                         center=(WIDTH // 2, HEIGHT // 2 + 70),
                         fontsize=24, color="yellow")


pgzrun.go()
