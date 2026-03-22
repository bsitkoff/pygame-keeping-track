import pgzrun
import random

WIDTH = 800
HEIGHT = 600

# TODO: Create a state variable to control which screen is shown
# Hint: use "start", "playing", and "game_over" as your three states

score = 0

player = Actor('happy')
player.pos = (WIDTH // 2, HEIGHT // 2)

# TODO: Create at least one enemy and one collectible using Actor()


def reset_game():
    global score
    score = 0
    player.pos = (WIDTH // 2, HEIGHT // 2)
    # TODO: Reset enemy and collectible positions too


def update():
    global score
    # TODO: Only run game logic when state is "playing"

    # Player movement
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        player.y -= 5
    if keyboard.down:
        player.y += 5

    # TODO: Add enemy movement

    # TODO: Detect collectible pickup and update score

    # TODO: Detect enemy collision and switch to game over state


def draw():
    screen.fill((0, 0, 0))

    # TODO: Draw different things depending on the current state
    # "start" — show a title and "Press SPACE to begin"
    # "playing" — draw player, enemies, collectibles, and the score
    # "game_over" — show final score and "Press R to restart"

    player.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")


def on_key_down(key):
    pass
    # TODO: Handle keypresses to change between states
    # SPACE on start screen -> playing
    # R on game over screen -> start


pgzrun.go()
