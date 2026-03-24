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


def update():
    global score  # TODO: Add state here too once you create a state variable

    # TODO: Use if/elif to check the state and run different code for each:

    # When state is "start":
    #   Wait for SPACE, then reset positions and switch to "playing"

    # When state is "playing":
    #   Move the player
    #   Move the enemy
    #   Detect collectible pickup and update score
    #   Detect enemy collision and switch to game over

    # When state is "game_over":
    #   Wait for R, then switch back to "start"

    pass  # Remove this line once you add your if/elif


def draw():
    screen.fill((30, 30, 30))

    # TODO: Draw different things depending on the current state
    # "start" — show a title and "Press SPACE to begin"
    # "playing" — draw player, enemies, collectibles, and the score
    # "game_over" — show final score and "Press R to restart"

    player.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")


pgzrun.go()
