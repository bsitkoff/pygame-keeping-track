import pgzrun
import random

WIDTH = 800
HEIGHT = 600

# state controls which screen is shown — "start", "playing", or "game_over"
state = "start"
score = 0

player = Actor('happy')
alien = Actor('alien')
cookie = Actor('cookie')


def reset_game():
    global score
    score = 0
    player.pos = (WIDTH // 2, HEIGHT // 2)
    alien.pos = (100, 100)
    cookie.pos = (300, 300)


def update():
    global state, score

    # Only run game logic when actually playing
    if state != "playing":
        return

    # Player movement
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    # Wrap around screen
    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y > HEIGHT:
        player.y = 0
    if player.y < 0:
        player.y = HEIGHT

    # Alien chases player
    if player.x > alien.x:
        alien.x += 1
    elif player.x < alien.x:
        alien.x -= 1
    if player.y > alien.y:
        alien.y += 1
    elif player.y < alien.y:
        alien.y -= 1

    # Collect cookie — score goes up, cookie moves
    if player.colliderect(cookie):
        score += 1
        cookie.pos = (random.randint(0, WIDTH), random.randint(0, HEIGHT))

    # Caught by alien — game over
    if player.colliderect(alien):
        state = "game_over"


def draw():
    screen.fill((0, 0, 0))

    if state == "start":
        screen.draw.text("DODGE AND COLLECT",
                         center=(WIDTH // 2, HEIGHT // 2 - 40),
                         fontsize=40, color="white")
        screen.draw.text("Collect cookies. Don't get caught.",
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


def on_key_down(key):
    global state

    if state == "start" and key == keys.SPACE:
        reset_game()
        state = "playing"

    elif state == "game_over" and key == keys.R:
        state = "start"


pgzrun.go()
