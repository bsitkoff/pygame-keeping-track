import pgzrun

WIDTH = 400
HEIGHT = 300

score = 0

player = Actor('happy')
player.pos = (200, 150)

cookie = Actor('cookie')
cookie.pos = (100, 100)


def update():
    # BUG: This will crash! Python thinks score is a local variable
    # because we assign to it, but we never declared it locally.
    if player.colliderect(cookie):
        score += 1
        cookie.x += 80


def draw():
    screen.fill((0, 0, 0))
    player.draw()
    cookie.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")


pgzrun.go()
