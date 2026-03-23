import pgzrun

WIDTH = 400
HEIGHT = 300

score = 0

player = Actor('happy')
player.pos = (200, 150)

cookie = Actor('cookie')
cookie.pos = (100, 100)


def update():
    # Player movement
    if keyboard.left:
        player.x -= 4
    if keyboard.right:
        player.x += 4
    if keyboard.up:
        player.y -= 4
    if keyboard.down:
        player.y += 4

    # BUG: This will crash! Python thinks score is a local variable
    # because we assign to it, but we never declared it locally.
    if player.colliderect(cookie):
        score += 1
        cookie.x += 80


def draw():
    screen.fill((30, 30, 30))
    player.draw()
    cookie.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")


pgzrun.go()
