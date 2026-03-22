import pgzrun

WIDTH = 600
HEIGHT = 400


def draw():
    screen.fill((30, 30, 30))

    # Basic text — position is the top-left corner
    screen.draw.text("Hello!", (10, 10), fontsize=30, color="white")

    # Centered text — center= puts the middle of the text at that point
    screen.draw.text("Centered Text",
                     center=(WIDTH // 2, 100),
                     fontsize=40, color="yellow")

    # Different colors — named colors
    screen.draw.text("Red text", (10, 160), fontsize=28, color="red")
    screen.draw.text("Cyan text", (10, 200), fontsize=28, color="cyan")

    # RGB tuple colors — (red, green, blue) each 0–255
    screen.draw.text("Orange (RGB)", (10, 240), fontsize=28, color=(255, 140, 0))
    screen.draw.text("Purple (RGB)", (10, 280), fontsize=28, color=(180, 60, 255))

    # Different sizes
    screen.draw.text("Small", (350, 160), fontsize=18, color="white")
    screen.draw.text("Medium", (350, 190), fontsize=30, color="white")
    screen.draw.text("BIG", (350, 230), fontsize=50, color="white")

    # Showing a score variable
    score = 42
    screen.draw.text(f"Score: {score}", (350, 310), fontsize=30, color="white")


pgzrun.go()
