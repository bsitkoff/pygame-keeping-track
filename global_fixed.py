import pgzrun

WIDTH = 400
HEIGHT = 300

score = 0

player = Actor('happy')
player.pos = (200, 150)

cookie = Actor('cookie')
cookie.pos = (100, 100)


def update():
    global score  # FIX: tells Python we mean the variable defined at the top

    # Player movement
    if keyboard.left:
        player.x -= 4
    if keyboard.right:
        player.x += 4
    if keyboard.up:
        player.y -= 4
    if keyboard.down:
        player.y += 4

    if player.colliderect(cookie):
        score += 1
        cookie.x += 80


def draw():
    screen.fill((30, 30, 30))
    player.draw()
    cookie.draw()
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=30, color="white")


pgzrun.go()
